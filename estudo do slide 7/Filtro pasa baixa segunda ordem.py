import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
from scipy.signal import tf2zpk

# y(z)      b_o + b_1 * Z^-1 + b_2 * Z^-2
#------  = -------------------------------
# x(z)      1 + a_1 * z^-1 + a_2 * z^-2

# Fc = 1000
# Fs = 8000

# K = tg ( (pi() * Fc) / Fs) 

# b_o = K^2/(1+raiz(2)*K +K^2)

# b_1 = 2 * b_o 

# b_2 = b_o

# a_1 = (2 * (K^2 - 1)) / (1 + raiz(2) * K + K^2)

# a_2 = (1 - raiz(2) * K + K^2) / (1 + raiz(2) * K + K^2)



# Definindo as constantes do filtro
Fc = 1000  # Frequência de corte em Hz
Fs = 8000  # Frequência de amostragem em Hz

# Calculando K
K = np.tan((np.pi * Fc) / Fs)

# Coeficientes do filtro
b0 = K**2 / (1 + np.sqrt(2) * K + K**2)
b1 = 2 * b0
b2 = b0
a1 = (2 * (K**2 - 1)) / (1 + np.sqrt(2) * K + K**2)
a2 = (1 - np.sqrt(2) * K + K**2) / (1 + np.sqrt(2) * K + K**2)

# Arrays de coeficientes para o filtro
b = [b0, b1, b2]
a = [1, a1, a2]

# Calculando a resposta em frequência
w, h = freqz(b, a, fs=Fs)

# Convertendo a resposta em dB
h_db = 20 * np.log10(abs(h))
print(b0)
print(b1)
print(b2)
print(a1)
print(a2)


# Plotando a resposta em frequência
plt.plot(w, h_db)
plt.title("Filtro Passa-Baixa de Segunda Ordem")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.show()

# Calculando polos e zeros
zeros, poles, _ = tf2zpk(b, a)

# Plotando o círculo unitário, polos e zeros
plt.figure(figsize=(6, 6))
plt.plot(np.cos(np.linspace(0, 2 * np.pi, 100)), np.sin(np.linspace(0, 2 * np.pi, 100)), 'k--')  # Círculo unitário
plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Zeros', marker='o', s=100)
plt.scatter(np.real(poles), np.imag(poles), color='red', label='Polos', marker='x', s=100)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.title("Diagrama de Polos e Zeros")
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()
