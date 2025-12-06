cont = 0

with open ("input.txt", "r") as archivo:
    contenido = archivo.read()

lineas = contenido.splitlines()
numeros = []
n = len(lineas)-1
for i in range(n):
    numeros.append(lineas[i].split())

operaciones = lineas[-1].split()

pos = 0
for operacion in operaciones:
    operandos = []
    for i in range(n):
        operandos.append(int(numeros[i][pos]))
    resultado = operandos[0]

    if operacion == '*':
        for j in range(1, n):
            resultado *= operandos[j]
    elif operacion == '+':
        for j in range(1, n):
            resultado += operandos[j]
    cont += resultado
    pos += 1

print(cont)