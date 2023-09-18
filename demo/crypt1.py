# Import the cryptography library
# - you should already have the library by running `pip install cryptography`
from cryptography.fernet import Fernet

# Generate a Fernet Key
key = Fernet.generate_key()

# Create a Fernet object with a key
crypt = Fernet(key)

# Define an encryption function
def encrypt(s, crypt):
    result = crypt.encrypt(s.encode())
    return result

# Define a decryption function
def decrypt(s, crypt):
    result = crypt.decrypt(s)
    return result

message = "Hello World"

encrypted = encrypt(message, crypt)
decrypted = decrypt(encrypted, crypt)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)