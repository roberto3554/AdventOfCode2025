with open("input.txt", "r") as archivo:
    lineas = archivo.readlines()

lineas = [linea.rstrip('\n') for linea in lineas]
ancho_max = max(len(linea) for linea in lineas)
lineas = [linea.ljust(ancho_max) for linea in lineas]

operaciones_linea = lineas[-1]
lineas_numeros = lineas[:-1]

n_lineas_numeros = len(lineas_numeros)

resultado_total = 0
col_actual = ancho_max - 1

while col_actual >= 0:
    columna_actual = ''.join(lineas_numeros[i][col_actual] for i in range(n_lineas_numeros))
    if columna_actual.strip() == '':
        col_actual -= 1
        continue
    operandos = []
    
    while col_actual >= 0:
        columna = ''.join(lineas_numeros[i][col_actual] for i in range(n_lineas_numeros))
        if columna.strip() == '':
            break
        
        numero_digitos = []
        for i in range(n_lineas_numeros):
            digito = lineas_numeros[i][col_actual]
            if digito != ' ':
                numero_digitos.append(digito)
        
        if numero_digitos:
            numero_str = ''.join(numero_digitos)
            operandos.append(int(numero_str))
        
        col_actual -= 1

    if col_actual + 1 < len(operaciones_linea):
        operacion = operaciones_linea[col_actual + 1]
    else:
        temp_col = col_actual + 1
        while temp_col < len(operaciones_linea) and operaciones_linea[temp_col] == ' ':
            temp_col += 1
        if temp_col < len(operaciones_linea):
            operacion = operaciones_linea[temp_col]
        else:
            operacion = None
    
    if operacion and operandos:
        if operacion == '+':
            resultado = sum(operandos)
        elif operacion == '*':
            resultado = 1
            for op in operandos:
                resultado *= op
        
        resultado_total += resultado

print(resultado_total)