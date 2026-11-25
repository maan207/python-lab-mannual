
# Python program to display the domain registrar name using WHOIS
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-44")

import whois

domain = "tryhack.com"
result = whois.whois(domain)
print("\nDomain Name:", domain)
print("Registrar Name:", result.registrar)
