
#Multilevel Inheritance : Security tool -> NetworkSecurity -> Firewall
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-23_1")
class Security:
    def protect(self):
        print("System protection is enabled")
class NetworkSecurity(Security):
    def monitor_network(self):
        print("Network traffic is monitored")
class Firewall(NetworkSecurity):
    def block_traffic(self):
        print("Malicious traffic is blocked")

f = Firewall()
f.protect()
f.monitor_network()
f.block_traffic()

#Multiple Inheritance : Encryption + Authentication -> SecureSystem
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-23_2")
class Encryption:
    def encrypt(self):
        print("Data is encrypted")

class Authentication:
    def authenticate(self):
        print("user authentication is performed")

class SecureSystem(Encryption, Authentication):
    def secure_data(self):
        print("System provides secure data access")

s = SecureSystem()
s.encrypt()
s.authenticate()
s.secure_data()

#Hierarchical Inheritance : Security System -> IDS and IPS
print("Program :- MSc CS & CL Semester-1")
print("Enrollment : 92600565012")
print("Practical-23_3")
class SecuritySystem:
    def monitor(self):
        print("Network is bring monitored")

class IDS(SecuritySystem):
    def detect(self):
        print("IDS detects suspicious activity")

class IPS(SecuritySystem):
    def prevent(self):
        print("IPS prevents malicious activity")

i = IDS()
p = IPS()

i.monitor()
i.detect()
p.prevent()
