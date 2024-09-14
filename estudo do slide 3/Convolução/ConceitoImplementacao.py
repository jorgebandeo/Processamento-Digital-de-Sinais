import numpy as np
import matplotlib.pyplot as plt

# Definindo as sequências x[k] e h[k]
x = [1, 1, 1, 1, 1, 1]
h = [1, 0.5, 0.25, 0.125]

# Calculando a convolução
y = np.convolve(x, h)

# Plotando o resultado da convolução
plt.figure()
n = np.arange(0, len(y))
plt.stem(n, y)
plt.title('Convolução de x e h')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
