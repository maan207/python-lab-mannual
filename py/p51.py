# Python program to check whether an IP address is UP or DOWN using Ping
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-51")

import subprocess
ip = "10.0.2.15"
print("\nChecking IP Address:", ip)
result = subprocess.run(
    ["ping", "-c", "1", "-W", "2", ip],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
if result.returncode == 0:
    print("IP Address", ip, "is UP")
else:
    print("IP Address", ip, "is DOWN")

