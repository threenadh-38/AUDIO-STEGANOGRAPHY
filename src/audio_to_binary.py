import wave
import numpy as np

def audio_to_binary(audio_file_path):
    """
    Convert a stereo .wav audio file (16-bit depth) to binary data.
    :param audio_file_path: Path to the audio file.
    :return: Binary data of the audio.
    """
    with wave.open(audio_file_path, 'rb') as audio:
        frames = audio.readframes(audio.getnframes())
        binary_data = np.frombuffer(frames, dtype=np.int16)
    return binary_data

def binary_to_audio(binary_data, output_file_path, params):
    """
    Convert binary data back to a .wav audio file.
    :param binary_data: Binary data to convert back to audio.
    :param output_file_path: Output path for the audio file.
    :param params: Audio parameters (nchannels, sampwidth, framerate, nframes, comptype, compname).
    """
    with wave.open(output_file_path, 'wb') as audio:
        audio.setparams(params)
        audio.writeframes(binary_data.tobytes())