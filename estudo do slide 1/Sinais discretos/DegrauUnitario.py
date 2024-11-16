import numpy as np
import matplotlib.pyplot as plt




def salvar_pcm(nome_arquivo, sinal):
    """
    Salva o sinal no formato PCM (16 bits).

    Parâmetros:
    - nome_arquivo: nome do arquivo para salvar o sinal (com extensão .pcm)
    - sinal: sinal a ser salvo (array numpy)
    """
    # Normalizar o sinal para o intervalo de -1 a 1
    sinal_normalizado = sinal / np.max(np.abs(sinal))
    
    # Converter para formato 16-bit PCM
    sinal_pcm = np.int16(sinal_normalizado * 32767)
    
    # Salvar em formato PCM
    with open(nome_arquivo, 'wb') as f:
        f.write(sinal_pcm.tobytes())
    print(f'Sinal salvo como "{nome_arquivo}".')

def ler_pcm(caminho_arquivo, bit_depth=16):
    """
    Lê um arquivo PCM e retorna os dados de áudio.

    Parâmetros:
    - caminho_arquivo: caminho do arquivo PCM a ser lido
    - bit_depth: profundidade de bits do sinal (16 ou 32)

    Retorna:
    - audio_data: vetor numpy contendo o sinal de áudio
    """
    # Abrir o arquivo PCM
    with open(caminho_arquivo, 'rb') as f:
        raw_data = f.read()

    # Converter os dados brutos para numpy array
    if bit_depth == 16:
        audio_data = np.frombuffer(raw_data, dtype=np.int16)
    elif bit_depth == 32:
        audio_data = np.frombuffer(raw_data, dtype=np.int32)
    else:
        raise ValueError("Bit depth não suportado")

    return audio_data




# Configuração
fs = 8000  # Taxa de amostragem (Hz)
duration = 60  # Duração do sinal em segundos
total_samples = fs * duration  # Número total de amostras

# Gerando o tempo discreto
n = np.arange(total_samples)  # Vetor de amostras
t = n / fs  # Vetor de tempo em segundos

# Criando o degrau unitário na metade do tempo
degrau = np.where(n >= total_samples // 2, 1, 0)

salvar_pcm("degrau_1_2.pcm",degrau)

# Plotando o degrau unitário
plt.figure(figsize=(10, 4))
plt.plot(t, degrau, label='Degrau Unitário', color='b')
plt.title('Degrau Unitário na Metade de 1 Minuto')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
