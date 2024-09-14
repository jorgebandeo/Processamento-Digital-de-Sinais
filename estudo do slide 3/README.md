
# Processamento Digital de Sinais (DSP) - Implementações e Algoritmos (Aula 3)

Este repositório contém implementações de algoritmos em Python para conceitos avançados de Processamento Digital de Sinais (DSP), incluindo a transformação de variáveis e convolução, além da aplicação da média móvel usando convolução.

## Conteúdo

1. **Transformação de Variáveis**
   - Reversão no Tempo
   - Deslocamento no Tempo (Atraso e Avanço)
2. **Convolução**
   - Conceito e Implementação
   - Aplicação da Média Móvel usando Convolução

### 1. Transformação de Variáveis

#### a) Reversão no Tempo

A reversão no tempo é uma transformação na qual o sinal é invertido ao longo do eixo do tempo. Isto é útil em várias aplicações de DSP para manipulação de sinais, como em sistemas de controle e filtragem.

```python
import numpy as np
import matplotlib.pyplot as plt

# Sinal de exemplo
n = np.arange(0, 10)
x = np.sin(2 * np.pi * 0.1 * n)

# Reversão no tempo
x_reverso = x[::-1]

plt.figure()
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(n, x_reverso, linefmt='r-', markerfmt='ro', basefmt='k-', label='Reverso no Tempo')
plt.title('Reversão no Tempo')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
```

#### b) Deslocamento no Tempo

O deslocamento no tempo pode ser um atraso ou avanço do sinal. Ele é usado em várias aplicações, como em algoritmos de compensação de tempo ou na introdução de delay.

```python
# Deslocamento no tempo - Atraso
atraso = 3
x_atrasado = np.roll(x, atraso)

plt.figure()
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(n, x_atrasado, linefmt='r-', markerfmt='ro', basefmt='k-', label='Atraso de 3 amostras')
plt.title('Deslocamento no Tempo - Atraso')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
```

### 2. Convolução

A convolução é uma operação matemática fundamental no processamento de sinais. Ela combina dois sinais para produzir um terceiro sinal, que representa como a forma de um sinal é modificada por outro.

#### a) Conceito e Implementação

A convolução pode ser calculada em Python usando a função `np.convolve`.

```python
# Definindo as sequências x[k] e h[k]
x = [1, 1, 1, 1, 1, 1]
h = [1, 0.5, 0.25, 0.125]

# Calculando a convolução
y = np.convolve(x, h)

# Plotando o resultado da convolução
plt.figure()
n = np.arange(0, len(y))
plt.stem(n, y, use_line_collection=True)
plt.title('Convolução de x e h')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

#### b) Média Móvel usando Convolução

A média móvel é uma técnica de suavização de sinais que pode ser implementada de forma eficiente utilizando convolução.

```python
# Sinal de exemplo
sinal = np.random.randn(100)  # Sinal aleatório

# Definindo o filtro de média (kernel) de tamanho k
k = 8  # Tamanho da janela de média
kernel = np.ones(k) / k  # Filtro de média móvel

# Calculando a média móvel usando convolução
media_movel = np.convolve(sinal, kernel, mode='valid')

# Plotando o sinal original e a média móvel
plt.figure()
plt.plot(sinal, label='Sinal Original')
plt.stem(np.arange(len(media_movel)), media_movel, label='Média Móvel (Convolução)', linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('Média Móvel usando Convolução')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
```

### Executando o Código

Para executar os exemplos, você precisará de um ambiente Python configurado com as bibliotecas `numpy` e `matplotlib`. Após configurar o ambiente, copie e cole os códigos em um script Python ou em um Jupyter Notebook para visualizar os resultados.
