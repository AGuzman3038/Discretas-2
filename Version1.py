# Programa para sumar y restar dos matrices en Python
# Documentación:
# Este programa toma dos matrices de tamaño 2x2 predefinidas y realiza
# la suma y la resta entre ellas. Las matrices están definidas como listas de listas.
# Funciones clave:
# - suma_matrices: Función que toma dos matrices y devuelve su suma.
# - resta_matrices: Función que toma dos matrices y devuelve su resta.

# Definimos las matrices
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

# Función para sumar dos matrices
def suma_matrices(m1, m2):
    resultado = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return resultado

# Función para restar dos matrices
def resta_matrices(m1, m2):
    resultado = [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    return resultado

# Suma y resta de las matrices
suma = suma_matrices(matriz1, matriz2)
resta = resta_matrices(matriz1, matriz2)

# Mostramos los resultados
print("Suma de matrices:")
for fila in suma:
    print(fila)

print("\nResta de matrices:")
for fila in resta:
    print(fila)
