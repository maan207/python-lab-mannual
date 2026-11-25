# Write a Python program to update records in a MySQL table and display records.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-34")

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="marwadi" )
print("Database Connected Successfully")
mycursor = mydb.cursor()
sql = "UPDATE customers SET city = %s WHERE name = %s"
values = ("Jamnagar", "Komal")
mycursor.execute(sql, values)
mydb.commit()
print("Record updated successfully")
mycursor.execute("SELECT * FROM customers")
print("\nUpdated Customer Records:")
for record in mycursor.fetchall():
    print("Name:", record[0], "| City:", record[1])
mycursor.close()
mydb.close()
