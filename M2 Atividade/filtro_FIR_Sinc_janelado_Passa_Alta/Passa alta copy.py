import numpy as np
import matplotlib.pyplot as plt
import os


def calcular_coeficientes_fir(numtaps, fc, fs):
    """
    Calcula os coeficientes de um filtro FIR janelado.

    Parâmetros:
    - numtaps: Número de coeficientes do filtro
    - fc: Frequência de corte (Hz)
    - fs: Taxa de amostragem (Hz)

    Retorna:
    - Coeficientes do filtro FIR
    """
    norm_fc = fc / (fs / 2)  # Frequência normalizada
    center = numtaps // 2
    b = np.zeros(numtaps)

    for n in range(numtaps):
        if n == center:
            b[n] = 1.0 - 2.0 * norm_fc
        else:
            x = np.pi * (n - center)
            b[n] = -np.sin(2.0 * norm_fc * x) / x

        # Aplicação da janela de Hamming
        b[n] *= 0.54 - 0.46 * np.cos(2.0 * np.pi * n / (numtaps - 1))

    return b


def aplicar_filtro_fir(b, numtaps, input_signal):
    """
    Aplica um filtro FIR a um sinal de entrada.

    Parâmetros:
    - b: Coeficientes do filtro FIR
    - numtaps: Número de coeficientes do filtro
    - input_signal: Sinal de entrada

    Retorna:
    - Sinal filtrado
    """
    length = len(input_signal)
    output_signal = np.zeros(length)

    for n in range(length):
        y = 0.0
        for k in range(numtaps):
            if n - k >= 0:
                y += b[k] * input_signal[n - k]

        y = np.clip(y, -32768, 32767)
        output_signal[n] = y

    return output_signal


def salvar_pcm(nome_arquivo, sinal):
    """
    Salva o sinal no formato PCM (16 bits).
    """
    sinal_pcm = np.clip(sinal, -32768, 32767).astype(np.int16)
    with open(nome_arquivo, 'wb') as f:
        f.write(sinal_pcm.tobytes())
    print(f'Sinal salvo como "{nome_arquivo}".')


def ler_pcm(caminho_arquivo, bit_depth=16):
    """
    Lê um arquivo PCM e retorna os dados de áudio.

    Parâmetros:
    - caminho_arquivo: Caminho do arquivo PCM
    - bit_depth: Profundidade de bits do sinal (16 ou 32)

    Retorna:
    - Array numpy contendo o sinal
    """
    with open(caminho_arquivo, 'rb') as f:
        raw_data = f.read()
    if bit_depth == 16:
        return np.frombuffer(raw_data, dtype=np.int16)
    elif bit_depth == 32:
        return np.frombuffer(raw_data, dtype=np.int32)
    else:
        raise ValueError("Bit depth não suportado")


def criar_pasta_resultados(pasta="Resultados"):
    """
    Cria uma pasta para salvar os resultados, se não existir.
    """
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    return pasta


# Configurações do filtro
fs = 8000  # Taxa de amostragem
fc = 150   # Frequência de corte
numtaps = 301  # Número de coeficientes do filtro

# Calcular os coeficientes FIR
b = calcular_coeficientes_fir(numtaps, fc, fs)

# Criar pasta para salvar os resultados
pasta_resultados = criar_pasta_resultados("filtro_FIR_Sinc_janelado_Passa_Alta/Resultados")

# Salvar os coeficientes do filtro em um arquivo
with open(os.path.join(pasta_resultados, "coeficientes_fir.txt"), "w") as f:
    for coef in b:
        f.write(f"{coef}\n")
print("Coeficientes do filtro FIR salvos.")

# Resposta em frequência do filtro
w = np.linspace(0, fs / 2, 8000)
h = np.fft.fft(b, 8000)
h_db = 20 * np.log10(np.abs(h[:4000]))

frequencies = [100, 1000]  # Frequências de interesse
attenuations = {freq: 20 * np.log10(np.abs(h[np.argmin(np.abs(w - freq))]))
                for freq in frequencies}

plt.figure(figsize=(10, 6))
plt.plot(w[:4000], h_db, label="Resposta em Frequência")
for freq, att in attenuations.items():
    idx = np.argmin(np.abs(w - freq))
    plt.annotate(f"{att:.2f} dB", xy=(w[idx], h_db[idx]),
                 xytext=(w[idx] + 200, h_db[idx] - 10),
                 arrowprops=dict(facecolor='red', arrowstyle="->"))
plt.title("Resposta em Frequência do Filtro FIR")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, "resposta_frequencia_fir.png"))
plt.close()

# Processar sinal de entrada
caminho_arquivo = "filtro_FIR_Sinc_janelado_Passa_Alta/Q3_Voz_ruido.pcm"
input_signal = ler_pcm(caminho_arquivo)
output_signal = aplicar_filtro_fir(b, numtaps, input_signal)

# Salvar sinal filtrado
salvar_pcm(os.path.join(pasta_resultados, "Sai_Q3_voz_ruido.pcm"), output_signal)

# Gráfico de entrada e saída
tempo = np.linspace(0, len(input_signal) / fs, len(input_signal))
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(tempo, input_signal, label="Entrada", color="orange")
plt.title("Sinal de Entrada")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(tempo, output_signal, label="Saída", color="green")
plt.title("Sinal de Saída")
plt.grid()

plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, "sinais_entrada_saida.png"))
plt.close()

# Gráfico de polos e zeros
zeros = np.roots(b)
poles = []
plt.figure(figsize=(6, 6))
plt.scatter(np.real(zeros), np.imag(zeros), label="Zeros", color="blue")
plt.scatter(np.real(poles), np.imag(poles), label="Polos", color="red")
# Círculo unitário
unit_circle = np.exp(1j * np.linspace(0, 2 * np.pi, 100))
plt.plot(np.real(unit_circle), np.imag(unit_circle), linestyle="--", color="black", label="Círculo Unitário")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Polos e Zeros do Filtro FIR")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, "polos_zeros_fir.png"))
plt.close()

# Cálculo da atenuação (AT)
valor_pico_entrada = np.max(np.abs(input_signal))
valor_pico_saida = np.max(np.abs(output_signal))
atenuacao_db = 20 * np.log10(valor_pico_saida / valor_pico_entrada)
print(f"Atenuação (AT) em dB: {atenuacao_db:.2f} dB")

print(f"Gráficos e resultados salvos na pasta '{pasta_resultados}'.")



