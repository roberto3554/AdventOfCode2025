with open("input.txt") as archivo:
    lineas = [linea.rstrip() for linea in archivo.readlines()]

filas = len(lineas)
columnas = len(lineas[0])

grid = [list(linea) for linea in lineas]

caminos = [0] * columnas
caminos[filas // 2 - 1] = 1

for i in range(0, filas - 1):
    nuevos = [0] * columnas
    for j in range(columnas):
        if caminos[j] > 0:
            if grid[i + 1][j] == '^':
                nuevos[j - 1] += caminos[j]
                nuevos[j + 1] += caminos[j]
            else:
                nuevos[j] += caminos[j]
    caminos = nuevos

print(sum(caminos))