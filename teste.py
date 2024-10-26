import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Função para calcular a resposta em frequência
def plot_frequency_response(num, den, title):
    w, h = signal.freqz(num, den)
    plt.figure()
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title(f'Resposta em Frequência - {title}')
    plt.xlabel('Frequência Normalizada [radians / sample]')
    plt.ylabel('Magnitude [dB]')
    plt.grid()
    plt.show()

# Função de Transferência 1
num1 = [3, -3.6]
den1 = [1, -1.4, 0.45]
plot_frequency_response(num1, den1, 'Função de Transferência 1')

# Função de Transferência 2
num2 = [1, 0]  # z^1 + 0
den2 = [1, -2.1, 1.08]  # (z - 0.9)(z - 1.2)
plot_frequency_response(num2, den2, 'Função de Transferência 2')

# Função de Transferência 3
num3 = [1, 0.9]  # z + 0.9
den3 = [1, 1, 0.41]  # z^2 + z + 0.41
plot_frequency_response(num3, den3, 'Função de Transferência 3')
