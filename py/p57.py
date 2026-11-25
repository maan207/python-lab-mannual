log_data = """
User admin login failed User vishal login successful User root login failed
User guest login failed
User student login successful User admin login failed
"""
failed_count = 0
for line in log_data.splitlines():
if "login failed" in line.lower():
failed_count += 1 print("Security Log:") print(log_data)
print("Total Failed Login Attempts:", failed_count)

