

# Processamento Digital de Sinais (DSP) - Exemplos e Implementações

Este repositório contém exemplos e implementações de códigos em Python para conceitos básicos de Processamento Digital de Sinais (DSP), incluindo a geração de sinais contínuos e discretos, bem como a visualização de diferentes tipos de sinais.

## Conteúdo

1. **Amostragem de um Sinal Contínuo**
2. **Sinais Discretos Básicos**
   - Impulso Unitário
   - Degrau Unitário
   - Sequência Senoidal
   - Sequência Exponencial

### 1. Amostragem de um Sinal Contínuo

Neste exemplo, geramos um sinal senoidal contínuo com uma frequência específica e, em seguida, o amostramos utilizando diferentes frequências de amostragem. O objetivo é visualizar o efeito da amostragem em diferentes condições.

#### Código

```python
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
plt.plot(t, sinal_continuo)
plt.title(f'Sinal Contínuo: {f_sinal}Hz')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

#### Explicação

- **f_sinal**: Define a frequência do sinal contínuo a ser gerado.
- **fs**: Define a frequência de amostragem.
- **t**: Cria um vetor de tempo para 1 segundo de duração com base na frequência de amostragem.
- **sinal_continuo**: Gera o sinal senoidal contínuo.
- **plt.plot**: Plota o sinal contínuo.

### 2. Sinais Discretos Básicos

Esta seção abrange diferentes tipos de sinais discretos básicos, como Impulso Unitário, Degrau Unitário, Sequência Senoidal e Sequência Exponencial.

#### a) Impulso Unitário

```python
n = np.arange(-10, 11)
impulso = np.where(n == 0, 1, 0)

plt.stem(n, impulso, use_line_collection=True)
plt.title('Impulso Unitário')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

- **Impulso Unitário**: É uma sequência que assume o valor de 1 em n=0 e 0 em qualquer outro ponto. Utilizamos `np.where` para definir o impulso.

#### b) Degrau Unitário

```python
degrau = np.where(n >= 0, 1, 0)

plt.stem(n, degrau, use_line_collection=True)
plt.title('Degrau Unitário')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

- **Degrau Unitário**: É uma sequência que assume o valor de 1 para n >= 0 e 0 para n < 0.

#### c) Sequência Senoidal

```python
f_senoidal = 100
fs = 8000
t = np.arange(0, 1, 1/fs)

sequencia_senoidal = np.sin(2 * np.pi * f_senoidal * t)

plt.stem(t, sequencia_senoidal, use_line_collection=True)
plt.title('Sequência Senoidal')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

- **Sequência Senoidal**: Gera uma sequência senoidal com frequência de 100 Hz, amostrada a 8 kHz.

#### d) Sequência Exponencial

```python
A = 1
a_values = [0.5, -0.5, 2]
n = np.arange(0, 50, 1)

plt.figure()

for a in a_values:
    exponencial = A * (a ** n)
    plt.stem(n, exponencial, label=f'a = {a}', use_line_collection=True)

plt.title('Sequência Exponencial')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
```

- **Sequência Exponencial**: Calcula uma sequência exponencial para diferentes valores de "a" e plota cada uma.

### Como Fazer a Plotagem de Forma Amostrada com Pontos

Para exibir os gráficos de forma amostrada com pontos, utilize o comando `plt.stem` ao invés de `plt.plot`. O comando `plt.stem` é projetado para mostrar sequências discretas com linhas verticais e marcadores, o que facilita a visualização da natureza discreta do sinal.

#### Exemplo

```python
plt.stem(n, impulso)
```

- **`use_line_collection=True`**: Esta opção otimiza a renderização para sequências discretas, melhorando o desempenho para grandes conjuntos de dados.

### Executando o Código

Para executar os exemplos, você precisará de um ambiente Python configurado com as bibliotecas `numpy` e `matplotlib`. Após configurar o ambiente, copie e cole os códigos em um script Python ou em um Jupyter Notebook para visualizar os resultados.

