import numpy as np
import matplotlib.pyplot as plt
def gera_sinal_inpuso(ponto, janela):
    # Entrada de impulso unitário
    entrada = np.zeros(janela)
    entrada[ponto] = 1  # Impulso unitário
    return entrada


h = [0.1, 0.2, 0.4, 0.2,0.1]

# Numero A
x1 = [1,1]
y1 = np.convolve( h,x1)
N1 = np.arange(-2, len(y1)-2)  # Passo padrão é 1, então vai gerar: [-2, -1, 0, 1, 2]

# Numero B
x2 = gera_sinal_inpuso(2,10)
y2 = np.convolve( h,x2)
N2 = np.arange(0, len(y2))  # Passo padrão é 1, então vai gerar: [-2, -1, 0, 1, 2]

# Plotando o resultado da convolução
plt.figure()

plt.stem(N1, y1)
plt.title('Convolução Letra A')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.figure()
plt.stem(N2, y2)
plt.title('Convolução Letra B')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
