import numpy as np
import matplotlib.pyplot as plt
# Gerando impulso unitário
n = np.arange(0, 11)
impulso = np.where(n == 5, 1, 0)
# Definindo as sequências x[k] e h[k]
x = impulso
h = [0.1, 0.2, 0.4, 0.2,0.1]

# Calculando a convolução
y = np.convolve( h,x)

# Plotando o resultado da convolução
plt.figure()
n = np.arange(0, len(y))
plt.stem(n, y)
plt.title('Convolução de x e h')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
