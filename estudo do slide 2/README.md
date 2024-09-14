
# Processamento Digital de Sinais (DSP) - Implementações e Algoritmos

Este repositório contém implementações de algoritmos em Python para conceitos de Processamento Digital de Sinais (DSP), incluindo algoritmos de média móvel, delay e eco.

## Conteúdo

1. **Propriedades de Sistemas Discretos**
   - Causalidade
   - Estabilidade
   - Linearidade
   - Invariância no Tempo
2. **Implementação de Algoritmos**
   - Média Móvel
   - Delay
   - Eco

### 1. Propriedades de Sistemas Discretos

Aqui discutimos as propriedades de sistemas discretos como causalidade, estabilidade, linearidade e invariância no tempo.

### 2. Implementação de Algoritmos

#### a) Média Móvel

A média móvel é usada para suavizar sinais, especialmente úteis em aplicações de filtragem de ruído.

```python
def media_movel_manual(signal, k):
    """
    Calcula a média móvel de um sinal manualmente.
    
    Parâmetros:
    - signal: lista ou array de entrada do sinal
    - k: número de elementos para a média móvel

    Retorna:
    - Uma lista com os valores da média móvel calculada.
    """
    n = len(signal)
    media_movel = []

    # Calcula a média móvel para cada ponto do sinal
    for i in range(n - k + 1):
        media = np.sum(signal[i:i + k]) / k
        media_movel.append(media)
    
    return media_movel

# Exemplo de uso
sinal = np.random.randn(100)  # Sinal aleatório
k_values = [4, 8, 16, 32]  # Diferentes tamanhos de janela

plt.figure()

for k in k_values:
    media = media_movel_manual(sinal, k)
    plt.plot(media, label=f'k={k}')

plt.title('Média Móvel com Diferentes Tamanhos de Janela (Manual)')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
```

#### b) Implementação do Delay

A implementação do delay aplica um atraso ao sinal original e combina o sinal original com sua versão atrasada para criar o efeito de delay.

```python
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros de Delay
Fs = 8000
n1 = 80  # 10 ms delay -> 80 amostras
n2 = 120  # 15 ms delay -> 120 amostras
a0, a1, a2 = 0.5, 0.3, 0.2

# Sinal de entrada (Impulso Unitário)
entrada = np.zeros(200)
entrada[0] = 1  # Impulso no início

# Saída com atraso
saida = np.zeros(len(entrada))

for j in range(len(entrada)):
    y = a0 * entrada[j]
    if n1 <= j:  # Verifica se o índice n1 está dentro dos limites
        y += a1 * entrada[j - n1]
    if n2 <= j:  # Verifica se o índice n2 está dentro dos limites
        y += a2 * entrada[j - n2]
    
    saida[j] = y

# Plotando o sinal original e o sinal com delay
plt.figure()
plt.stem(entrada, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(saida, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Delay')
plt.title('Sinal Original e Sinal com Delay')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.yticks(np.arange(0, 1, 0.05))  # Define os intervalos do eixo Y de 0.05 em 0.05
plt.legend()
plt.grid(True)
plt.show()
```

#### c) Implementação do Eco

O eco é uma forma de delay onde o sinal original é misturado com uma versão atrasada dele mesmo.

```python
# Parâmetros de Eco
D = int(1e-3 * Fs)  # 1 ms delay
a0, a1 = 1.0, 0.5

# Entrada de impulso unitário
entrada = np.zeros(200)
entrada[0] = 1  # Impulso unitário

# Saída com eco
saida_eco = np.zeros(len(entrada))

for i in range(len(entrada)):
    if i >= D:
        saida_eco[i] = entrada[i] + a1 * entrada[i - D]
    else:
        saida_eco[i] = entrada[i]

# Plotando o sinal original e o sinal com eco
plt.figure()
plt.stem(entrada, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(saida_eco, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')
plt.title('Sinal Original e Sinal com Eco')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
```

### Executando o Código

Para executar os exemplos, você precisará de um ambiente Python configurado com as bibliotecas `numpy` e `matplotlib`. Após configurar o ambiente, copie e cole os códigos em um script Python ou em um Jupyter Notebook para visualizar os resultados.

