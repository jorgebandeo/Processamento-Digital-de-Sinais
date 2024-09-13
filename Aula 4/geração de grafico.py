import matplotlib.pyplot as plt

# Valores fornecidos
valores_y = [2, 3.5, 4.75, 5.87, 5.87,5.87, 3.87, 2.37, 1.12]
indices = ['y[n-3]', 'y[n-2]', 'y[n-1]', 'y[n]', 'y[n+1]', 'y[n+2]', 'y[n+3]', 'y[n+4]', 'y[n+5]']

# Plotagem do gráfico
plt.figure(figsize=(8, 6))
plt.plot(indices, valores_y, marker='o', linestyle='-', color='b', label='Valores de y[n]')
plt.title('Gráfico dos Valores de y[n]')
plt.xlabel('Amostras')
plt.ylabel('Valores')
plt.grid(True)
plt.legend()
plt.show()
