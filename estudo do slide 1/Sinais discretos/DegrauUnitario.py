import numpy as np
import matplotlib.pyplot as plt


# Gerando degrau unitário
n = np.arange(-10, 11)
degrau = np.where(n >= 0, 1, 0)

# Plotando degrau unitário
plt.stem(n, degrau)
plt.title('Degrau Unitário')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
