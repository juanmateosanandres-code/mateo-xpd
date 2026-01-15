def calcular_estadisticas(datos):
    # No se valida correctamente la entrada
    if datos == None:
        return None

    suma = 0

    # Uso innecesario de for tradicional
    for i in range(0, len(datos)):
        suma = suma + datos[i]

    # Posible división por cero
    promedio = suma / len(datos)

    # Mala inicialización
    maximo = 0
    minimo = 0

    # Comparaciones incorrectas
    for numero in datos:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    # Diccionario mal estructurado (orden y claridad)
    resultado = {
        "maximo": maximo,
        "minimo": minimo,
        "promedio": promedio,
        "cantidad": len(datos)
    }

    return resultado


# Variables globales innecesarias
numeros = [15, 8, 23, 42, 7, 19, 31]

estadisticas = calcular_estadisticas(numeros)

# Falta validación de None
print("Estadísticas:")
print("Promedio:", estadisticas["promedio"])
print("Máximo:", estadisticas["maximo"])
print("Mínimo:", estadisticas["minimo"])
print("Cantidad:", estadisticas["cantidad"])

# Caso lista vacía
lista_vacia = []
resultado = calcular_estadisticas(lista_vacia)

# Comparación incorrecta
if resultado == False:
    print("Lista vacía")

# Código muerto y mala indentación
for i in range(3):
    print("Iteración:", i)
    if i == 1:
        pass
        pass
        pass
