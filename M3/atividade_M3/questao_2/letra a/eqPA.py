import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

# 1. Definir parâmetros do filtro
Fs = 8000  # Frequência de amostragem
Fc = 400   # Frequência de corte
order = 2  # Ordem do filtro

# Calcular a frequência normalizada
Wn = Fc / (Fs / 2)

# Criar o filtro IIR passa-alta
b, a = butter(order, Wn, btype='high', analog=False)

# Exibir a resposta em frequência do filtro
w, h = freqz(b, a, fs=Fs)
plt.figure()
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Resposta em Frequência do Filtro Passa-Alta (IIR)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.show()

# 2. Processar o sinal de entrada
# Ler o sinal de entrada (ruido_branco.pcm)
input_signal = np.memmap("questão 2/letra a/ruido_branco.pcm", dtype='h', mode='r')

# Filtrar o sinal usando o filtro IIR
output_signal = lfilter(b, a, input_signal)

# Exibir o sinal de saída
plt.figure()
plt.plot(output_signal, label="Sinal Filtrado (Passa-Alta)")
plt.title("Sinal de Saída (Passa-Alta IIR)")
plt.xlabel("Amostras")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# 3. Salvar o sinal de saída
output_signal = output_signal.astype(np.int16)  # Converter para formato de 16 bits
with open("questão 2/letra a/dn_Q2.pcm", "wb") as f:
    output_signal.tofile(f)

print("Sinal filtrado salvo como 'dn_Q2.pcm'.")
