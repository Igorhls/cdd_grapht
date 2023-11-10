import matplotlib.pyplot as plt

# Dados da sequência de bits
sequencia_bits = "1001101100"

# Função para plotar o gráfico da codificação Manchester Diferencial
def plot_codificacao_manchester_diferencial(sequencia_bits):
    nivel_eletrico = []
    transicoes_meio_bit = []
    transicoes_inicio_bit = []

    ultimo_nivel = 0
    for bit in sequencia_bits:
        if bit == '1':
            nivel_eletrico.append(-ultimo_nivel)
            nivel_eletrico.append(ultimo_nivel)
            transicoes_meio_bit.append(len(nivel_eletrico) - 2)
            transicoes_inicio_bit.append(len(nivel_eletrico) - 1)
            ultimo_nivel = -ultimo_nivel
        else:
            nivel_eletrico.append(ultimo_nivel)
            nivel_eletrico.append(-ultimo_nivel)
            transicoes_meio_bit.append(len(nivel_eletrico) - 2)
            transicoes_inicio_bit.append(len(nivel_eletrico) - 1)

    plt.figure(figsize=(10, 2))
    plt.title("Codificação Manchester Diferencial")
    plt.xlabel("Tempo")
    plt.ylabel("Nível Elétrico")
    plt.step(range(len(nivel_eletrico)), nivel_eletrico, where='post', color='blue', linewidth=1.5)
    plt.ylim(min(nivel_eletrico) - 1, max(nivel_eletrico) + 1)
    for idx, t in enumerate(transicoes_meio_bit):
        plt.axvline(t, color='red', linestyle='--', linewidth=1.5)
        plt.text(t, max(nivel_eletrico) + 0.5, f"Transição {idx + 1}", color='red')
    for t in transicoes_inicio_bit:
        plt.axvline(t, color='green', linestyle='--', linewidth=1.5)
    plt.xticks(range(len(sequencia_bits) * 2), list(sequencia_bits) * 2)
    plt.yticks([-1, 0, 1], ['-1', '0', '1'])
    plt.grid(True)
    plt.show()

# Plotar o gráfico da codificação Manchester Diferencial
plot_codificacao_manchester_diferencial(sequencia_bits)
