file1 = input("Enter first file name: ") file2 = input("Enter second file name: ") try:
with open(file1, "rb") as f1:
data1 = f1.read()
with open(file2, "rb") as f2:
data2 = f2.read() if data1 == data2:
print("Both files contain identical data.") else:
print("Both files contain different data.") except FileNotFoundError:
print("Error: File not found.")
