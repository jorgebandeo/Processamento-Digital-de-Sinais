import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Definições iniciais para eco audível
Fs = 8000  # Taxa de amostragem em Hz
n1_audivel = int(0.5 * Fs)  # Atraso de 0.5 segundos
n2_audivel = int(0.75 * Fs) # Atraso de 0.75 segundos
a0 = 0.5
a1 = 0.3
a2 = 0.2

# Criar um sinal de entrada (ex: impulso unitário)
tamanho_entrada = 3 * Fs  # Duração do sinal de entrada (3 segundos)
entrada = np.zeros(tamanho_entrada)
entrada[0] = 1  # Definindo o impulso unitário

# Vetor de delay para eco perceptível
vetor_delay_audivel = np.zeros(n2_audivel + 1)  # Ajuste do tamanho do vetor de delay
saida_audivel = np.zeros_like(entrada)

# Processamento do eco audível
for j in range(len(entrada)):
    vetor_delay_audivel[0] = entrada[j]
    y_audivel = a0 * vetor_delay_audivel[0] + (a1 * vetor_delay_audivel[n1_audivel] if j >= n1_audivel else 0) + (a2 * vetor_delay_audivel[n2_audivel] if j >= n2_audivel else 0)
    
    # Atualização do vetor de delay
    vetor_delay_audivel[1:] = vetor_delay_audivel[:-1]
    saida_audivel[j] = y_audivel

# Salvar o sinal como arquivo WAV para ouvir o eco
write('eco_perceptivel.wav', Fs, saida_audivel.astype(np.float32))
print('Arquivo de áudio salvo como "eco_perceptivel.wav".')

# Plotando o resultado para visualização
plt.stem(saida_audivel)
plt.title('Resposta ao Impulso com Eco Perceptível')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()
