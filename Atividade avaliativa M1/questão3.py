import numpy as np
import matplotlib.pyplot as plt
def h(sinal, R):
    saida = np.zeros(len(sinal))
    for i in range(len(sinal)):
        if i == 0:
            saida[i] = sinal[i]
        else:
            saida[i] = sinal[i] - sinal[i-1] + R*saida[i-1]
    return saida

def gera_sinal_inpuso(ponto, janela):
    # Entrada de impulso unitário
    entrada = np.zeros(janela)
    entrada[ponto] = 1  # Impulso unitário
    return entrada

def gera_sinal_degrau(ponto, panto2, janela):
    # Gerando degrau unitário
    entrada = np.zeros(janela)
    for i in range(len(entrada)):
        if (i >= ponto and i <= panto2):
            entrada[i] = 1
        else:
            entrada[i] = 0

    return entrada
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

    R = 0.95

    S1 = gera_sinal_inpuso(0,10)
    Y1 = h(S1, R)
    
    S2 = gera_sinal_degrau(0,10,10)
    Y2 = h(S2, R)

    S3 = ler_pcm("Atividade avaliativa M1\Anexo_41743450.pcm", bit_depth=16)
    Y3 = h(S3, R)

    # Plotar o sinal lido
    plt.figure()
    #plt.plot(sinal_lido, label='Sinal Senoidal (Lido do PCM)')
    plt.stem(Y1, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
    plt.stem(S1, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')
    plt.title('Sinal Senoidal do Arquivo PCM')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.stem(S2, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')
    plt.stem(Y2, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
    plt.title('Sinal Senoidal do Arquivo PCM')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.stem(S3, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')
    plt.stem(Y3, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
    plt.title('Sinal Senoidal do Arquivo PCM')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.xlim(0,100)
    plt.legend()



    plt.show()