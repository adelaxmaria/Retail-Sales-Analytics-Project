import csv
import sqlite3

connection = sqlite3.connect("retail.db")

cursor = connection.cursor()

# creating 4 staging tables 

products_table = """  
CREATE TABLE IF NOT EXISTS products (
    StockCode TEXT PRIMARY KEY,
    Description TEXT
);
"""
cursor.execute(products_table)

connection.commit()

customers_table = """
CREATE TABLE IF NOT EXISTS customers(
    CustomerID TEXT PRIMARY KEY,
    Country TEXT
);
"""
cursor.execute(customers_table)

connection.commit()

invoices_table = """
CREATE TABLE IF NOT EXISTS invoices(
    InVoiceNo TEXT PRIMARY KEY,
    InVoiceDate TEXT,
    CustomerID TEXT
);
"""

cursor.execute(invoices_table)

connection.commit()

invoice_lines_table = """
CREATE TABLE IF NOT EXISTS invoice_lines(
    line INTEGER PRIMARY KEY AUTOINCREMENT,
    InVoiceNo TEXT,
    StockCode TEXT,
    Quantity INTEGER,
    UnitPrice REAL
);

"""
cursor.execute(invoice_lines_table)

connection.commit()

# adding actual data into the tables

inserting_products = """ INSERT OR IGNORE INTO products (StockCode, Description)
    SELECT 
    StockCode,
    Description
    FROM staging_raw;
"""

cursor.execute(inserting_products)

connection.commit()

inserting_customers = """ INSERT OR IGNORE INTO customers (CustomerID, Country)
    SELECT 
    CustomerID,
    Country
    FROM staging_raw;
"""
cursor.execute(inserting_customers)

connection.commit()


inserting_invoices = """ INSERT OR IGNORE INTO invoices (InVoiceNo, InVoiceDate, CustomerID) 
    SELECT
    InVoiceNo, 
    InVoiceDate, 
    CustomerID
    FROM staging_raw;
"""

cursor.execute(inserting_invoices)

connection.commit()

inserting_invoice_lines = """ INSERT OR IGNORE INTO invoice_lines (InVoiceNo, StockCode, Quantity, UnitPrice)
    SELECT
    InVoiceNo, 
    StockCode, 
    CAST(Quantity AS INTEGER), 
    CAST(UnitPrice AS REAL)
    FROM staging_raw;
"""

cursor.execute(inserting_invoice_lines)

connection.commit()

connection.close()

print("Success.")