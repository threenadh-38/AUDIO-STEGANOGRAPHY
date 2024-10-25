import os
from retrieve_hidden_image import retrieve_hidden_image  # Import the function to retrieve hidden image

def main():
    """
    Main function to handle the retrieval of the hidden image from the stego audio.
    """
    # Define the path to the stego audio file and the AES key
    stego_audio_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\Audio\output-audio\stego-audio.wav"  # Path to the stego audio file
    key = b'ThisIsASecretKey'  # AES key (ensure it's 16, 24, or 32 bytes)

    # Call the function to retrieve the hidden image
    decrypted_image_data = retrieve_hidden_image(stego_audio_path, key)  # Retrieve the hidden image

    # Step 4: Reconstruct the image from binary data
    if decrypted_image_data:
        output_image_path = r"C:\Users\LENOVO\OneDrive\Documents\Audio Steganography\images\output-image\output_image.png"  # Output path for the image
        with open(output_image_path, 'wb') as image_file:  # Open the output image file in binary write mode
            image_file.write(decrypted_image_data)  # Write the decrypted image data to the file
        print("Image reconstruction completed. Output image saved at", output_image_path)  # Confirm completion

if __name__ == "__main__":
    main() # Call the main function
