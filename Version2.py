# Programa que permite sumar y restar matrices con entrada del usuario

# Función para ingresar una matriz
def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de una matriz de {filas}x{columnas}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

# Función para sumar matrices
def suma_matrices(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

# Función para restar matrices
def resta_matrices(m1, m2):
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

# Dimensiones de las matrices
filas, columnas = 2, 2

# Ingresar las dos matrices
matriz1 = ingresar_matriz(filas, columnas)
matriz2 = ingresar_matriz(filas, columnas)

# Sumar y restar matrices
suma = suma_matrices(matriz1, matriz2)
resta = resta_matrices(matriz1, matriz2)

# Mostrar resultados
print("Suma de las matrices:")
for fila in suma:
    print(fila)

print("\nResta de las matrices:")
for fila in resta:
    print(fila)
