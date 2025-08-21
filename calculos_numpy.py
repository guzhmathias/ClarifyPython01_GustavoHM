import numpy as np

# Criando uma array Numpy (vetor)

arr = np.array([1,2,3,4,5])

print(f"Array Numpy: \n{arr}")

# Operações matemáticas em Arrays

print(f"Array Multiplicado por 2\n{arr * 2}")

print(arr[2] * arr[4])

# Operações entre Arrays

arr2 = np.array([10,20,30,40,50])
print(arr + arr2)

# Criando uma Matriz (2D)
matriz = np.array([[1,2,3],[4,5,6]])
print(f"Matriz 2 x 3: \n{matriz}")

# Soma e Média da Matriz

print(f'Soma de todos os elementos da matriz: \n{np.sum(matriz)}')
print(f'Média de todos os elementos da matriz: \n{np.mean(matriz)}')
print(f'Matriz Transposta: \n{matriz.T}')


# Gerando Números Aleatórios
print(f'Numeros aleatórios entre 0 e 1: \n{np.random.rand(3,3)}')

# Valor Máximo e mínimo da Array (max e min)

print(f"Valor máximo da Array \n{np.max(arr)}\nValor máximo da Array \n{np.min(arr)}")

# Desvio padrão em média de dispersão (std)
print(f'\nDesvio padrão da array\n{np.std(arr2)}')

# Indexação Avançada 
print(f"\nElementos maiores que 3 \n{arr[arr > 3]}")

# Ordenação
arr3 = np.array([24,6,95,3,19,65,7])
print(f"Array Ordenada\n{np.sort(arr3)}")

# Gerando números aleatórios entre 1 e 100
print(f"Números aleatórios entre 1 e 100\n{np.random.randint(1,100, size=(3,3))}")

#Reorganizando dados
print(f"Reshape da matriz (2x3) para (3x2)\n{matriz.reshape(3,2)}")