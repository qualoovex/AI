#Programmer: Granger
#Date:3-12-24
#Program: Password Generator
#Recourse: https://www.zdnet.com/article/how-to-write-better-chatgpt-prompts-in-5-steps/


import hashlib
import getpass
import secrets

def hash_password(password, salt):
    # Combine password and salt, and then hash using SHA-256
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed_password

# Get user input for password without displaying characters
password = getpass.getpass("Enter your password: ")

# Generate a random salt
salt = secrets.token_hex(16)

# Hash the password with the salt
hashed_password = hash_password(password, salt)

# Print the hashed password and salt (for demonstration purposes)
print("Salt:", salt)
print("Hashed Password:", hashed_password)



