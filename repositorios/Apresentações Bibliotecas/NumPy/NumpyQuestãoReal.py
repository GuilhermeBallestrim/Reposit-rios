import os
import numpy as np
os.system('cls')

notas = np.random.randint(30, 100, 24,)
#notas = np.array([60, 70, 56, 80, 98, 100, 90, 30, 56, 57, 56, 76, 78, 43, 59, 98, 87, 87, 65, 87, 88, 50, 10, 12, 10, 30, 60, 50, 70, 70, 71, 72])

aprovado = notas >= 60

print("Notas:", notas)

# Estatísticas
media = np.mean(notas)
mediana = np.median(notas)
desvio = np.std(notas)
nota_max = np.max(notas)
nota_min = np.min(notas)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desvio padrão: {desvio:.2f}")
print(f"Nota máxima: {nota_max}")
print(f"Nota mínima: {nota_min}")

# Quantidade de aprovados e reprovados
qtd_aprovados = np.sum(aprovado)
qtd_reprovados = len(notas) - qtd_aprovados

print(f"Aprovados: {qtd_aprovados}")
print(f"Reprovados: {qtd_reprovados}")