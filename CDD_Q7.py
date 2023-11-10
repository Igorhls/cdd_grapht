import matplotlib.pyplot as plt

# Dados da sequência de bits
sequencia_bits = "1001101100"

# Função para plotar os gráficos das codificações
def plot_codificacao(codificacao, nivel_eletrico, transicoes):
    plt.figure(figsize=(10, 2))
    plt.title(f"Codificação {codificacao}")
    plt.xlabel("Tempo")
    plt.ylabel("Nível Elétrico")
    plt.step(range(len(nivel_eletrico)), nivel_eletrico, where='post', color='blue', linewidth=1.5)
    plt.ylim(min(nivel_eletrico) - 1, max(nivel_eletrico) + 1)
    for idx, t in enumerate(transicoes):
        plt.axvline(t, color='red', linestyle='--', linewidth=1.5)
        plt.text(t, max(nivel_eletrico) + 0.5, f"Transição {idx + 1}", color='red')
    plt.xticks(range(len(sequencia_bits)), list(sequencia_bits))
    plt.yticks([-1, 0, 1], ['-1', '0', '1'])
    plt.grid(True)
    plt.show()

# Codificação NRZ Polar
nrz_polar_nivel = [1 if bit == '1' else -1 for bit in sequencia_bits]
plot_codificacao("NRZ Polar", nrz_polar_nivel, [])

# Codificação NRZ-M
nrz_m_nivel = [1 if bit == '1' else -1 for bit in sequencia_bits]
nrz_m_transicoes = [idx for idx in range(1, len(sequencia_bits)) if sequencia_bits[idx] != sequencia_bits[idx - 1]]
plot_codificacao("NRZ-M", nrz_m_nivel, nrz_m_transicoes)

# Codificação NRZ-S
nrz_s_nivel = [1 if bit == '1' else -1 for bit in sequencia_bits]
nrz_s_transicoes = [idx for idx in range(1, len(sequencia_bits)) if sequencia_bits[idx] != sequencia_bits[idx - 1]]
plot_codificacao("NRZ-S", nrz_s_nivel, nrz_s_transicoes)

# Codificação RZ Unipolar
rz_unipolar_nivel = [1 if bit == '1' else 0 for bit in sequencia_bits for _ in range(2)]
rz_unipolar_transicoes = [idx*2 for idx in range(1, len(sequencia_bits))]
plot_codificacao("RZ Unipolar", rz_unipolar_nivel, rz_unipolar_transicoes)

# Codificação RZ Bipolar
rz_bipolar_nivel = [1 if bit == '1' else 0 for bit in sequencia_bits for _ in range(2)]
rz_bipolar_nivel[1::2] = [-1 if bit == '1' else 0 for bit in sequencia_bits]
rz_bipolar_transicoes = [idx*2 for idx in range(1, len(sequencia_bits)) if sequencia_bits[idx] != sequencia_bits[idx - 1]]
plot_codificacao("RZ Bipolar", rz_bipolar_nivel, rz_bipolar_transicoes)

# Codificação AMI
ami_nivel = []
ultimo_nivel = 0
for bit in sequencia_bits:
    if bit == '1':
        ami_nivel.append(1 if ultimo_nivel == 0 else -ultimo_nivel)
        ultimo_nivel = -ultimo_nivel
    else:
        ami_nivel.append(0)
plot_codificacao("AMI", ami_nivel, [])
