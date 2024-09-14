import numpy as np
import matplotlib.pyplot as plt

def media_movel_manual(signal, k):
    """
    Calcula a média móvel de um sinal manualmente.
    
    Parâmetros:
    - signal: lista ou array de entrada do sinal
    - k: número de elementos para a média móvel

    Retorna:
    - Uma lista com os valores da média móvel calculada.
    """
    n = len(signal)
    media_movel = []

    # Calcula a média móvel para cada ponto do sinal
    for i in range(n - k + 1):
        media = np.sum(signal[i:i + k]) / k
        media_movel.append(media)
    
    return media_movel

# Exemplo de uso - degrau unitário
n = np.arange(-10, 11)
sinal = np.where(n >= 0, 1, 0)
k_values = 4  # Diferentes tamanhos de janela

plt.figure()

media = media_movel_manual(sinal, k_values)
plt.stem(media, label=f'k={k_values}')

plt.title('Média Móvel com Diferentes Tamanhos de Janela (Manual)')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
# Define os intervalos do eixo Y de 0.5 em 0.5
plt.yticks(np.arange(0, 1, 0.05))
plt.legend()
plt.grid(True)
plt.show()
