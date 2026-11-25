
# Python program to create a Line Graph
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-41")

import matplotlib.pyplot as plt

subjects = ["Python", "DBMS", "CNS", "CLSC"]
marks = [85, 78, 92, 80]
plt.plot(subjects, marks, marker='o', linestyle='-')
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
