cont = 0
baterias = 12

with open('input.txt', 'r') as archivo:
    lineas = archivo.readlines()
    
for linea in lineas:
    s = linea.strip()

    indice = 0
    activas = []
    for i in range(baterias):
        pos_fin = len(s) - (baterias - i)
        seg = s[indice:pos_fin + 1]
        mejor = max(seg)
        pos = seg.find(mejor) + indice
        activas.append(mejor)
        indice = pos + 1

    cont += int(''.join(activas))

print(cont)