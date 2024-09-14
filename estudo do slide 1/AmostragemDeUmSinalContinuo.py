import numpy as np
import matplotlib.pyplot as plt

# Definindo os parâmetros
f_sinal = 100  # Frequência do sinal em Hz
fs = 8000  # Frequência de amostragem em Hz
t = np.arange(0, 1, 1/fs)  # Tempo de 1 segundo

# Gerando o sinal contínuo
sinal_continuo = np.sin(2 * np.pi * f_sinal * t)

# Plotando o sinal contínuo
plt.figure()
plt.stem(t, sinal_continuo)
plt.title(f'Sinal Contínuo: {f_sinal}Hz')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Amostragem do sinal em diferentes frequências
frequencias = [100, 200, 400, 1000, 2000]  # Frequências do sinal
plt.figure()

for f in frequencias:
    sinal_continuo = np.sin(2 * np.pi * f * t)
    plt.stem(t, sinal_continuo, label=f'{f}Hz')

plt.title('Sinais Contínuos com Diferentes Frequências')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Fixando a frequência do sinal e variando a frequência de amostragem
f_sinal = 400  # Frequência do sinal fixada em 400Hz
fs_variado = [2000, 4000, 8000, 16000]  # Diferentes frequências de amostragem
plt.figure()

for fs in fs_variado:
    t = np.arange(0, 1, 1/fs)
    sinal_continuo = np.sin(2 * np.pi * f_sinal * t)
    plt.stem(t, sinal_continuo, label=f'Fs = {fs}Hz')

plt.title('Sinal de 400Hz com Diferentes Frequências de Amostragem')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
