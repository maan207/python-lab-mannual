# Python program to perform a WHOIS lookup for a given domain name
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-42")

import whois

domain = "google.com"
result = whois.whois(domain)
print("\nWHOIS Information:")
print("Domain Name:", result.domain_name)
print("Registrar:", result.registrar)
print("Creation Date:", result.creation_date)
print("Expiration Date:", result.expiration_date)
print("Name Servers:", result.name_servers)
print("Domain Status:", result.status)
