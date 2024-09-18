from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import io

# Constants
KEY = b'Sixteen byte key'  # Must be 16, 24, or 32 bytes long
IV_SIZE = 16  # AES block size

def encrypt_image(image_path, output_path):
    """
    Encrypt an image and save it to the output path.
    """
    with Image.open(image_path) as img:
        # Convert image to bytes
        img_bytes = img.tobytes()
        
        # Save image dimensions and mode
        width, height = img.size
        mode = img.mode
        
        # Create a new IV for each encryption
        iv = os.urandom(IV_SIZE)
        
        # Create AES cipher object
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        
        # Pad the image bytes and encrypt
        padded_data = pad(img_bytes, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        
        # Write IV, dimensions, mode, and encrypted data to file
        with open(output_path, 'wb') as file:
            file.write(iv)
            file.write(width.to_bytes(4, byteorder='big'))
            file.write(height.to_bytes(4, byteorder='big'))
            file.write(mode.encode('utf-8').ljust(8, b'\x00'))  # Ensure mode is 8 bytes
            file.write(encrypted_data)

def decrypt_image(encrypted_path, output_path):
    """
    Decrypt an image and save it to the output path.
    """
    with open(encrypted_path, 'rb') as file:
        # Read IV, dimensions, mode, and encrypted data
        iv = file.read(IV_SIZE)
        width = int.from_bytes(file.read(4), byteorder='big')
        height = int.from_bytes(file.read(4), byteorder='big')
        mode = file.read(8).strip(b'\x00').decode('utf-8')
        encrypted_data = file.read()
        
        # Create AES cipher object
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        
        # Decrypt and unpad the data
        padded_data = cipher.decrypt(encrypted_data)
        img_bytes = unpad(padded_data, AES.block_size)
        
        # Convert bytes back to image
        img = Image.frombytes(mode, (width, height), img_bytes)
        img.save(output_path)

if __name__ == "__main__":
    # Example usage
    encrypt_image('input_image.jpg', 'encrypted_image.enc')
    decrypt_image('encrypted_image.enc', 'decrypted_image.jpg')
