from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_data(data, key):
    """
    Encrypt data using AES encryption.
    :param data: Data to be encrypted (binary).
    :param key: AES key (must be 16, 24, or 32 bytes).
    :return: Initialization vector and ciphertext.
    """
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_data(iv, ct, key):
    """
    Decrypt AES encrypted data.
    :param iv: Initialization vector.
    :param ct: Ciphertext (encrypted data).
    :param key: AES key for decryption.
    :return: Decrypted plaintext data.
    """
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt