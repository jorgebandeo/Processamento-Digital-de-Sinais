from scipy.signal import bilinear, zpk2tf, tf2zpk
from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt



# Parâmetros do filtro passa-baixa analógico
fc = 100  # Frequência de corte
fs = 1000  # Frequência de amostragem
wc = 2 * np.pi * fc

# Coeficientes analógicos do filtro passa-baixa de 1ª ordem
b_analog = [wc]
a_analog = [1, wc]

# Aplicando a transformação bilinear para obter o filtro digital
b_digital, a_digital = bilinear(b_analog, a_analog, fs)

# Calculando a resposta em frequência
w, h = freqz(b_digital, a_digital, worN=8000)

# Plotando pólos e zeros
zeros, poles, _ = tf2zpk(b_digital, a_digital)
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
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Resposta em Frequência do Filtro Passa-Baixa')
plt.xlabel('Frequência [rad/amostra]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.show()
