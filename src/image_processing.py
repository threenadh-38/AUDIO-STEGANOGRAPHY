def image_to_binary(image_data):
    """
    Convert compressed image data to binary format.
    :param image_data: Binary image data (compressed).
    :return: Binary representation of the image.
    """
    return ''.join(format(byte, '08b') for byte in image_data)

def binary_to_image(binary_data, output_image_path):
    """
    Convert binary data back into an image.
    :param binary_data: Binary data to convert back into an image.
    :param output_image_path: Path to save the output image.
    """
    byte_data = bytearray(int(binary_data[i:i + 8], 2) for i in range(0, len(binary_data), 8))
    with open(output_image_path, 'wb') as image_file:
        image_file.write(byte_data)