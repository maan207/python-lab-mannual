#Write a Python program to create a table, insert records, retrieve and display records from a table.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-33")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="marwadi" )
print("Database Connected Successfully")
mycursor = mydb.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    name VARCHAR(255), city VARCHAR(255))""")
print("Table created successfully")
sql = "INSERT INTO customers (name, city) VALUES (%s, %s)"
records = [
    ("Komal", "Mumbai"), ("Rahul", "Ahmedabad"), ("Priya", "Rajkot"), ("Amit", "Surat")]
mycursor.executemany(sql, records)
mydb.commit()
print("Records inserted successfully")
mycursor.execute("SELECT * FROM customers")
print("\nCustomer Records:")
for record in mycursor.fetchall():
    print("Name:", record[0], "| City:", record[1])
mycursor.close()
mydb.close()
