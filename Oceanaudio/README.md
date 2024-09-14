
# Processamento Digital de Sinais (DSP) - Geração, Salvação e Leitura de Sinal em Formato PCM

Este documento explica como criar um sinal senoidal, exportá-lo no formato de áudio PCM (Pulse Code Modulation) para ser aberto no Ocenaudio, e posteriormente ler o arquivo PCM para visualização e análise do sinal em Python.

## Conteúdo

1. **Introdução**
2. **Configuração do Ambiente**
3. **Geração do Sinal Senoidal**
4. **Salvando o Sinal como PCM**
5. **Lendo o Arquivo PCM**
6. **Plotando o Sinal Lido**
7. **Como Executar o Código**

### 1. Introdução

O processamento de sinais digitais envolve a manipulação de sinais de áudio. Este exemplo demonstra como gerar um sinal senoidal, salvar o sinal no formato de áudio PCM, que é amplamente utilizado para representar sinais de áudio digitais, e abrir o arquivo PCM no Ocenaudio para escuta e análise.

### 2. Configuração do Ambiente

Para executar o código, você precisará do Python instalado em sua máquina e das bibliotecas necessárias:

```bash
pip install numpy matplotlib scipy
```

### 3. Geração do Sinal Senoidal

O código abaixo gera um sinal senoidal com frequência de 440 Hz (nota musical A), duração de 2 segundos, e uma frequência de amostragem de 8 kHz.

```python
import numpy as np
import matplotlib.pyplot as plt

def gerar_sinal_senoidal(frequencia, duracao, Fs):
    """
    Gera um sinal senoidal.

    Parâmetros:
    - frequencia: frequência da onda senoidal (Hz)
    - duracao: duração do sinal (segundos)
    - Fs: frequência de amostragem (Hz)

    Retorna:
    - n: vetor de tempo
    - x: sinal senoidal
    """
    n = np.arange(0, duracao, 1/Fs)  # Vetor de tempo
    x = np.sin(2 * np.pi * frequencia * n)  # Sinal senoidal
    return n, x
```

### 4. Salvando o Sinal como PCM

Após a geração do sinal, ele é salvo no formato PCM (16 bits), que pode ser aberto no Ocenaudio.

```python
def salvar_pcm(nome_arquivo, sinal):
    """
    Salva o sinal no formato PCM (16 bits).

    Parâmetros:
    - nome_arquivo: nome do arquivo para salvar o sinal (com extensão .pcm)
    - sinal: sinal a ser salvo (array numpy)
    """
    # Normalizar o sinal para o intervalo de -1 a 1
    sinal_normalizado = sinal / np.max(np.abs(sinal))
    
    # Converter para formato 16-bit PCM
    sinal_pcm = np.int16(sinal_normalizado * 32767)
    
    # Salvar em formato PCM
    with open(nome_arquivo, 'wb') as f:
        f.write(sinal_pcm.tobytes())
    print(f'Sinal salvo como "{nome_arquivo}".')
```

### 5. Lendo o Arquivo PCM

O código a seguir lê o arquivo PCM salvo e converte os dados brutos de áudio em um array numpy para plotagem e análise.

```python
def ler_pcm(caminho_arquivo, bit_depth=16):
    """
    Lê um arquivo PCM e retorna os dados de áudio.

    Parâmetros:
    - caminho_arquivo: caminho do arquivo PCM a ser lido
    - bit_depth: profundidade de bits do sinal (16 ou 32)

    Retorna:
    - audio_data: vetor numpy contendo o sinal de áudio
    """
    # Abrir o arquivo PCM
    with open(caminho_arquivo, 'rb') as f:
        raw_data = f.read()

    # Converter os dados brutos para numpy array
    if bit_depth == 16:
        audio_data = np.frombuffer(raw_data, dtype=np.int16)
    elif bit_depth == 32:
        audio_data = np.frombuffer(raw_data, dtype=np.int32)
    else:
        raise ValueError("Bit depth não suportado")

    return audio_data
```

### 6. Plotando o Sinal Lido

Após ler o arquivo PCM, o sinal é plotado para visualização:

```python
# Ler o arquivo PCM salvo
sinal_lido = ler_pcm(nome_arquivo_pcm, bit_depth=16)

# Plotar o sinal lido
plt.figure()
plt.plot(sinal_lido, label='Sinal Senoidal (Lido do PCM)')
plt.title('Sinal Senoidal do Arquivo PCM')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
```

### 7. Como Executar o Código

1. **Salve o código em um arquivo Python (`.py`) ou em um Jupyter Notebook.**
2. **Execute o script.** O sinal será gerado, salvo como `sinal_senoidal.pcm`, e o arquivo poderá ser aberto no Ocenaudio.
3. **Abra o arquivo PCM no Ocenaudio:** Inicie o Ocenaudio, clique em **Arquivo > Abrir** e selecione `sinal_senoidal.pcm`.
4. **Visualize e escute o sinal:** O Ocenaudio permitirá a visualização do sinal e sua reprodução.

### Conclusão

Este README explica como gerar um sinal senoidal, salvá-lo em formato PCM para uso em editores de áudio como Ocenaudio, e lê-lo para análise e visualização. Esta abordagem é útil para aplicações que envolvem processamento e manipulação de sinais digitais.
