import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk
import os

# Função para calcular a resposta em frequência
def frequency_response(filter_size, fs=8000):
    kernel = np.ones(filter_size) / filter_size
    w, h = freqz(kernel, worN=8000, fs=fs)
    return w, h  # w já em Hz

# Função para calcular polos e zeros
def poles_and_zeros(filter_size):
    kernel = np.ones(filter_size) / filter_size
    z, p, _ = tf2zpk(kernel, [1])  # FIR tem denominador constante
    return z, p

# Função para aplicar o filtro média móvel
def moving_average_filter(signal, filter_size):
    kernel = np.ones(filter_size) / filter_size
    return np.convolve(signal, kernel, mode='same')

# Função para calcular atenuação em dB com tratamento para magnitude zero
def attenuation_in_db(h, w, freq, fs=8000):
    freq_index = np.argmin(np.abs(w - freq))
    magnitude = np.abs(h[freq_index])
    if magnitude > 0:
        return 20 * np.log10(magnitude)
    else:
        return -np.inf  # Retorna -∞ para magnitude zero

# Função para ler arquivo PCM
def ler_pcm(caminho_arquivo, bit_depth=16):
    try:
        with open(caminho_arquivo, 'rb') as f:
            raw_data = f.read()
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado. Usando sinal de exemplo.")
        return np.sin(2 * np.pi * 100 * np.arange(0, 1, 1 / 8000))  # Sinal senoidal de exemplo

    if bit_depth == 16:
        audio_data = np.frombuffer(raw_data, dtype=np.int16)
    elif bit_depth == 32:
        audio_data = np.frombuffer(raw_data, dtype=np.int32)
    else:
        raise ValueError("Bit depth não suportado")

    return audio_data

# Função para salvar arquivo PCM
def save_pcm(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data.astype(np.int16).tobytes())

# Função para criar pastas, se necessário
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Configurações iniciais
input_file = "MM/Sin_spike.pcm"  # Arquivo de entrada
filter_sizes = [9,10,11]  # Tamanhos diferentes de filtros
frequencies = [100, 1000]  # Frequências para análise (Hz)
fs = 8000  # Taxa de amostragem

# Criar pastas para gráficos
base_folder = "MM/Resultados"
folders = {
    "entrada_saida": os.path.join(base_folder, "Entrada_Saida"),
    "resposta_frequencia": os.path.join(base_folder, "Resposta_Frequencia"),
    "polos_zeros": os.path.join(base_folder, "Polos_Zeros")
}
for folder in folders.values():
    create_folder(folder)

# Carregar o sinal de entrada
input_signal = ler_pcm(input_file)

# Aplicar filtros e gerar gráficos
for size in filter_sizes:
    # Aplicar filtro
    output_signal = moving_average_filter(input_signal, size)
    save_pcm(f"MM/Sai_Sin_spike_{size}.pcm", output_signal)
    
    # Resposta em frequência
    w, h = frequency_response(size, fs)
    
    # Polos e zeros
    zeros, poles = poles_and_zeros(size)
    
    # Calcular atenuações
    attenuations = {freq: attenuation_in_db(h, w, freq, fs) for freq in frequencies}
    print(f"Filtro {size} Coeficientes:")
    for freq, att in attenuations.items():
        print(f"  Atenuação em {freq}Hz: {att:.2f} dB")

    # 1. Gráfico do sinal de entrada e saída
    plt.figure(figsize=(10, 6))
    plt.plot(input_signal, label="Entrada", alpha=0.7)
    plt.plot(output_signal, label=f"Saída", alpha=0.7)
    plt.title(f"Sinal de Entrada e Saída (Filtro {size})")
    plt.xlabel("Amostras")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(folders["entrada_saida"], f"Entrada_Saida_Filtro_{size}.png"))
    plt.close()
    
    # 2. Gráfico da resposta em frequência
    plt.figure(figsize=(10, 6))
    plt.plot(w, 20 * np.log10(np.abs(h)), label="Resposta em Frequência")
    for freq, att in attenuations.items():
        idx = np.argmin(np.abs(w - freq))
        plt.annotate(f"{att:.2f} dB", xy=(w[idx], 20 * np.log10(np.abs(h[idx]))),
                     xytext=(w[idx] + 200, 20 * np.log10(np.abs(h[idx])) - 10),
                     arrowprops=dict(facecolor='red', arrowstyle="->"))
    plt.title(f"Resposta em Frequência (Filtro {size})")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(folders["resposta_frequencia"], f"Resposta_Frequencia_Filtro_{size}.png"))
    plt.close()
    
    # 3. Gráfico de polos e zeros
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(zeros), np.imag(zeros), label="Zeros", color='blue')
    plt.scatter(np.real(poles), np.imag(poles), label="Polos", color='red')
    plt.title(f"Polos e Zeros (Filtro {size})")
    plt.xlabel("Parte Real")
    plt.ylabel("Parte Imaginária")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(folders["polos_zeros"], f"Polos_Zeros_Filtro_{size}.png"))
    plt.close()
