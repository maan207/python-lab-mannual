#Write a Python program to connect Python with MySQL database and display a message “Database Connected Successfully”.
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-32")
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor=mydb.cursor()
mycursor.execute("create database marwadi")
print("Database created")
mydb.close()
