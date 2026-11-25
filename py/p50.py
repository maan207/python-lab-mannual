
# Python program to check files in a directory using os library
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-50")

import os
directory = "."
if os.path.exists(directory):
    print("\nFiles in the Current Directory:")
    items = os.listdir(directory)

    for item in items:
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            print(item)
else:
    print("Directory does not exist.")
