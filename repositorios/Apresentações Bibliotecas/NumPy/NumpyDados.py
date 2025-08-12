import os
import numpy as np
os.system('cls')

dados = np.random.randint(1, 100, 10)  # 10 números aleatórios entre 1 e 99
print("Dados:", dados)

print("Média:", np.mean(dados))
print("Mediana:", np.median(dados))
print("Desvio padrão:", np.std(dados))