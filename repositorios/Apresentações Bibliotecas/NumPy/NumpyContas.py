import os
import numpy as np
os.system('cls')

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Soma
print("Soma:", a + b)

# Multiplicação elemento a elemento
print("Multiplicação:", a * b)

# Potência
print("Potência:", a ** 2)

# Média e soma total
print("Média:", np.mean(a))
print("Soma total:", np.sum(a))
print("Soma total de tudo:", np.sum(a+b))