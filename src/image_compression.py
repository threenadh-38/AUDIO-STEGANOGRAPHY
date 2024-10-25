from PIL import Image
import io

def compress_image(image_file_path):
    """
    Compress an image and return the compressed binary data.
    :param image_file_path: Path to the image file.
    :return: Compressed binary image data.
    """
    with Image.open(image_file_path) as img:
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='PNG', optimize=True, quality=85)
        return byte_arr.getvalue()

def decompress_image(compressed_data, output_image_path):
    """
    Decompress image binary data back to an image file.
    :param compressed_data: Compressed binary data of the image.
    :param output_image_path: Path to save the decompressed image.
    """
    with open(output_image_path, 'wb') as image_file:
        image_file.write(compressed_data)