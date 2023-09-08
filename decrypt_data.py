# decrypts our data if we need to.

from cryptography.fernet import Fernet


def decrypt_data(encrypted_data, key):
    """Decrypt the provided data using the given key."""
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return decrypted_data


def read_file(filename):
    """Read a file and return its content."""
    with open(filename, "rb") as file:
        return file.read()


def write_to_file(filename, content):
    """Write content to a file."""
    with open(filename, "w") as file:
        file.write(content)


# Read the encrypted data from the file
encrypted_data = read_file("encrypted_file.csv")

# The key used for encryption; ensure this is securely stored and retrieved
key = input("Enter the key used for encryption: ").encode()

# Decrypt the data
decrypted_data = decrypt_data(encrypted_data, key)

# Save the decrypted data to a new file
write_to_file("decrypted_file.csv", decrypted_data)
