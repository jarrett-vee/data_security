# decrypts our data if we need to.

from cryptography.fernet import Fernet
import os


def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data


def read_file(filename):
    with open(filename, "rb") as file:
        return file.read()


def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


encrypted_file_path = os.path.join("decrypt_and_encrypt", "encrypted_file.csv")
encrypted_data = read_file(encrypted_file_path)

key = input("Enter the key used for encryption: ").encode()

decrypted_data = decrypt_data(encrypted_data, key)

decrypted_file_path = os.path.join("decrypt_and_encrypt", "decrypted_file.csv")
write_to_file(decrypted_file_path, decrypted_data)
