#Encryption program

import hashlib
def encrypt_password(password):
    """Encrypts the password using SHA-256 hashing."""
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature
def main():
    print("Welcome to the Password Encryption Program")
    password = input("Please enter your password: ")
    encrypted_password = encrypt_password(password)
    print(f"Your encrypted password is: {encrypted_password}")
    
    # Optionally, you can verify the password
    verify_password = input("Re-enter your password to verify: ")
    if encrypt_password(verify_password) == encrypted_password:
        print("Password verified successfully!")
    else:
        print("Password verification failed.")
if __name__ == "__main__":
    main()
