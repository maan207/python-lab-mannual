# Python program to create a Bar Graph
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565010")
print("Practical-40")

import matplotlib.pyplot as plt

subjects = ["Python", "DBMS", "CNS", "CLSC"]
marks = [85, 78, 92, 80]
plt.bar(subjects, marks)
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
