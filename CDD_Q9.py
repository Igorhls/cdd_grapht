import matplotlib.pyplot as plt

# Função para realizar a divisão do pacote pelo polinômio gerador (G(x) = x^3 + x)
def division(pacote, polinomio):
    resultado = pacote[:]
    for i in range(len(pacote) - len(polinomio) + 1):
        if resultado[i] == '1':
            for j in range(len(polinomio)):
                resultado[i + j] = str(int(resultado[i + j]) ^ int(polinomio[j]))
    return resultado

# Pacote de bits transmitido (QUESTÃO 09)
pacote_bits = "100110100011000"
polinomio_gerador = "1001"

# Adicionando bits zero no final do pacote
pacote_com_zeros = pacote_bits + "000"

# Realizando a divisão
resultado_divisao = division(list(pacote_com_zeros), list(polinomio_gerador))

# Verificando se o resultado da divisão é igual a zero (sem erros de transmissão)
sem_erros = all(bit == '0' for bit in resultado_divisao)

# Configurando o gráfico
plt.figure(figsize=(10, 2))
plt.title("Análise CRC")
plt.xlabel("Bit")
plt.ylabel("Resto")
plt.yticks([0, 1], ['0', '1'])
plt.grid(True)

# Plotando o pacote de bits transmitido
plt.step(range(len(pacote_com_zeros)), [int(bit) for bit in pacote_com_zeros], where='post', color='blue', label='Pacote Transmitido')

# Plotando o polinômio gerador
plt.plot(range(len(pacote_com_zeros), len(pacote_com_zeros) + len(polinomio_gerador)), [int(bit) for bit in polinomio_gerador], 'g-', label='Polinômio Gerador')

# Plotando o resultado da divisão
plt.step(range(len(resultado_divisao)), [int(bit) for bit in resultado_divisao], where='post', color='red', label='Resultado da Divisão')

# Exibindo legenda
plt.legend()

# Exibindo o gráfico
plt.show()

# Verificando se há erros de transmissão
if sem_erros:
    print("Não há erros de transmissão no pacote.")
else:
    print("O pacote possui erros de transmissão.")
