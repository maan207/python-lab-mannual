
# Python program to check open ports using socket
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-48")
import socket
target = "127.0.0.1"
ports = [21, 22, 80, 443]
print("\nScanning Target:", target)
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED")
    s.close()
print("\nPort Scanning Completed.")
