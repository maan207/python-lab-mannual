# Python program to accept a domain name and display basic WHOIS information
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-43")

import whois

domain = input("Enter Domain Name: ")
result = whois.whois(domain)
print("\nBasic WHOIS Information:")
print("Domain Name:", result.domain_name)
print("Registrar:", result.registrar)
print("Creation Date:", result.creation_date)
print("Expiration Date:", result.expiration_date)
print("Name Servers:", result.name_servers)
print("Domain Status:", result.status)
