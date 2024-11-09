from scipy.signal import bilinear, zpk2tf, tf2zpk
from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt



# Parâmetros do filtro passa-baixa analógico
fc = 1000  # Frequência de corte
fs = 8000  # Frequência de amostragem
wc = 2 * np.pi * fc

# Coeficientes analógicos do filtro passa-baixa de 1ª ordem
b_analog = [wc]
a_analog = [1, wc]

# Aplicando a transformação bilinear para obter o filtro digital
a_digital, b_digital = bilinear(b_analog, a_analog, fs)
# Exibindo os coeficientes e os pólos/zeros
print("Coeficientes do filtro passa-alta digital H(z):")
print("Numerador (b):", b_digital)
print("Denominador (a):", a_digital)

# Calculando a resposta em frequência
w, h = freqz(a_digital, b_digital, worN=8000)

f_hz = (w * fs) / (2 * np.pi)

# Plotando pólos e zeros
zeros, poles, _ = tf2zpk(b_digital, a_digital)
print("\nZeros:", zeros)
print("Pólos:", poles)
plt.figure()
plt.plot(np.real(zeros), np.imag(zeros), 'o', label='Zeros')
plt.plot(np.real(poles), np.imag(poles), 'x', label='Pólos')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.title('Pólos e Zeros do Filtro Passa-Baixa')
plt.xlabel('Real')
plt.ylabel('Imaginário')
plt.legend()
plt.grid()

# Plotando a resposta em frequência do filtro passa-baixa
plt.figure(figsize=(10, 4))
plt.plot(f_hz, 20 * np.log10(abs(h)), 'b')
plt.title('Resposta em Frequência do Filtro Passa-Baixa')
plt.xlabel('Frequência [rad/amostra]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.show()
