import numpy as np
import scipy.io.wavfile as wav
import os

os.makedirs("data/raw", exist_ok=True)

sample_rate = 44100
duration = 5.0
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_signal = 0.5 * np.sin(2 * np.pi * 440 * t)
audio_int16 = (audio_signal * 32767).astype(np.int16)

# Generate dummy test files matching the 4-test bench matrix
wav.write("data/raw/test01_bias3v_fuzz100.wav", sample_rate, audio_int16)
wav.write("data/raw/test01_bias4.5v_fuzz100.wav", sample_rate, audio_int16)
wav.write("data/raw/test02_cap2.2uf_fuzz100.wav", sample_rate, audio_int16)
wav.write("data/raw/test02_cap47nf_fuzz100.wav", sample_rate, audio_int16)

print("✅ Synthetic audio files created successfully in /data/raw/")
