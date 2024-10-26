from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt

# Definindo a sequência
X_k = np.array([0.1, 0.2, 0.4, 0.2, 0.1])

# Calculando a resposta em frequência usando a Transformada Z
w, h = freqz(X_k, worN=8000)

# Plotando a magnitude e fase
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Magnitude da Resposta em Frequência')
plt.xlabel('Frequência [rad/amostra]')
plt.ylabel('Magnitude [dB]')

plt.subplot(1, 2, 2)
plt.plot(w, np.angle(h), 'r')
plt.title('Fase da Resposta em Frequência')
plt.xlabel('Frequência [rad/amostra]')
plt.ylabel('Fase [radianos]')
plt.show()
