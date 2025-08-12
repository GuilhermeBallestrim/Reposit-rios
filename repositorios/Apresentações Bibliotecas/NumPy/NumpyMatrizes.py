import numpy as np

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

# Multiplicação de matrizes
print("Multiplicação de matrizes:\n", np.dot(mat1, mat2))

# Transposta
print("Transposta:\n", mat1.T)

# Inversa
print("Inversa:\n", np.linalg.inv(mat1))
