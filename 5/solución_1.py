def is_fresh(id, rangos):
    return any(a <= id <= b for a, b in rangos)

with open("input.txt", "r") as archivo:
    datos = archivo.read()

lineas = datos.strip().split("\n\n")
rango = lineas[0].strip().splitlines()
ids = lineas[1].strip().splitlines()

rangos = []
for r in rango:
    a, b = map(int, r.split('-'))
    rangos.append((a, b))

ids = list(map(int, ids))

cont = sum(1 for x in ids if is_fresh(x, rangos))

print(cont)