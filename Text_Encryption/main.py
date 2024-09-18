from aes_des import aes_encrypt, aes_decrypt, des_encrypt, des_decrypt
from rsa_encryption import rsa_encrypt, rsa_decrypt, public_key, private_key

def main():
    print("Text Encryption Tool")
    print("Choose an encryption method:")
    print("1. AES")
    print("2. DES")
    print("3. RSA")

    choice = input("Enter your choice (1/2/3): ")

    if choice in ['1', '2', '3']:
        text = input("Enter the text to encrypt: ")

        if choice == '1':  # AES
            key = input("Enter a 16-byte encryption key: ")
            encrypted_text = aes_encrypt(text, key)
            print("\nEncrypted Text (AES):", encrypted_text)
            print("Decrypted Text (AES):", aes_decrypt(encrypted_text, key))

        elif choice == '2':  # DES
            key = input("Enter an 8-byte encryption key: ")
            encrypted_text = des_encrypt(text, key)
            print("\nEncrypted Text (DES):", encrypted_text)
            print("Decrypted Text (DES):", des_decrypt(encrypted_text, key))

        elif choice == '3':  # RSA
            encrypted_text = rsa_encrypt(text, public_key)
            print("\nEncrypted Text (RSA):", encrypted_text)
            print("Decrypted Text (RSA):", rsa_decrypt(encrypted_text, private_key))

    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
