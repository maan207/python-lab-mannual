# Python program to detect email addresses using Regular Expressions
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-47")

import re

text = """
Contact us at support@cyberlab.com
For queries, email admin@gmail.com
Invalid email: user@com
"""
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails = re.findall(pattern, text)
print("\nDetected Email Addresses:")
for email in emails:
    print(email)
print("\nTotal Emails Found:", len(emails))

