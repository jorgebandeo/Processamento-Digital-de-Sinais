import numpy as np
import matplotlib.pyplot as plt

# Sinal de exemplo
n = np.arange(0, 10)
x = np.sin(2 * np.pi * 0.1 * n)

# Reversão no tempo
x_reverso = x[::-1]

plt.figure()
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(n, x_reverso, linefmt='r-', markerfmt='ro', basefmt='k-', label='Reverso no Tempo')
plt.title('Reversão no Tempo')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
