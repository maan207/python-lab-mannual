import base64
message = input("Enter a message: ")
encoded = base64.b64encode(message.encode()) print("Encoded Message:", encoded.decode()) decoded = base64.b64decode(encoded).decode() print("Decoded Message:", decoded)
