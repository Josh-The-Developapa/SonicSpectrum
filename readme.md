# Project SonicSpectrum

## Overview

Welcome to Project SonicSpectrum! This repository contains code dedicated to analyzing audio files using Fast Fourier Transforms (FFT) and visualizing the frequency spectrum in a sinusoidal graph. Created by Joshua Mukisa & Emmanuel Asiimwe, this project aims to provide insights into the frequency components of audio signals, with a particular focus on the famous track "Pirates of the Caribbean - He's a Pirate.mp3".

## Introduction

This repository contains code dedicated to applying Fast Fourrier Transforms (FFT) to an audio file, and visualising it in a sinusoidal graph.

Audio File Name: **Pirates of the Caribbean - He's a Pirate.mp3**

FFT (Fast Fourier Transform) is an algorithm used to compute the discrete Fourier transform efficiently.

The Discrete Fourier Transform (DFT) is mathematically represented as follows:

$$X_k = \sum_{m=0}^{n-1} x_m \cdot e^{-i \frac{2\pi k m}{n}} \quad \text{for} \quad k = 0, 1, \ldots, n-1$$

In this expression:

- $X_k$ represents the $k$-th element of the DFT output.
- $x_m$ denotes the $m$-th element of the input sequence.
- $e^{-i \frac{2\pi k m}{n}}$ is the complex exponential term, where $e$ is the base of the natural logarithm, $i$ is the imaginary unit, and $\pi$ is the mathematical constant pi.

Additionally, $e^{i\frac{2\pi}{n}}$ corresponds to a primitive $n$-th root of 1. This term is crucial in the computation of the DFT, as it defines the angular frequency associated with each frequency component.


## Getting Started

To get started with Project SonicSpectrum, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have the necessary dependencies installed, including librosa, numpy, matplotlib, and pandas. (necessary dependencies can be found in the requirements.txt file)
3. Open the Jupyter Notebook file "SonicSpectrum.ipynb" to explore the code and analyze audio data.
4. Customize the code as needed for your own audio files or projects.

## Authors

- **Joshua Mukisa**
- **Emmanuel Asiimwe**

## Audio File Information

- **File Name**: Pirates of the Caribbean - He's a Pirate.mp3

## Contributing

Contributions to Project SonicSpectrum are welcome! If you have ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.
