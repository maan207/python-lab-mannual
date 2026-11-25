import ipaddress
ip = input("Enter an IP Address: ") try:
address = ipaddress.ip_address(ip) if address.is_private:
print("The given IP Address is Private.") else:
print("The given IP Address is Public.") except ValueError:
print("Invalid IP 
