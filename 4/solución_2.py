cont = 0

with open ('input.txt', 'r') as archivo:
    lineas = archivo.readlines()

lineas = [linea.strip() for linea in lineas]

n = len(lineas)
m = len(lineas[0])

lineas.insert(0, '.' * (m+2)) # Margen superior
lineas.append('.' * (m+2)) # Margen inferior

for i in range(len(lineas)):
    linea = '.' + lineas[i] + '.' # Margen lateral
    lineas[i] = linea

cambios = True
while cambios:
    cambios = False
    for i in range(1, n+1):
        for j in range(1, m+1):
            if lineas[i][j] == '@':
                vecinos = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (di != 0 or dj != 0) and lineas[i + di][j + dj] == '@':
                            vecinos += 1
                if vecinos < 4:
                    cont += 1
                    lineas[i] = lineas[i][:j] + '.' + lineas[i][j+1:]
                    cambios = True

print(cont)