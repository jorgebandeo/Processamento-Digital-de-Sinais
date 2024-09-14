import numpy as np
import matplotlib.pyplot as plt

# Sinal de exemplo
n = np.arange(-10, 11)
sinal = np.where(n >= 0, 1, 0)


# Definindo o filtro de média (kernel) de tamanho k
k = 4  # Tamanho da janela de média
kernel = np.ones(k) / k  # Filtro de média móvel

# Calculando a média móvel usando convolução
media_movel = np.convolve(sinal, kernel, mode='valid')

# Plotando o sinal original e a média móvel
plt.figure()
plt.stem( sinal[:len(media_movel)], label='Sinal Original')
plt.stem(np.arange(len(media_movel)), media_movel, label='Média Móvel (Convolução)', linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('Média Móvel usando Convolução')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
# Define os intervalos do eixo Y de 0.5 em 0.5
plt.yticks(np.arange(0, 1, 0.05))
plt.legend()
plt.grid(True)
plt.show()
