cont = 0

with open("input.txt") as archivo:
    lineas = archivo.readlines()

columnas = []
for i in range(len(lineas[0].strip())):
    columna = []
    for linea in lineas:
        columna.append(linea[i])
    columnas.append(columna)

centro = len(columnas) // 2

activas = {centro}

for fila in range(1, len(columnas[0])):
    nuevas = set()
    for col in activas:
        if columnas[col][fila] == '^':
            cont += 1
            nuevas.add(col - 1)
            nuevas.add(col + 1)
        else:
            nuevas.add(col)
    activas = nuevas

print(cont)