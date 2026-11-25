# Python program to demonstrate the use of DataFrames in Python
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-36")

import pandas as pd

data = {
    "Name": ["Komal", "Rahul", "Priya", "Amit"],
    "Course": ["MSc CS & CL", "MSc CS & CL", "MSc CS & CL", "MSc CS & CL"],
    "City": ["Jamnagar", "Ahmedabad", "Rajkot", "Surat"],
    "Marks": [85, 78, 92, 80]
}
df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

print("\nStudent Names:")
print(df["Name"])

print("\nFirst Two Records:")
print(df.head(2))

