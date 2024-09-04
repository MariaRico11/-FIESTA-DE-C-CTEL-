# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:57:34 2024

@author: LENOVO
"""

import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

file_paths = [
    "audio Dani.mp3",
    "Audio_Daniela.mp3",
    "audio daniela.mp3",
    "ambiente audio.mp3"
]

audios = []

for file_path in file_paths:
    y, sr = librosa.load(file_path, sr=None)
    audios.append((y, sr))
    
print("Audios cargados")
colores = ['#f486bf', '#cf91ee', '#7addec'] 

# Mostrar formas de onda
plt.figure(figsize=(14, 10))
for i, (y, sr) in enumerate(audios[:-1], start=1):
    duration = len(y) / sr
    time = np.linspace(0, duration, len(y))
    
    plt.subplot(3, 1, i)
    plt.plot(time, y, color=colores[i-1])
    plt.title(f"Forma de onda - Micrófono {i}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
plt.tight_layout()
plt.show()

# Normalizar audios a una misma longitud
min_length = min(len(y) for y, _ in audios[:-1])
señales = np.vstack([y[:min_length] for y, _ in audios[:-1]]).T  

# Transformada de Fourier
def mostrar_espectro(y, sr, titulo, max_freq=20000):
    
    Y = np.fft.fft(y)
    Y_magnitude = np.abs(Y)[:len(Y)//2]
    freqs = np.fft.fftfreq(len(Y), 1/sr)[:len(Y)//2]
    
    plt.figure(figsize=(14, 5))
    plt.plot(freqs, Y_magnitude,color=colores[i-1] )
    plt.title(f"Espectro de Frecuencia - {titulo}")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True)
    plt.show()

for i, (y, sr) in enumerate(audios[:-1], start=1):
    mostrar_espectro(y, sr, f"Micrófono {i}")
    
# Beamforming
def beamforming(señales, delay):
    num_micrófonos = señales.shape[1]
    señal_beamformed = np.zeros(len(señales))
    
    for i in range(num_micrófonos):
        señal_beamformed += np.roll(señales[:, i], delay[i])
    
    return señal_beamformed / num_micrófonos


velocidad_sonido = 343  # Velocidad del sonido m/s
distancia_mic = [0, 0.8, 1.6]  # Distancias en metros de los micrófonos
distancia_fonte = 0.8  
delay = [int(d / velocidad_sonido * audios[0][1]) for d in distancia_mic]

#Beamforming
señal_beamformed = beamforming(señales, delay)

# Señal beamformed
plt.figure(figsize=(14, 5))
plt.plot(señal_beamformed, color='#ec5c78' )
plt.title("Señal Beamformed")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Guardar la señal beamformed
sf.write('Voz_filtrada.mp3', señal_beamformed, audios[0][1])

# Calcular SNR 
ruido_ambiente, sr_ambiente = librosa.load("ambiente audio.mp3", sr=None)

def calcular_snr(señal, ruido):
    potencia_senal = np.mean(señal**2)
    potencia_ruido = np.mean(ruido**2)
    snr = 10 * np.log10(potencia_senal / potencia_ruido)
    return snr

snrs = [calcular_snr(y, ruido_ambiente) for y, _ in audios[:-1]]

for i, snr in enumerate(snrs, start=1):
    print(f"SNR Micrófono {i}: {snr:.2f} dB")
    
#SNR Ruido y señal Beamformed
potencia_senal_beamformed = np.mean(señal_beamformed**2)

ruido_combinado = np.mean(señales, axis=1)
potencia_ruido_combinado = np.mean(ruido_combinado**2)
snr_beamformed_vs_originales = 10 * np.log10(potencia_senal_beamformed / potencia_ruido_combinado)
print(f"SNR Señal Beamformed-Señales Originales: {snr_beamformed_vs_originales:.2f} dB")

