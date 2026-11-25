
# Python program to generate hash values using hashlib
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-49")

import hashlib

text = "Cyber Security"
data = text.encode()
md5_hash = hashlib.md5(data).hexdigest()
sha1_hash = hashlib.sha1(data).hexdigest()
sha256_hash = hashlib.sha256(data).hexdigest()
print("\nOriginal String:", text)
print("\nMD5 Hash:", md5_hash)
print("SHA-1 Hash:", sha1_hash)
print("SHA-256 Hash:", sha256_hash)
