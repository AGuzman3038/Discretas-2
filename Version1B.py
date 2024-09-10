# Programa para multiplicar un escalar por una matriz en Python
# Documentación:
# Este programa toma una matriz predefinida de tamaño 2x2 y un escalar,
# luego multiplica cada elemento de la matriz por el escalar.

# Definimos la matriz y el escalar
matriz = [[1, 2], [3, 4]]
escalar = 3

# Función para multiplicar un escalar por una matriz
def multiplicar_escalar_matriz(matriz, escalar):
    resultado = [[escalar * matriz[i][j] for j in range(len(matriz[0]))] for i in range(len(matriz))]
    return resultado

# Multiplicación
resultado = multiplicar_escalar_matriz(matriz, escalar)

# Mostramos el resultado
print("Resultado de la multiplicación:")
for fila in resultado:
    print(fila)
