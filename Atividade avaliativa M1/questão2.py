import numpy as np
import matplotlib.pyplot as plt
def gera_sinal_inpuso(ponto, janela):
    # Entrada de impulso unitário
    entrada = np.zeros(janela)
    entrada[ponto] = 1  # Impulso unitário
    return entrada

def gera_sinal_degrau(ponto, panto2, janela):
    # Gerando degrau unitário
    entrada = np.zeros(janela)
    for i in range(len(entrada)):
        if (i >= ponto and i <= panto2):
            entrada[i] = 1
        else:
            entrada[i] = 0

    return entrada

    
def eco_sinal(sinal, a0, a1, D):
    # Saída com eco
    saida_eco = np.zeros(len(sinal))

    for i in range(len(sinal)):
        if i >= D: # para restringir acesso de index indefinido
            saida_eco[i] = a0*sinal[i] + a1 * saida_eco[i - D]
        else: # para qualquer valor inferior ao D1 atribuido o segundo termo e nulo
            saida_eco[i] = a0*sinal[i]
    return saida_eco
 

D = 8  # 1 ms delay
a0, a1 = 1.0, 0.9


degrau_unitario = gera_sinal_degrau(0,6, 30)
inpulso_unitario = gera_sinal_inpuso(0, 30)
degrua_eco =  eco_sinal(degrau_unitario, a0,  a1, D)
inpulso_eco =  eco_sinal(inpulso_unitario, a0,  a1, D)

# Plotando o sinal original e o sinal com eco
plt.figure()

plt.stem(inpulso_unitario, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem( inpulso_eco, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')

plt.title('Inpulso e Sinal com Eco')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.figure()

plt.stem(degrau_unitario, linefmt='b-', markerfmt='bo', basefmt='k-', label='Original')
plt.stem(degrua_eco, linefmt='r-', markerfmt='ro', basefmt='k-', label='Com Eco')

plt.title('Degrua e Sinal com Eco')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.xlim(-4, 30)
plt.show()
