import matplotlib.pyplot as plt

# Dados fornecidos na QUESTÃO 11
amostras_tensao = [13, 8, 6, 10, 16, 17.8, 14, 14.4, 23.4, 24, 18, 9.8]
codigo_digital = [7, 4, 3, 5, 9, 9, 7, 8, 12, 12, 10, 5]

# Configuração do gráfico
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.title("Conversão D/A")
plt.xlabel("Código Digital (4 bits)")
plt.ylabel("Tensão (Volts)")

# Plotagem dos pontos de amostra
plt.scatter(codigo_digital, amostras_tensao, color='red', label='Amostras')

# Plotagem da curva conectando os pontos
plt.plot(codigo_digital, amostras_tensao, 'b-', label='Curva de Conversão')

# Adicionando rótulos para cada ponto de amostra
for i in range(len(amostras_tensao)):
    plt.text(codigo_digital[i], amostras_tensao[i], f"{amostras_tensao[i]}V", ha='right', va='bottom')

# Adicionando legenda
plt.legend()

# Configuração da escala dos eixos
plt.xticks(range(16))
plt.yticks(range(0, 31, 5))

# Exibindo o gráfico
plt.show()
