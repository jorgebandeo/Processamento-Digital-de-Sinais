import numpy as np
import matplotlib.pyplot as plt

def gerar_sinal_senoidal(frequencia_sinal, duracao, pontos=1000):
    """
    Gera um sinal senoidal contínuo.

    :param frequencia_sinal: Frequência do sinal em Hz
    :param duracao: Duração do sinal em segundos
    :param pontos: Número de pontos para gerar o sinal contínuo
    :return: Vetor de tempo e vetor do sinal contínuo
    """
    t_cont = np.linspace(0, duracao, pontos, endpoint=False)
    sinal_continuo = np.sin(2 * np.pi * frequencia_sinal * t_cont)
    return t_cont, sinal_continuo

def amostrar_sinal(sinal_continuo, frequencia_amostragem, duracao):
    """
    Amostra um sinal contínuo.

    :param sinal_continuo: O sinal contínuo a ser amostrado
    :param frequencia_amostragem: Frequência de amostragem em Hz
    :param duracao: Duração do sinal em segundos
    :return: Vetor de tempo amostrado e vetor do sinal amostrado
    """
    intervalo_amostragem = 1 / frequencia_amostragem
    n = np.arange(0, int(frequencia_amostragem * duracao))
    t_amostrado = n * intervalo_amostragem
    sinal_amostrado = np.interp(t_amostrado, np.linspace(0, duracao, len(sinal_continuo)), sinal_continuo)
    return t_amostrado, sinal_amostrado

# Parâmetros do sinal
frequencia_sinal = 5  # Frequência do sinal em Hz
frequencia_amostragem = 100 # Frequência de amostragem em Hz
duracao = 1  # Duração do sinal em segundos

# Geração do sinal contínuo
t_cont, sinal_continuo = gerar_sinal_senoidal(frequencia_sinal, duracao)

# Amostragem do sinal
t_amostrado, sinal_amostrado = amostrar_sinal(sinal_continuo, frequencia_amostragem, duracao)

# Plotagem dos sinais
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t_cont, sinal_continuo)
plt.title('Sinal Contínuo')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
markers, stemlines, baseline = plt.stem(t_amostrado, sinal_amostrado, basefmt=" ", linefmt='-', markerfmt='o')
plt.setp(markers, markersize=5, color='b')  # Ajuste o tamanho e a cor dos marcadores
plt.title('Sinal Amostrado')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
