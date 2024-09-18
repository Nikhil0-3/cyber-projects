from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    # Padding to make the text a multiple of 16 bytes for AES and 8 bytes for DES
    while len(text) % 16 != 0:
        text += ' '
    return text

# AES Encryption and Decryption
def aes_encrypt(plain_text, key):
    key = pad(key).encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def aes_decrypt(encrypted_text, key):
    key = pad(key).encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = cipher.decrypt(decoded_encrypted_text)
    return decrypted_text.decode('utf-8').strip()

# DES Encryption and Decryption
def des_encrypt(plain_text, key):
    key = pad(key)[:8].encode('utf-8')  # DES uses an 8-byte key
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text)[:8].encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def des_decrypt(encrypted_text, key):
    key = pad(key)[:8].encode('utf-8')
    cipher = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = cipher.decrypt(decoded_encrypted_text)
    return decrypted_text.decode('utf-8').strip()
