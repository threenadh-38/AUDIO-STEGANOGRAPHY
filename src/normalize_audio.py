# Amplitude Normalization 
import librosa

def normalize_audio(audio_file, target_range=(-1, 1)):
    y, sr = librosa.load(audio_file)
    y_normalized = librosa.util.normalize(y, norm=np.inf, axis=None)  # Normalize to [-1, 1]
    y_scaled = (y_normalized * (target_range[1] - target_range[0])) + target_range[0]  # Scale to desired range
    return y_scaled, sr

# Example usage:
audio_file = "your_audio_file.wav"
normalized_audio, sr = normalize_audio(audio_file)

# Save the normalized audio file
librosa.output.write_wav("normalized_audio.wav", normalized_audio, sr)