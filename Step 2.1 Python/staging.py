import sqlite3

connection = sqlite3.connect("retail.db") # connecting to the db

cursor = connection.cursor() # creating a cursor to the db

create_table = """
CREATE TABLE IF NOT EXISTS staging_raw (
    InvoiceNo TEXT,
    StockCode TEXT,
    Description TEXT,
    Quantity TEXT,
    InvoiceDate TEXT,
    UnitPrice TEXT,
    CustomerID TEXT,
    Country TEXT
); """

cursor.execute(create_table) # executing

connection.commit() # saving changes
connection.close()  

