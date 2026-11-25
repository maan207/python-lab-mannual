# Python program to create a Pie Chart
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-38")

import matplotlib.pyplot as plt

subjects = ["Python", "DBMS", "CNS", "CLSC"]
marks = [85, 78, 92, 80]
plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Subject-wise Marks Distribution")
plt.show()

