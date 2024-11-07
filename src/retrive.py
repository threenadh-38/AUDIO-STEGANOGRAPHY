import os
import base64  # Import the base64 module
from main import *
key = b'ThisIsASecretKey'  # AES key (ensure it's 16, 24, or 32 bytes)
output_image_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\images\output-image.png"
output_audio_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\Audio\output-audio\stego-audio.wav"  # Output audio file
try:
        # You would need to know the length of the data you embedded to extract it correctly.
    extracted_image_binary = extract_data_from_audio(stego_audio_binary, len(image_binary))
        
        # Convert the extracted binary back to bytes
    extracted_encrypted_image_data = bytes(int(extracted_image_binary[i:i + 8], 2) for i in range(0, len(extracted_image_binary), 8))

        # Decrypt the extracted data (if needed)
    decrypted_image_data = decrypt_data(iv, base64.b64encode(extracted_encrypted_image_data).decode('utf-8'), key)

        # Save the decrypted image data back to an image file (optional)
    with open(output_image_path, "wb") as img_file:
            img_file.write(decrypted_image_data)
    print("Image extracted and decrypted successfully.")

except Exception as e:
    print("An error occurred:", str(e))

print("Image extracted and decrypted successfully.")