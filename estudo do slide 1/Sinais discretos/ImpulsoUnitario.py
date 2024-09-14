import numpy as np
import matplotlib.pyplot as plt

# Gerando impulso unitário
n = np.arange(-10, 11)
impulso = np.where(n == 0, 1, 0)

# Plotando impulso unitário
plt.stem(n, impulso)
plt.title('Impulso Unitário')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
