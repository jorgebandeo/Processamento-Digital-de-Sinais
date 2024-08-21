import numpy as np 
import matplotlib.pyplot as plt
def read_pcm(file_path, num_channels=1, sample_rate=44100, bit_depth=16):
    # Calculando o número de bytes por amostra
    bytes_per_sample = bit_depth // 8

    # Abrindo o arquivo .pcm
    with open(file_path, 'rb') as f:
        # Lendo os dados brutos do arquivo
        raw_data = f.read()

    # Convertendo os dados brutos em um vetor numpy
    if bit_depth == 16:
        # Para 16 bits, usamos 'int16'
        audio_data = np.frombuffer(raw_data, dtype=np.int16)
    elif bit_depth == 32:
        # Para 32 bits, usamos 'int32'
        audio_data = np.frombuffer(raw_data, dtype=np.int32)
    else:
        raise ValueError("Bit depth não suportado")

    

    return audio_data

def optenção_de_inpulso( x):
    y = np.array([])
    aux = 0
    for n in x:
        y = np.append(y, n-aux)
        aux = n
    return  y

def media_movel( x, k):
    y = np.array([])
    mem = np.zeros(k)
    for n in x:
        mem = np.roll(mem, 1)  # Desloca os elementos de mem para a direita
        mem[0] = n  # Coloca o novo valor na primeira posição
        y = np.append(y, np.mean(mem))
    return y
def generate_step(n0, window_time, Fs):
    N = int(Fs * window_time)  # Número total de amostras
    n = np.linspace(n0 - (window_time / 2), n0 + (window_time / 2), 100)  # Eixo de tempo simétrico em torno de zero
    x = np.zeros(100)
    x[n >= n0] = 1  # Degrau começa em n0
    return n, x    

if __name__ == '__main__':
    n, x = generate_step(1,2,8000)
    


    # Exemplo de uso
    file_path = 'sweep_20_2k.pcm'
    audio_vector = read_pcm(file_path, num_channels=1, sample_rate=8000, bit_depth=16)

    y = media_movel(audio_vector, 100)
    # Definindo o vetor n (índices das amostras)
    n = np.arange(len(audio_vector))

    # Plotando com cores personalizadas
    plt.stem(n, audio_vector, linefmt='r-', markerfmt='ro', basefmt='r-')  # Sinal x em vermelho
    plt.stem(n, y, linefmt='b-', markerfmt='bo', basefmt='b-')  # Sinal y em azul

    # Adicionando título e rótulos
    plt.title('Gráfico Stem de n vs x e n vs y')
    plt.xlabel('n')
    plt.ylabel('Valores')

    # Mostrando o gráfico
    plt.show()







