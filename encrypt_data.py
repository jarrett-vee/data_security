# encrypts our super secret data using Fernet.

import csv
from cryptography.fernet import Fernet


def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()


def encrypt_data(data, key):
    """Encrypt the provided data using the given key."""
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data


def read_file(filename):
    """Read a file and return its content."""
    with open(filename, "r") as file:
        return file.read()


def write_to_file(filename, content):
    """Write content to a file."""
    with open(filename, "wb") as file:
        file.write(content)


# Generate a new key
key = generate_key()
print(f"Generated Key (Save this for decryption): {key}")

# Read data from CSV file
data = read_file("targets1.csv")
print(f"Original Data:\n{data}")

# Encrypt the data
encrypted_data = encrypt_data(data, key)

# Save encrypted data to a new file
write_to_file("encrypted_file.csv", encrypted_data)
