filename = input("Enter file name: ") risky_extensions = [
".exe",
".bat",
".cmd",
".vbs",
".js",
".scr",
".msi",
".ps1"
]
file_extension = "." + filename.split(".")[-1].lower() if file_extension in risky_extensions:
print("Warning! Potentially Risky File Extension.") else:
print("File Extension is Not in the Risk List.")
