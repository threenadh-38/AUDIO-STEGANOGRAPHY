import os
import base64  # Import the base64 module
from audio_to_binary import audio_to_binary, binary_to_audio
from cryptography import encrypt_data, decrypt_data
from image_compression import compress_image
from image_processing import image_to_binary
from lsb_steganography import embed_data_in_audio, extract_data_from_audio

# Set paths for input files (adjust as needed)
audio_file_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\Audio\input-audio\input.wav"  # Input audio file
image_file_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\images\input-image\input_image.png"  # Input image file
output_audio_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\Audio\output-audio\stego-audio.wav"  # Output audio file
key = b'ThisIsASecretKey'  # AES key (ensure it's 16, 24, or 32 bytes)

try:
    # Step 1: Convert audio to binary
    audio_binary = audio_to_binary(audio_file_path)
    print("Audio to Binary Convertion")
    # Step 2: Compress the image and get its binary data
    compressed_image_data = compress_image(image_file_path)
    print("Image Compression is done")
    # Step 3: Encrypt the compressed image data using AES encryption
    iv, encrypted_image_data = encrypt_data(compressed_image_data, key)
    print(iv,len(encrypted_image_data))
    print("Encryption using AES method is done!")
    # Step 4: Convert the encrypted image data to binary format
    # Decode the base64 encoded string to bytes
    encrypted_image_bytes = base64.b64decode(encrypted_image_data)
    print("converting to binary format is done")
    # Convert the encrypted image bytes to binary format
    image_binary = image_to_binary(encrypted_image_bytes)
    
    # Step 5: Embed the image binary data into the audio binary using LSB steganography
    stego_audio_binary = embed_data_in_audio(audio_binary, image_binary)
    # Step 6: Convert the modified binary back into an audio file and save it
    binary_to_audio(stego_audio_binary, output_audio_path, (2, 2, 44100, len(stego_audio_binary), 'NONE', 'not compressed'))

    print("Steganography completed. Stego-audio saved at", output_audio_path)
    # Optional: Extract the message from the stego audio (if needed)
    # You would need to know the length of the data you embedded to extract it correctly.
    # extracted_image_binary = extract_data_from_audio(stego_audio_binary, len(image_binary))
    
    # # Convert the extracted binary back to bytes
    # extracted_encrypted_image_data = bytes(int(extracted_image_binary[i:i + 8], 2) for i in range(0, len(extracted_image_binary), 8))

    # # Decrypt the extracted data (if needed)
    # decrypted_image_data = decrypt_data(iv, base64.b64encode(extracted_encrypted_image_data).decode('utf-8'), key)

    # # Save the decrypted image data back to an image file (optional)
    # with open("decrypted_image.png", "wb") as img_file:
    #     img_file.write(decrypted_image_data)

    # print("Image extracted and decrypted successfully.")

except Exception as e:
    print("An error occurred:", str(e))