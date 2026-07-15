
import csv
import sqlite3


connection = sqlite3.connect("retail.db")

cursor = connection.cursor()

cursor.execute("DELETE FROM staging_raw;") # emptying the staging db

connection.commit()

connection.close()

def rows (csv_file): # this function hands rows one by one

    with open(csv_file, mode = "r", encoding = "ISO-8859-1", newline = "") as file:

        reader = csv.reader(file)

        next (reader)

        for row in reader:
            yield row

def loading (db_file, csv_file): # this function puts data into sqline in chunks of 5000 

    connection = sqlite3.connect(db_file)

    cursor = connection.cursor()

    bucket = [] # this stores rows

    for row in rows(csv_file):

          bucket.append(row) # putting the row in the bucket

          if (len(bucket) == 5000):
              
              cursor.executemany("INSERT INTO staging_raw VALUES (?, ?, ?, ?, ?, ?, ?, ?);", bucket) # inserting the 50000 rows at once

              connection.commit()

              bucket.clear()

    if (len(bucket) > 0):
        cursor.executemany("INSERT INTO staging_raw VALUES (?, ?, ?, ?, ?, ?, ?, ?);", bucket) # same thing as above but with the remaining rows

        connection.commit()

    connection.close()

loading(db_file = "retail.db", csv_file = "Online_Retail.csv")
    

