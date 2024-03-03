import librosa
import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
# import os
# import IPython.display as ipd
import pandas as pd

def load_and_process_audio(file_path):
    """
    Load an MP3 file and process it for further signal processing.

    Parameters:
    - file_path (str): Path to the MP3 file.

    Returns:
    - audio_data (np.ndarray): Processed audio data.
    - sr (int): Actual sample rate of the loaded audio.
    """
    # Load the audio file
    audio_data, sr = librosa.load(file_path)

    return audio_data, sr

def plot_frequency_spectrum(audio_data, sr):
    """
    Perform FFT on the processed audio data and plot the frequency spectrum.

    Parameters:
    - audio_data (np.ndarray): Processed audio data.
    - sr (int): Sample rate of the audio data.

    Returns:
    None
    """
    # Perform FFT (Fourier Transforms)
    X = fft(audio_data)
    N = len(X)
    n = np.arange(N)
    T = N / sr
    freq = n / T
    df = pd.DataFrame({'Frequency':freq, "Amplitude":np.abs(X)})
    threshold_percentage = 0.5
    prominent_frequencies = df[(df['Frequency'] < 150) & (df['Amplitude'] > threshold_percentage*max(np.abs(X)))]

    # Plot frequency spectrum
    plt.figure(figsize=(13, 8))
    
    # Subplot 2: Frequency Spectrum
    plt.subplot(211)
    plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.title('Frequency Spectrum')
    plt.xlim(0, 450)  # Adjust the frequency range as needed
    
    
    # Subplot 1: Time-domain Signal
    plt.subplot(212)
    plt.plot(np.arange(len(audio_data)) / sr, audio_data, 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Time-domain Signal')
    
    # Adjust layout for better visualization
    plt.subplots_adjust(hspace=0.6)  # Add spacing between subplots
    
    # Display the plot
    plt.show()
    print(prominent_frequencies.to_string(index=False))
