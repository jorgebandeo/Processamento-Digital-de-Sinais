import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import os


def calculate_notch_coefficients(fs, f0, q):
    """
    Calcula os coeficientes de um filtro IIR rejeita-faixa.

    Parâmetros:
    - fs: Taxa de amostragem (Hz)
    - f0: Frequência central do notch (Hz)
    - q: Fator de qualidade

    Retorna:
    - Coeficientes (b, a): Numerador e denominador do filtro
    """
    omega = 2 * np.pi * f0 / fs  # Frequência angular
    alpha = np.sin(omega) / (2 * q)

    # Coeficientes do numerador
    b0 = 1
    b1 = -2 * np.cos(omega)
    b2 = 1

    # Coeficientes do denominador
    a0 = 1 + alpha
    a1 = -2 * np.cos(omega)
    a2 = 1 - alpha

    # Normalizar coeficientes
    b = [b0 / a0, b1 / a0, b2 / a0]
    a = [1, a1 / a0, a2 / a0]

    return b, a


def apply_filter(input_signal, b, a):
    """
    Aplica um filtro IIR a um sinal de entrada.

    Parâmetros:
    - input_signal: Sinal de entrada (array)
    - b: Coeficientes do numerador
    - a: Coeficientes do denominador

    Retorna:
    - Sinal filtrado
    """
    y = np.zeros_like(input_signal, dtype=float)
    for n in range(2, len(input_signal)):
        y[n] = (
            b[0] * input_signal[n]
            + b[1] * input_signal[n - 1]
            + b[2] * input_signal[n - 2]
            - a[1] * y[n - 1]
            - a[2] * y[n - 2]
        )
    return np.clip(y, -32768, 32767).astype(np.int16)


def ler_pcm(caminho_arquivo):
    """
    Lê um arquivo PCM e retorna os dados de áudio como numpy array.

    Parâmetros:
    - caminho_arquivo: Caminho do arquivo PCM.

    Retorna:
    - Array numpy com os dados do sinal.
    """
    with open(caminho_arquivo, "rb") as f:
        raw_data = f.read()
    return np.frombuffer(raw_data, dtype=np.int16)


def salvar_pcm(nome_arquivo, sinal):
    """
    Salva o sinal no formato PCM (16 bits).
    """
    with open(nome_arquivo, "wb") as f:
        f.write(sinal.tobytes())
    print(f'Sinal salvo como "{nome_arquivo}".')


def criar_pasta_resultados(pasta="Resultados"):
    """
    Cria uma pasta para salvar os resultados, se não existir.
    """
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    return pasta


def calcular_atenuacao(w, h, frequencias):
    """
    Calcula a atenuação em dB para frequências especificadas.

    Parâmetros:
    - w: Frequências calculadas por freqz.
    - h: Resposta em frequência calculada por freqz.
    - frequencias: Lista de frequências de interesse.

    Retorna:
    - Dicionário com frequências como chave e atenuações em dB como valor.
    """
    attenuations = {}
    for freq in frequencias:
        idx = np.argmin(np.abs(w - freq))
        magnitude = np.abs(h[idx])
        attenuations[freq] = 20 * np.log10(magnitude) if magnitude > 0 else -np.inf
    return attenuations


# Configurações do filtro
fs = 8000  # Taxa de amostragem (8 kHz)
f0 = 400   # Frequência central do notch (Hz)
q = 30     # Fator de qualidade
frequencies = [200, 1000]  # Frequências de interesse para análise

# Calcular coeficientes
b, a = calculate_notch_coefficients(fs, f0, q)

# Criar pasta para resultados
pasta_resultados = criar_pasta_resultados("IIR_Rejeita_Faixa/Reultados")

# Carregar sinal de entrada
caminho_arquivo = "IIR_Rejeita_Faixa/Q2_voz_ruido.pcm"
input_signal = ler_pcm(caminho_arquivo)

# Aplicar filtro
output_signal = apply_filter(input_signal, b, a)

# Salvar sinal filtrado
salvar_pcm(os.path.join(pasta_resultados, "Sai_M2_voz_ruido.pcm"), output_signal)

# Gráfico da resposta em frequência com marcadores
w, h = freqz(b, a, worN=8000, fs=fs)
attenuations = calcular_atenuacao(w, h, frequencies)
plt.figure(figsize=(10, 6))
plt.plot(w, 20 * np.log10(np.abs(h)), label="Resposta em Frequência")
for freq, att in attenuations.items():
    idx = np.argmin(np.abs(w - freq))
    plt.annotate(f"{att:.2f} dB", xy=(w[idx], 20 * np.log10(np.abs(h[idx]))),
                 xytext=(w[idx] + 200, 20 * np.log10(np.abs(h[idx])) - 10),
                 arrowprops=dict(facecolor='red', arrowstyle="->"))
plt.title("Resposta em Frequência do Filtro")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, "resposta_frequencia.png"))
plt.close()

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
poles = np.roots(a)
plt.figure(figsize=(6, 6))
plt.scatter(np.real(zeros), np.imag(zeros), label="Zeros", color="blue")
plt.scatter(np.real(poles), np.imag(poles), label="Polos", color="red")
# Círculo unitário
unit_circle = np.exp(1j * np.linspace(0, 2 * np.pi, 100))
plt.plot(np.real(unit_circle), np.imag(unit_circle), linestyle="--", color="black", label="Círculo Unitário")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.title("Polos e Zeros do Filtro")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, "polos_zeros.png"))
plt.close()

print(f"Gráficos e resultados salvos na pasta '{pasta_resultados}'.")
