import rsa
import base64

# Generate RSA keys (public and private)
public_key, private_key = rsa.newkeys(512)

def rsa_encrypt(plain_text, pub_key):
    encrypted_text = rsa.encrypt(plain_text.encode('utf-8'), pub_key)
    return base64.b64encode(encrypted_text).decode('utf-8')

def rsa_decrypt(encrypted_text, priv_key):
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = rsa.decrypt(decoded_encrypted_text, priv_key)
    return decrypted_text.decode('utf-8')
