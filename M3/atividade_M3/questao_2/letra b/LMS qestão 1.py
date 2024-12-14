import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm  # Para barra de progresso
import time  # Para medir o tempo de execução

# Carregar Sinal de Entrada (x[n])
with open('questão 2/letra b/ruido_branco.pcm', 'rb') as fid:
    x = np.fromfile(fid, np.int16)

# Carregar Sinal Esperado (d[n])
with open('questão 2/letra b/dn_Q2.pcm', 'rb') as fid:
    d = np.fromfile(fid, np.int16)

# Função LMS adaptativa
def lms_filter(x, d, u, K):
    N = len(x)
    e = np.zeros(N)
    y = np.zeros(N, dtype=np.int16)
    w = np.zeros(K)  # Coeficientes adaptativos

    amostrasY = np.zeros(K)

    # Filtro LMS
    for i in range(len(x)):
        # Calcular saída atual do filtro adaptativo
        for j in range(len(w)):
            if (i - j) >= 0:
                amostrasY[j] = x[i - j] * w[j]
        y[i] = amostrasY.sum()

        # Calcular o erro entre o sinal esperado e o sinal gerado
        e[i] = d[i] - y[i]

        # Atualizar os coeficientes adaptativos
        for k in range(len(w)):
            if (i - k) >= 0:
                w[k] += u * e[i] * x[i - k]

    return y, e, w

# Testar diferentes valores de u e K
us = [0.0000000001] #valor minimo para tender a 0 - 0.0000000001
Ks = [10]  #valor minimo para tender a 0 - 50

# Barra de progresso para combinar os parâmetros
total_iterations = len(us) * len(Ks)
progress_bar = tqdm(total=total_iterations, desc="Processamento", unit="combinação")

# Tempo total de execução
start_time = time.time()

for u in us:
    for K in Ks:
        iteration_start = time.time()

        # Executar o filtro LMS
        y, e, w = lms_filter(x, d, u, K)

        # Plotar resultados e salvar em imagens
        plt.figure(figsize=(10, 8))
        plt.subplot(3, 1, 1)
        plt.plot(d, 'b')
        plt.title(f"Sinal Esperado (d) - u={u:.1e}, K={K}")
        plt.grid()

        plt.subplot(3, 1, 2)
        plt.plot(y, 'r')
        plt.title("Saída do Filtro (y)")
        plt.grid()

        plt.subplot(3, 1, 3)
        plt.plot(e, 'g')
        plt.title("Erro (e)")
        plt.grid()

        plt.tight_layout()

        # Salvar como imagem
        image_filename = f"questão 2/letra b/resultados_u{u:.1e}_K{K}.png"
        plt.savefig(image_filename)
        plt.close()  # Fechar a figura para não exibir

        # Atualizar barra de progresso
        iteration_end = time.time()
        elapsed_time = iteration_end - iteration_start
        progress_bar.set_postfix_str(f"u={u:.1e}, K={K}, Tempo: {elapsed_time:.2f}s")
        progress_bar.update(1)

progress_bar.close()

# Tempo total de execução
end_time = time.time()
print(f"Processamento completo em {end_time - start_time:.2f} segundos.")
