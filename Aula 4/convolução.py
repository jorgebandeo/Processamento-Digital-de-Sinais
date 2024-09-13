import matplotlib.pyplot as plt
import math as m
import numpy as np




def convolucao():
    # Solicitando a entrada do usuário para o primeiro array
    x_input = input("Digite os elementos do primeiro array separados por espaço: ")
    # Convertendo a entrada em um array NumPy
    x = np.array([float(num) for num in x_input.split()])
    x_n = int (input("Digite o momento:"))
    # Adicionando zeros no início do sinal para o deslocamento
    

    # Solicitando a entrada do usuário para o segundo array
    h_input = input("Digite os elementos do segundo array separados por espaço: ")
    # Convertendo a entrada em um array NumPy
    h = np.array([float(num) for num in h_input.split()])
    h_n = int (input("Digite o momento:"))
    # Adicionando zeros no início do sinal para o deslocamento
    

    init = min(x_n , h_n)
    return (np.convolve(x, h)) , init 

def media_movel ():
    x_input = input("Digite os elementos do array separados por espaço: ")
    # Convertendo a entrada em um array NumPy
    x = np.array([float(num) for num in x_input.split()])
    x_n = input("Digite o momento:")
    K_input = int(input("Digite o K da media movel: "))

    h = np.ones(K_input)
    y = np.convolve(x,h)
    return (y), len(y)


while(1):
    print("0) sair ")
    print("1) convolução de x e y ")
    print("2) media movel com convolução")
    op = input("opção")

    y = None

    if op == "1":
        y, init = convolucao()
    elif op == "2": 
        y, init = media_movel()
    elif op == "0":
        break

    # Criando o eixo x ajustado
    x = np.arange(init, init + len(y))

    # Plotando o sinal com o início definido
    plt.figure(figsize=(8, 6))
    plt.stem(x, y)
    plt.title('Sinal')
    plt.xlabel('Amostras')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()