# Write a Python program to delete records from a MySQL table and display records.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565010")
print("Practical-35")

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marwadi"
)

print("Database Connected Successfully")
mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE name = %s"
values = ("Amit",)

mycursor.execute(sql, values)
mydb.commit()

print("Records deleted successfully")

mycursor.execute("SELECT * FROM customers")
print("\nRemaining Customer Records:")

for record in mycursor.fetchall():
    print("Name:", record[0], "| City:", record[1])

mycursor.close()
mydb.close()


