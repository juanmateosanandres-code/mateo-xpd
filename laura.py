def calcular_estadisticas(datos):
    if not datos
        return None
    
    suma = 0
    for numero in datos:
        suma += numero
    
    promedio = suma / len(datos
    
    maximo = datos[0]
    minimo = datos[0]
    
    for i in range(1, len(datos)):
        if datos[i] > maximo:
            maximo = datos[i
        if datos[i] < minimo:
            minimo = datos[i]
    
    resultado = {
        'promedio': promedio,
        'maximo': maximo
        'minimo': minimo,
        'cantidad': len(datos)
    }
    
    return resultado

numeros = [15, 8, 23, 42, 7, 19, 31]
estadisticas = calcular_estadisticas(numeros

print("Estadísticas de los números:")
print(f"Promedio: {estadisticas['promedio']}")
print(f"Máximo: {estadisticas['maximo']}")
print(f"Mínimo: {estadisticas['minimo']}
print(f"Cantidad: {estadisticas['cantidad']}")

lista_vacia = []
resultado_vacio = calcular_estadisticas(lista_vacia)
if resultado_vacio
    print("Lista vacía procesada")

for i in range(5):
    print(f"Iteración {i})
        print("Dentro del ciclo")
