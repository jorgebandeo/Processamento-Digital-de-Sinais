import numpy as np
import matplotlib.pyplot as plt

# Parâmetros de Eco
Fs = 8000
D = int(1e-3 * Fs)  # 1 ms delay
a0, a1 = 1.0, 0.5

# Entrada de impulso unitário
entrada = np.zeros(20)
entrada[0] = 1  # Impulso unitário

# Saída com eco
saida_eco = np.zeros(len(entrada))

for i in range(len(entrada)):
    if i >= D:
        saida_eco[i] = entrada[i] + a1 * entrada[i - D]
    else:
        saida_eco[i] = entrada[i]

# Plotando o sinal original e o sinal com eco
plt.figure()
plt.stem(entrada, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(saida_eco, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')
plt.title('Sinal Original e Sinal com Eco')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
