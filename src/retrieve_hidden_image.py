import os
import base64  # Import base64 for encoding and decoding
from audio_to_binary import audio_to_binary  # Import function to convert audio to binary
from cryptography import decrypt_data  # Import function to decrypt data
from lsb_steganography import extract_data_from_audio  # Import function to extract data from audio

def retrieve_hidden_image(stego_audio_path, key):
    """
    Retrieve the hidden image from the stego audio file.
    :param stego_audio_path: Path to the stego audio file containing the hidden image.
    :param key: AES key used for decryption.
    :return: Decrypted image binary data.
    """
    # Step 1: Convert the stego audio file to binary
    audio_binary = audio_to_binary(stego_audio_path)  # Call function to convert audio to binary
    print("Converted stego audio to binary.")

    # Step 2: Extract the image data from the audio binary data
    image_binary, hidden_data_length = extract_data_from_audio(audio_binary)  # Call function to extract data
    print("Extracted hidden image binary data from audio.")

    # Step 3: Prepare for decryption
    try:
        # Ensure the extracted data has the correct padding
        padding_needed = len(image_binary) % 4
        if padding_needed:
            image_binary += '=' * (4 - padding_needed)  # Add necessary padding

        # Convert the binary string to bytes
        # Split the binary string into chunks of 8 bits
        image_bytes = bytearray()
        for i in range(0, len(image_binary), 8):
            byte = image_binary[i:i + 8]  # Get the next 8 bits
            if len(byte) < 8:
                break  # Ignore incomplete byte
            image_bytes.append(int(byte, 2))  # Convert to integer and append to bytearray

        # Verify the length of the extracted data
        if len(image_bytes) < 16:
            raise ValueError("Extracted data is too short to contain a valid IV.")

        # Extract the IV and ciphertext
        iv = image_bytes[:16]  # First 16 bytes are the IV
        ct = image_bytes[16:]  # The rest is the ciphertext
        
        # Perform decryption using the extracted binary data
        decrypted_image_data = decrypt_data(iv, ct, key)  # Call function to decrypt data
        print("Decrypted the hidden image data.")
        
        return decrypted_image_data  # Return the decrypted image data

    except Exception as e:
        print("An error occurred during retrieval:", str(e))
