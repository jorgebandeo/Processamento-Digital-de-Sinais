import numpy as np
import matplotlib.pyplot as plt

def gerar_sinal_senoidal(frequencia, duracao, Fs):
    """
    Gera um sinal senoidal.

    Parâmetros:
    - frequencia: frequência da onda senoidal (Hz)
    - duracao: duração do sinal (segundos)
    - Fs: frequência de amostragem (Hz)

    Retorna:
    - n: vetor de tempo
    - x: sinal senoidal
    """
    n = np.arange(0, duracao, 1/Fs)  # Vetor de tempo
    x = np.sin(2 * np.pi * frequencia * n)  # Sinal senoidal
    return n, x

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

if __name__ == '__main__':
    # Gerar sinal senoidal
    frequencia = 440  # Frequência de 440 Hz (nota A)
    duracao = 2  # Duração de 2 segundos
    Fs = 8000  # Frequência de amostragem de 8 kHz
    n, x = gerar_sinal_senoidal(frequencia, duracao, Fs)

    # Salvar sinal como PCM
    nome_arquivo_pcm = 'sinal_senoidal.pcm'
    salvar_pcm(nome_arquivo_pcm, x)

    # Ler o arquivo PCM salvo
    sinal_lido = ler_pcm(nome_arquivo_pcm, bit_depth=16)

    # Plotar o sinal lido
    plt.figure()
    plt.plot(sinal_lido, label='Sinal Senoidal (Lido do PCM)')
    plt.title('Sinal Senoidal do Arquivo PCM')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.show()
