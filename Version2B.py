# Programa que permite multiplicar un escalar por una matriz con entrada del usuario

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

# Función para multiplicar un escalar por una matriz
def multiplicar_escalar_matriz(matriz, escalar):
    return [[escalar * matriz[i][j] for j in range(len(matriz[0]))] for i in range(len(matriz))]

# Ingresar la matriz
filas, columnas = 2, 2
matriz = ingresar_matriz(filas, columnas)

# Ingresar el escalar
escalar = int(input("Ingrese el valor del escalar: "))

# Multiplicación
resultado = multiplicar_escalar_matriz(matriz, escalar)

# Mostrar el resultado
print("Resultado de la multiplicación:")
for fila in resultado:
    print(fila)
