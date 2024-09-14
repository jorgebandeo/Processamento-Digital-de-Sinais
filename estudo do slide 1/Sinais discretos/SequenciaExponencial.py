import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
A = 1  # Amplitude
a_values = -0.5  # Diferentes valores de "a"
n = np.arange(0, 50, 1)

plt.figure()

exponencial = A * a_values ** n
plt.stem(n, exponencial, label=f'a = {a_values}')

plt.title('Sequência Exponencial')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()