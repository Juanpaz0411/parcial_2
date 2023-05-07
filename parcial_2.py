import pandas as pd
import os

class BaseDeDatos:
    def __init__(self, **kwargs):
        self.databases = {}
        for name, path in kwargs.items():
            df = pd.read_csv(path)
            self.databases[name] = df

    def generate_database(self):
        data = {'id': [1, 2, 3, 4, 5],
                'nombre': ['Juan', 'Pedro', 'María', 'Luisa', 'Ana'],
                'edad': [25, 30, 27, 23, 28]}
        return pd.DataFrame(data)

    def procesar_archivos(self):
        nombres = input('\nIngrese los nombres de los archivos separados por espacios:\n').split()
        if not nombres or nombres == '':
            exit()
        else:
            ingresar_ruta = input('\nDesea ingresar una ruta? Responda si o no:\n')
            rutas = {}

            if not ingresar_ruta or ingresar_ruta.lower() == 'no':#.lower permite que no importe si hay minuscula o mayuscula
                ruta_actual = os.path.dirname(os.path.abspath(__file__))#se utiliza para obtener la ruta del directorio que contiene el archivo de script actual en Python.
                rutas = {nombre: ruta_actual for nombre in nombres}
                print('Como no se ingresó una ruta, la ruta por defecto será:', ruta_actual)
            elif ingresar_ruta.lower() == 'si':
                rutas_input = input('\nIngrese las rutas correspondientes a los archivos separadas por <;>:\n').split(';')
                if len(rutas_input) < len(nombres):
                    continuar = input('\nel numero de rutas es menor al numero de nombres de archivos, quiere continuar?\n')
                    if continuar.lower() == 'si':
                        print('Como no se ingresaron algunas rutas, para estos archivos la ruta será:', os.path.dirname(os.path.abspath(__file__)))
                        ruta_actual = os.path.dirname(os.path.abspath(__file__))
                        rutas_input.extend([ruta_actual] * (len(nombres) - len(rutas_input)))#.extended() agrega datos de una lista que esta en los parentesis a la que precede a .extended()
                    else:
                        exit()
                elif len(rutas_input) > len(nombres):
                    print('\nLa cantidad de rutas excede la cantidad de nombres de archivos \n')
                    exit()
                rutas = {nombre: ruta for nombre, ruta in zip(nombres, rutas_input)}#zip()mas de dos listas en tupla
            else:
                print('\nRespuesta inadecuada\n')
                exit()

            print('\nLos archivos con sus respectivas ubicaciones son:\n')
            for nombre, ruta in rutas.items():
                print("{} : {}".format(nombre, ruta))

            verificacion = input('\nDesea verificar si los archivos están en las rutas indicadas? Responda si o no\n')
            if verificacion.lower() == 'si':
                self.validar_nombres_archivos(nombres, rutas)
            else:
                exit()
# README.md commit_final.py parcial1.py
#C:\Users\USUARIO WINDOWS\programacion\parcial_2;C:\Users\USUARIO WINDOWS\programacion\parcial_pruebas;C:\Users\USUARIO WINDOWS\programacion\parcial_1

    def validar_nombres_archivos(self, nombres, rutas):
        resultados = {}
        for nombre, ruta in rutas.items():
            archivo = os.path.join(ruta, nombre)
            if os.path.exists(archivo):
                resultados[nombre] = 'si está en la ruta indicada'
                print("\n{} está en la ruta indicada".format(nombre))
            else:
                resultados[nombre] = 'no está en la ruta ingresada'
                print("\n{} no está en la ruta ingresada".format(nombre))

#punto 3

# Crear una instancia de la clase BaseDeDatos y llamar al método procesar_archivos
x = int(input('que punto del parcial se va a exponer? 1, 3, 8, 10, 11, 12, 15\n'))

if x is None or x not in (1, 3, 8, 10, 11, 12, 15):
    print('Respuesta invalida')
    exit()
elif x==1:
    bd = BaseDeDatos()
    bd.procesar_archivos()

