# Python program to demonstrate different ways of creating DataFrames
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-37")

import pandas as pd
import numpy as np

data1 = {
    "Name": ["Komal", "Rahul"],
    "Marks": [85, 78]
}
df1 = pd.DataFrame(data1)
print("\n1. DataFrame using Dictionary:")
print(df1)

data2 = [
    {"Name": "Priya", "City": "Rajkot"},
    {"Name": "Amit", "City": "Surat"}
]
df2 = pd.DataFrame(data2)
print("\n2. DataFrame using List of Dictionaries:")
print(df2)

data3 = [
    ["Komal", 85],
    ["Rahul", 78]
]
df3 = pd.DataFrame(data3, columns=["Name", "Marks"])
print("\n3. DataFrame using List of Lists:")
print(df3)

data4 = np.array([
    ["Priya", 92],
    ["Amit", 80]
])
df4 = pd.DataFrame(data4, columns=["Name", "Marks"])
print("\n4. DataFrame using NumPy Array:")
print(df4)

