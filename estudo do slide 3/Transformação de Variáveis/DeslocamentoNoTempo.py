import numpy as np
import matplotlib.pyplot as plt

# Sinal de exemplo
n = np.arange(0, 10)
x = np.sin(2 * np.pi * 0.1 * n)
# Deslocamento no tempo - Atraso
atraso = 3
x_atrasado = np.roll(x, atraso)

plt.figure()
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(n, x_atrasado, linefmt='r-', markerfmt='ro', basefmt='k-', label='Atraso de 3 amostras')
plt.title('Deslocamento no Tempo - Atraso')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
