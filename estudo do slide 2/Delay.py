import numpy as np
import matplotlib.pyplot as plt

# Parâmetros de Delay
Fs = 8000
n1 = int(1e-3 * Fs)  
n2 = int(1.5e-3 * Fs) 
a0, a1, a2 = 0.5, 0.3, 0.2

# Sinal de entrada (Impulso Unitário)
entrada = np.zeros(20)
entrada[0] = 1  # Impulso no início

# Saída com atraso
saida = np.zeros(len(entrada))
vetor_delay = np.zeros(200)  # Tamanho do vetor de delay deve ser o maior atraso

for j in range(len(entrada)):
    
    y = a0 * entrada[j]
    if n1 <= j:  # Verifica se o índice n1 está dentro dos limites
        y += a1 * entrada[j - n1]
    if n2 <= j:  # Verifica se o índice n2 está dentro dos limites
        y += a2 * entrada[j - n2]
    
    saida[j] = y
    y = 0

# Plotando o sinal original e o sinal com delay
plt.figure()
plt.stem(entrada, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(saida, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Delay')
plt.title('Sinal Original e Sinal com Delay')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
# Define os intervalos do eixo Y de 0.5 em 0.5
plt.yticks(np.arange(0, 1, 0.05))
plt.legend()
plt.grid(True)
plt.show()
