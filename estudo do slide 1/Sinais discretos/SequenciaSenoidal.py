import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
f_senoidal = 100  # Frequência do sinal senoidal
fs = 8000  # Frequência de amostragem
t = np.arange(0, 0.01, 1/fs)  # Duração de 0.01 segundo

# Gerando sequência senoidal
sequencia_senoidal = np.sin(2 * np.pi * f_senoidal * t)

# Plotando sequência senoidal
plt.stem(t, sequencia_senoidal)
plt.title('Sequência Senoidal')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
