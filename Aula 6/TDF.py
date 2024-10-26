import numpy as np
import matplotlib.pyplot as plt

# Função para aplicar a Transformada de Fourier Discreta (DFT) ao sinal
def aplicar_dft(sinal):
    N = len(sinal)
    X = np.zeros(N, dtype=complex)  # Array para armazenar a DFT

    for k in range(N):
        soma = 0
        for n in range(N):
            angulo = -2j * np.pi * k * n / N
            soma += sinal[n] * np.exp(angulo)
        X[k] = soma
    
    return X

# Exemplo de uso
if __name__ == "__main__":
    # Parâmetros do sinal
    N = 100  # Número de amostras

    # Gerar um sinal de degrau unitário que começa em 1 e vai até 2
    sinal = np.zeros(N)
    sinal[N // 2:] = 1  # Degrau unitário começando na metade

    # Aplicar a Transformada de Fourier Discreta
    dft = aplicar_dft(sinal)

    # Gerar as frequências correspondentes
    frequencias = np.fft.fftfreq(N, d=1/N)

    # Magnitude e fase da DFT
    Mod_X = np.abs(dft)
    Fase_X = np.angle(dft)

    # Plotar o sinal original
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.stem(range(N), sinal)
    plt.title('Sinal de Degrau Unitário (1 a 2)')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plotar a magnitude da Transformada de Fourier Discreta
    plt.subplot(3, 1, 2)
    plt.plot(frequencias[:N // 2], Mod_X[:N // 2])
    plt.title('Magnitude da Transformada de Fourier Discreta (DFT)')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)

    # Plotar a fase da Transformada de Fourier Discreta
    plt.subplot(3, 1, 3)
    plt.plot(frequencias[:N // 2], Fase_X[:N // 2])
    plt.title('Fase da Transformada de Fourier Discreta (DFT)')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Fase (radianos)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
