import librosa
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import os
import IPython.display as ipd
from utils import load_and_process_audio, plot_frequency_spectrum

BASE_DIR = '../data'
file_name = "Pirates-5secinterval.m4a" 

file_path = os.path.join(BASE_DIR, file_name)  # Replace with the actual path to your audio file
audio_data, sr = load_and_process_audio(file_path)

plot_frequency_spectrum(audio_data, sr)

ipd.Audio(audio_data, rate=sr)


