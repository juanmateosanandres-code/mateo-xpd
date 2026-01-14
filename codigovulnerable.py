import os

def autenticar(usuario, contrasena):
    # ❌ Credenciales quemadas en el código (vulnerabilidad)
    usuario_correcto = "admin"
    contrasena_correcta = "1234"

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        return True
    else:
        return False


def ejecutar_comando(comando):
    # ❌ Ejecución de comandos del sistema sin validación
    os.system(comando)


def calcular_promedio(numeros):
    # ❌ No se valida si la lista está vacía
    suma = 0
    for n in numeros:
        suma += n
    return suma / len(numeros)


def leer_archivo(ruta):
    # ❌ No se controla si el archivo existe
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido


# -------- PROGRAMA PRINCIPAL --------

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if autenticar(usuario, contrasena):
    print("Acceso concedido")

    comando = input("Ingrese un comando del sistema: ")
    ejecutar_comando(comando)

    datos = []
    print("Promedio:", calcular_promedio(datos))

    texto = leer_archivo("archivo_inexistente.txt")
    print(texto)
else:
    print("Acceso denegado")
