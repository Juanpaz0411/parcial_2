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
        nombres = input('Ingrese los nombres de los archivos separados por espacios:\n').split()
        ingresar_ruta = input('Desea ingresar una ruta? Responda si o no:\n')
        if not ingresar_ruta or ingresar_ruta.lower() == 'no':
            rutas = [os.getcwd()] * len(nombres)
            print('como no se ingreso ruta, la ruta por defecto será:',os.path.dirname(os.path.abspath(__file__)),)#obtener la ruta del directorio que contiene el archivo de script actual, ademas El archivo de script es el archivo de código fuente que contiene el código Python que se está ejecutando.
        elif ingresar_ruta.lower() == 'si':
            rutas = input('Ingrese las rutas correspondientes a los archivos separadas por <;>:\n').split(';')
        else:
            print('Respuesta inadecuada')
            exit()
        if len(rutas) != len(nombres):
            print('La cantidad de rutas no coinciden con la cantidad de nombres de archivos')
            exit()
        tupla = zip(nombres, rutas)
        print('Los archivos con sus respectivas ubicaciones son:')
        for nombre, ruta in tupla:
            print("{} : {}".format(nombre, ruta))
        verificacion = input('Desea verificar si los archivos estan en las rutas indicadas? de ser asi responda si\n')
        if verificacion.lower() == 'si':     
            self.validar_nombres_archivos(nombres, rutas)
        else:
            exit()

    def validar_nombres_archivos(self, nombres, rutas):
        resultados = {}
        for nombre, ruta in zip(nombres, rutas):
            archivo = os.path.join(ruta, nombre)
            if os.path.exists(archivo):
                resultados[nombre] = 'si está en la ruta indicada'
                print("{}: está en la ruta indicada".format(nombre))
            else:
                resultados[nombre] = 'no está en la ruta ingresada'
                print("{}: no está en la ruta ingresada".format(nombre))


# Crear una instancia de la clase BaseDeDatos y llamar al método procesar_archivos
bd = BaseDeDatos()
bd.procesar_archivos()
