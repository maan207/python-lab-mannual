
# Python program to display the domain creation date using WHOIS
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-45")

import whois

domain = "chatgpt.com"
result = whois.whois(domain)
print("\nDomain Name:", domain)
print("Creation Date:", result.creation_date)
