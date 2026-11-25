url = input("Enter a URL: ") suspicious_keywords = [ "login",
"verify",
"bank", "password", "secure",
"update",
"free", "confirm"
]
found = []
for keyword in suspicious_keywords:
if keyword in url.lower():
found.append(keyword) if found:
print("Suspicious Keywords Found:") for keyword in found:
print(keyword) else:
print("No Suspicious Keywords Found.")
