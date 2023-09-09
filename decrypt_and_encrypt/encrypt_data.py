# encrypts our super secret data using Fernet.

import csv
import os
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def write_to_file(filename, content):
    with open(filename, "wb") as file:
        file.write(content)


key = generate_key()
print(f"Generated Key (Save this for decryption): {key}")

data_path = "../data_security/data.csv"
data = read_file(data_path)
print(f"Original Data:\n{data}")

encrypted_data = encrypt_data(data, key)

path = os.path.join("decrypt_and_encrypt", "encrypted_file.csv")
write_to_file(path, encrypted_data)
