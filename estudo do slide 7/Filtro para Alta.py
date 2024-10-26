from scipy.signal import bilinear, tf2zpk, freqz
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do filtro
fc = 1000           # Frequência de corte em Hz
fs = 8000           # Frequência de amostragem em Hz
wc = 2 * np.pi * fc # Frequência angular de corte em rad/s

# Coeficientes analógicos do filtro passa-alta
b_analog = [1, 0]   # Numerador de H(s) = s / (s + wc)
a_analog = [1, wc]  # Denominador de H(s) = s / (s + wc)

# Transformação bilinear para obter H(z)
b_digital, a_digital = bilinear(b_analog, a_analog, fs)

# Calculando os pólos e zeros
zeros, poles, _ = tf2zpk(b_digital, a_digital)

# Exibindo os coeficientes e os pólos/zeros
print("Coeficientes do filtro passa-alta digital H(z):")
print("Numerador (b):", b_digital)
print("Denominador (a):", a_digital)
print("\nZeros:", zeros)
print("Pólos:", poles)

# Plotagem dos Pólos e Zeros no plano z
plt.figure(figsize=(6, 6))
plt.plot(np.real(zeros), np.imag(zeros), 'o', label='Zeros')
plt.plot(np.real(poles), np.imag(poles), 'x', label='Pólos')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.title("Pólos e Zeros do Filtro Passa-Alta no Plano z")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.legend()
plt.grid()
plt.show()

# Resposta em Frequência do Filtro
w, h = freqz(b_digital, a_digital, worN=8000, fs=fs)
plt.figure(figsize=(10, 5))
plt.plot(w, 20 * np.log10(abs(h)), label="Magnitude")
plt.title("Resposta em Frequência do Filtro Passa-Alta")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.legend()
plt.show()
