import os
import subprocess

def ejecutar_comando(comando):
    # ❌ Vulnerabilidad: ejecución de comandos del sistema
    os.system(comando)

def leer_archivo(ruta):
    archivo = open(ruta, "r")
    contenido = archivo.read()
    return contenido

def dividir(a, b):
    # ❌ Posible división por cero
    return a / b

def ejemplo():
    comando = input("Ingrese un comando: ")
    ejecutar_comando(comando)

    ruta = input("Ingrese ruta del archivo: ")
    print(leer_archivo(ruta))

    print(dividir(10, 0))

    password = "123456"  # ❌ Credencial hardcodeada
    print("Password:", password)

    try:
        x = 10 / 0
    except:
        # ❌ Except vacío
        pass

ejemplo()
