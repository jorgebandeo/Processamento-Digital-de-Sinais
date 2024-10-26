Aqui está o README com os cálculos detalhados e os códigos para cada filtro (passa-baixa e passa-alta) separados.

---

# Projeto de Filtros Digitais com Transformada Z e Resposta em Frequência

Este projeto implementa filtros digitais passa-baixa e passa-alta usando a transformação bilinear. Inclui o cálculo teórico da função de transferência discreta \( H(z) \) para cada filtro, a resposta em frequência e a visualização dos pólos e zeros.

## Índice
1. [Introdução](#introdução)
2. [Transformada Z e Resposta em Frequência](#transformada-z-e-resposta-em-frequência)
3. [Filtro Passa-Baixa](#filtro-passa-baixa)
4. [Filtro Passa-Alta](#filtro-passa-alta)
5. [Visualização dos Resultados](#visualização-dos-resultados)

---

## Introdução

Este README documenta a implementação de filtros digitais, incluindo a Transformada Z e a resposta em frequência. São abordados:
- Filtro Passa-Baixa de primeira ordem com transformação bilinear
- Filtro Passa-Alta de primeira ordem com transformação bilinear
- Resposta em frequência e gráfico de pólos e zeros para cada filtro

---

## Transformada Z e Resposta em Frequência

A Transformada Z é uma ferramenta essencial para a análise de sistemas discretos e cálculo de resposta em frequência. A resposta em frequência de um sistema é obtida ao avaliar sua função de transferência \( H(z) \) ao longo da unidade de círculo \( |z| = 1 \).

Em Python, utilizamos a função `freqz` para calcular e plotar a resposta em frequência.

---

## Filtro Passa-Baixa

### Cálculos e Função de Transferência

1. **Função de Transferência no Domínio Contínuo**:
   Para um filtro passa-baixa de primeira ordem, a função de transferência é:
   \[
   H(s) = \frac{\omega_c}{s + \omega_c}
   \]
   onde \( \omega_c = 2 \pi f_c \) é a frequência angular de corte.

2. **Transformação Bilinear**:
   Substituímos \( s \) pela transformação bilinear:
   \[
   s = \frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
   \]
   Substituindo e simplificando, obtemos:
   \[
   H(z) = \frac{0.282 + 0.282 z^{-1}}{1 - 0.436 z^{-1}}
   \]

3. **Identificação dos Pólos e Zeros**:
   - **Zero**: \( z = -1 \)
   - **Pólo**: \( z = 0.436 \)

### Código em Python para o Filtro Passa-Baixa

```python
from scipy.signal import bilinear, freqz
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do filtro passa-baixa
fc = 1000  # Frequência de corte em Hz
fs = 8000  # Frequência de amostragem em Hz
wc = 2 * np.pi * fc  # Frequência angular de corte em rad/s

# Coeficientes do filtro analógico
b_analog = [wc]
a_analog = [1, wc]

# Transformação bilinear para obter H(z)
b_digital, a_digital = bilinear(b_analog, a_analog, fs)

# Resposta em frequência
w, h = freqz(b_digital, a_digital, worN=8000, fs=fs)
plt.plot(w, 20 * np.log10(abs(h)), label="Passa-Baixa")
plt.title("Resposta em Frequência do Filtro Passa-Baixa")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.legend()
plt.show()
```

---

## Filtro Passa-Alta

### Cálculos e Função de Transferência

1. **Função de Transferência no Domínio Contínuo**:
   Para um filtro passa-alta de primeira ordem, a função de transferência é:
   \[
   H(s) = \frac{s}{s + \omega_c}
   \]

2. **Transformação Bilinear**:
   Substituímos \( s \) pela transformação bilinear:
   \[
   s = \frac{2}{T} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
   \]
   Substituindo e simplificando, obtemos:
   \[
   H(z) = \frac{0.718 - 0.718 z^{-1}}{1 - 0.436 z^{-1}}
   \]

3. **Identificação dos Pólos e Zeros**:
   - **Zero**: \( z = 1 \)
   - **Pólo**: \( z = 0.436 \)

### Código em Python para o Filtro Passa-Alta

```python
# Parâmetros do filtro passa-alta
b_analog = [1, 0]  # Numerador de H(s) = s / (s + wc)
a_analog = [1, wc]  # Denominador de H(s) = s / (s + wc)

# Transformação bilinear para obter H(z)
b_digital, a_digital = bilinear(b_analog, a_analog, fs)

# Resposta em frequência
w, h = freqz(b_digital, a_digital, worN=8000, fs=fs)
plt.plot(w, 20 * np.log10(abs(h)), label="Passa-Alta")
plt.title("Resposta em Frequência do Filtro Passa-Alta")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.legend()
plt.show()
```

---

## Visualização dos Resultados

### Pólos e Zeros dos Filtros

Para cada filtro, plotamos os pólos e zeros no plano \( z \).

```python
from scipy.signal import tf2zpk

# Calculando pólos e zeros para o filtro passa-baixa
zeros_pb, poles_pb, _ = tf2zpk(b_digital, a_digital)

# Calculando pólos e zeros para o filtro passa-alta
zeros_pa, poles_pa, _ = tf2zpk(b_digital, a_digital)

# Plotagem
plt.figure(figsize=(6, 6))
plt.plot(np.real(zeros_pb), np.imag(zeros_pb), 'o', label='Zeros Passa-Baixa')
plt.plot(np.real(poles_pb), np.imag(poles_pb), 'x', label='Pólos Passa-Baixa')
plt.plot(np.real(zeros_pa), np.imag(zeros_pa), 'o', label='Zeros Passa-Alta', color='orange')
plt.plot(np.real(poles_pa), np.imag(poles_pa), 'x', label='Pólos Passa-Alta', color='red')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.title("Pólos e Zeros dos Filtros Passa-Baixa e Passa-Alta no Plano z")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.legend()
plt.grid()
plt.show()
```

### Descrição dos Resultados

- **Pólos e Zeros**:
  - O gráfico mostra a localização dos pólos e zeros de cada filtro. A posição dos pólos e zeros determina a resposta em frequência do filtro.
- **Resposta em Frequência**:
  - O filtro passa-baixa atenua as frequências acima da frequência de corte.
  - O filtro passa-alta permite a passagem de frequências acima da frequência de corte e atenua as frequências abaixo dela.

---

## Conclusão

Este projeto mostra como calcular e implementar filtros digitais passa-baixa e passa-alta a partir de suas representações analógicas. A Transformada Z e a transformação bilinear foram essenciais para converter as funções de transferência contínuas \( H(s) \) para o domínio discreto \( H(z) \).