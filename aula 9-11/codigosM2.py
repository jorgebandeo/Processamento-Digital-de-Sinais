from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
from scipy.fft import fft, fftfreq



def janelalamento(cof, fc, M = 0):
    i2 = np.arange(0, M+1, 1)
    #print(i2)
    h2 = np.zeros(int(M+1))
    for ind in range(int(M+1)):
        if (ind-M/2) == 0:
            h2[ind] = 2*np.pi*fc
        else:
            h2[ind] = np.sin(2*np.pi*fc*(ind-M/2))/(ind-M/2)

        h2[ind] = h2[ind] * (0.54 - 0.46*np.cos(2*np.pi*ind/M)) # Filtro sinc * janela

    # normalize
    h2 = h2 / np.sum(h2)



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

def aplica_filtro_passa_rexectfaixa(signal, Fb=30,Fc=200, Fs=8000, M = 0):
    """
    Aplica um filtro passa-faixa de segunda ordem a um sinal de entrada.
    
    Parâmetros:
    signal : array-like
        Sinal de entrada a ser filtrado.
    Fb : float, opcional
        Frequência de corte central do filtro em Hz. Padrão é 1000 Hz.
    Fs : float, opcional
        Frequência de amostragem em Hz. Padrão é 8000 Hz.
        
    Retorna:
    filtered_signal : array-like
        Sinal de saída filtrado.
    """
    # Calculando C e D
    C = (np.tan((np.pi * Fb) / Fs) - 1) / (np.tan((2 * np.pi * Fb) / Fs) + 1)
    D = - np.cos((2 * np.pi * Fc) / Fs)

    # Coeficientes do filtro
    b0 = (1 / 2) * (1 - C)
    b1 = D*(1-C)
    b2 = (1 / 2) * (1 - C)
    a1 = D * (1 - C)
    a2 = -C

    # Arrays de coeficientes para o filtro
    b = [b0, b1, b2]
    a = [1, a1, a2]
   # Calculando a resposta em frequência
    w, h = freqz(b, a, fs=Fs)

    # Convertendo a resposta em dB
    h_db = 20 * np.log10(abs(h))

    # Plotando a resposta em frequência
    plt.plot(w, h_db)
    plt.title("Filtro Passa-Baixa de Segunda Ordem")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()
    plt.show()
    # Aplicando o filtro ao sinal
    filtered_signal = lfilter(b, a, signal)


 

    return filtered_signal
def aplica_filtro_passa_faixa(signal, Fb=30,Fc=200, Fs=8000, M = 0):
    """
    Aplica um filtro passa-faixa de segunda ordem a um sinal de entrada.
    
    Parâmetros:
    signal : array-like
        Sinal de entrada a ser filtrado.
    Fb : float, opcional
        Frequência de corte central do filtro em Hz. Padrão é 1000 Hz.
    Fs : float, opcional
        Frequência de amostragem em Hz. Padrão é 8000 Hz.
        
    Retorna:
    filtered_signal : array-like
        Sinal de saída filtrado.
    """
    # Calculando C e D
    C = (np.tan((np.pi * Fb) / Fs) - 1) / (np.tan((2 * np.pi * Fb) / Fs) + 1)
    D = - np.cos((2 * np.pi * Fc) / Fs)

    # Coeficientes do filtro
    b0 = (1 / 2) * (1 + C)
    b1 = 0
    b2 = (1 / 2) * ( - C-1)
    a1 = D * (1 - C)
    a2 = -C

    # Arrays de coeficientes para o filtro
    b = [b0, b1, b2]
    a = [1, a1, a2]
   # Calculando a resposta em frequência
    w, h = freqz(b, a, fs=Fs)

    # Convertendo a resposta em dB
    h_db = 20 * np.log10(abs(h))

    # Plotando a resposta em frequência
    plt.plot(w, h_db)
    plt.title("Filtro Passa-Baixa de Segunda Ordem")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid()
    plt.show()
    # Aplicando o filtro ao sinal
    filtered_signal = lfilter(b, a, signal)


 

    return filtered_signal
# Função que aplica o filtro passa-baixa de segunda ordem a um sinal de entrada
def aplica_filtro_passa_baixa(signal, Fc=1000, Fs=8000, M = 0 ):
    """
    Aplica um filtro passa-baixa de segunda ordem a um sinal de entrada.
    
    Parâmetros:
    signal : array-like
        Sinal de entrada a ser filtrado.
    Fc : float, opcional
        Frequência de corte do filtro em Hz. Padrão é 1000 Hz.
    Fs : float, opcional
        Frequência de amostragem em Hz. Padrão é 8000 Hz.
        
    Retorna:
    filtered_signal : array-like
        Sinal de saída filtrado.
    """
    # Calculando K
    K = np.tan((np.pi * Fc) / Fs)

    # Coeficientes do filtro
    b0 = K**2 / (1 + np.sqrt(2) * K + K**2)
    b1 = 2 * b0
    b2 = b0
    a1 = (2 * (K**2 - 1)) / (1 + np.sqrt(2) * K + K**2)
    a2 = (1 - np.sqrt(2) * K + K**2) / (1 + np.sqrt(2) * K + K**2)

    # Arrays de coeficientes para o filtro
    b = janelalamento([b0, b1, b2], Fc, M)
    a = janelalamento([1, a1, a2], Fc, M)

    print("a : " + a )
    print("b : " + b )

    # Aplicando o filtro ao sinal
    filtered_signal = lfilter(b, a, signal)
    #return filtered_signal

def aplica_filtro_passa_alta(signal, Fc=1000, Fs=8000, M = 0):
    #           b_0 + b_1 * z^-1 + b_2 * z^-2
    # H(z) = -----------------------------------------
    #           1 + a_1 * z^-1 + a_2 * z^-2 

    # K = arctag ( (pi() * Fc) / Fs) 

    # b_0 =1/(1+raiz(2)*K +K^2)

    # b_1 = 2/(1+raiz(2)*K +K^2)

    # b_2 = b_0 

    # a_1 = (2 * (K^2 - 1)) / (1 + raiz(2) * K + K^2)

    # a_2 = (1 - raiz(2) * K + K^2) / (1 + raiz(2) * K + K^2)

    # Calculando K
    K = np.arctan((np.pi * Fc) / Fs)

    # Coeficientes do filtro
    b0 = 1 / (1 + np.sqrt(2) * K + K**2)
    b1 = - 2 / (1 + np.sqrt(2) * K + K**2)
    b2 = b0
    a1 = (2 * (K**2 - 1)) / (1 + np.sqrt(2) * K + K**2)
    a2 = (1 - np.sqrt(2) * K + K**2) / (1 + np.sqrt(2) * K + K**2)

    # Arrays de coeficientes para o filtro
    b = [b0, b1, b2]
    a = [1, a1, a2]


    
    # Aplicando o filtro ao sinal
    filtered_signal = lfilter(b, a, signal)
    return filtered_signal

Fs = 8000

# Definindo a frequencia de corte
# tem que estar entre 0 e 0.5
Fc_Hz =  1000
Fc = Fc_Hz/Fs # fc normalizada

# definindo o roll-off
# BW é a largura em samples da banda de transição
# Tem que estar em 0 e 0.5
BW_Hz = 500
BW = BW_Hz/Fs # BW normalizada
M = 4 / BW # Número de coefs do filter



Fb=300

# Exemplo de uso
file_path = '../aula 9-11/sweep_20_2k.pcm.pcm'
sweep =0#= read_pcm(file_path, num_channels=1, sample_rate=8000, bit_depth=16)
# Testando a função com o sinal sweep
sweep_filtered = aplica_filtro_passa_baixa(sweep,Fc,Fs, M)
t = np.arange(len(sweep))




# Calculando a Transformada de Fourier dos sinais de entrada (sweep) e saída (sweep_filtered)
sweep_fft = fft(sweep)
sweep_filtered_fft = fft(sweep_filtered)

# Frequências correspondentes
frequencies = fftfreq(len(t), 1/Fs)

# Calculando a Transformada de Fourier dos sinais de entrada (sweep) e saída (sweep_filtered) para obter a resposta em frequência
sweep_fft = fft(sweep)
sweep_filtered_fft = fft(sweep_filtered)





# Ajustando o espaçamento entre os subgráficos para melhorar a visualização
plt.figure(figsize=(14, 12))

# Sinais no domínio do tempo
plt.subplot(3, 1, 1)
plt.plot(t, sweep, label="Sinal Sweep Original")
plt.plot(t, sweep_filtered, label="Sinal Sweep Filtrado", color="orange", alpha=0.7)
plt.title("Sinal Sweep Original e Filtrado no Domínio do Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Espectro de frequência (magnitude)
plt.subplot(3, 1, 2)
plt.plot(frequencies[:len(frequencies)//2], np.abs(sweep_fft[:len(sweep_fft)//2]), label="Sinal Sweep Original", alpha=0.7)
plt.plot(frequencies[:len(frequencies)//2], np.abs(sweep_filtered_fft[:len(sweep_filtered_fft)//2]), label="Sinal Sweep Filtrado", alpha=0.7)
plt.title("Espectro de Frequência - Magnitude dos Sinais Original e Filtrado")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()

# Resposta em frequência em dB
plt.subplot(3, 1, 3)
plt.plot(frequencies[:len(frequencies)//2], 20 * np.log10(np.abs(sweep_fft[:len(sweep_fft)//2])), label="Sinal Sweep Original", alpha=0.7)
plt.plot(frequencies[:len(frequencies)//2], 20 * np.log10(np.abs(sweep_filtered_fft[:len(sweep_filtered_fft)//2])), label="Sinal Sweep Filtrado", alpha=0.7)
plt.title("Resposta em Frequência - Magnitude em dB dos Sinais Original e Filtrado")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.grid()

# Aumentando o espaçamento entre os subgráficos
plt.tight_layout(pad=3.0)
plt.show()
