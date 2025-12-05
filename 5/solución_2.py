with open("input.txt", "r") as archivo:
    datos = archivo.read()

lineas = datos.strip().split("\n\n")[0]
rangos = []

for linea in lineas.splitlines():
    a, b = map(int, linea.split("-"))
    rangos.append((a, b))

rangos.sort()

uion = [rangos[0]]

for ini, fin in rangos[1:]:
    last_ini, last_fin = uion[-1]

    if ini <= last_fin + 1: uion[-1] = (last_ini, max(last_fin, fin))
    else: uion.append((ini, fin))

cont = sum(b - a + 1 for a, b in uion)

print(cont)