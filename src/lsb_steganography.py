import numpy as np

def embed_data_in_audio(audio_binary, data_binary):
    """
    Embed binary data into the least significant bit (LSB) of an audio file.
    :param audio_binary: Binary data of the audio file.
    :param data_binary: Binary data to embed.
    :return: Modified audio binary data with the embedded data.
    """
    audio_array = np.array(audio_binary)  # Convert audio binary data to numpy array
    data_length = len(data_binary)  # Get the length of the data to embed
    
    # Check if the data fits into the audio binary
    if data_length > audio_array.size:
        raise ValueError("Data is too large to embed in the audio file.")

    # Embed each bit of the data into the least significant bit of the audio samples
    for i in range(data_length):
        audio_array[i] = (audio_array[i] & 0b11111110) | (int(data_binary[i]) & 0b00000001)

    return audio_array

def extract_data_from_audio(audio_binary, data_length):
    """
    Extract binary data from the least significant bits (LSB) of an audio file.
    :param audio_binary: Binary data of the audio file.
    :param data_length: Length of the data to extract.
    :return: Extracted binary data.
    """
    audio_array = np.array(audio_binary)  # Convert audio binary data to numpy array
    data_binary = ''  # Initialize an empty string to store extracted data

    # Extract the LSB from each audio sample to get the embedded data
    for i in range(data_length):
        data_binary += str(audio_array[i] & 0b00000001)  # Get the LSB

    return data_binary