#%% to learn SQLite
import sqlite3
import os
import csv

# set the directory
path = "/Users/horse/Desktop/Coursera/Python/SQLite"
os.chdir(path)

#%% connect to a database 
sqlite_file = 'DB_test'    # name of the sqlite database file
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()


#%% query data
cursor.execute("select * from sample_data where dim='i' limit 10")

with open("out.csv", "wb") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor)
    

#%% Closing the connection to the database file
conn.close()
