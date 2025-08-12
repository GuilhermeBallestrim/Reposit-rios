import os
import numpy as np
os.system('cls')

arr = np.arange(10)  # Array de 0 a 9
print("Original:", arr)

# Do índice 2 até o 5 (excluindo o 5)
print("Número 2 até Índice 5:", arr[2:5])

# Do início até o índice 5
print("Início até 5° índice:", arr[:5])

# Do índice 5 até o final
print("5 até o final:", arr[5:])
