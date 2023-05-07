import pandas as pd
import os

class BaseDeDatos:
    def __init__(self, **kwargs):
        self.databases = {}
        for name, path in kwargs.items():
            df = pd.read_csv(path)
            self.databases[name] = df

#punto 1
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

    def bases_csv(self):
        respuesta = input("\nTiene alguna base de datos CSV para agregar? responda si o no:\n")
        if not respuesta or respuesta.lower() == 'no':
            self.generate_databases()
    
        elif respuesta.lower() == "si":
            nombres = input('\nIngrese el nombre de las bases de datos, deben ser dos y estar separados por espacios:\n').split()
            if len(nombres) != 2:
                print('Error, debe ingresar exactamente dos archivos CSV.')
                exit()
            else:
                ingresar_ruta = input ('\nDesea ingresar la ruta? Responda si o no: \n')
                if not ingresar_ruta or ingresar_ruta.lower() == 'no':
                    ruta_actual = os.path.dirname(os.path.abspath(__file__))
                    rutas = {nombre: ruta_actual for nombre in nombres}
                    print('Como no se ingresó una ruta, la ruta por defecto será:', ruta_actual)
                elif ingresar_ruta.lower() == 'si':
                    rutas_input = input('\nIngrese las rutas correspondientes a los archivos separadas por <;>:\n').split(';')
                    if len(rutas_input) < len(nombres):
                        print('Como no se ingresó una ruta, para estos archivos la ruta será:', os.path.dirname(os.path.abspath(__file__)))
                        ruta_actual = os.path.dirname(os.path.abspath(__file__))
                        rutas_input.extend([ruta_actual] * (len(nombres) - len(rutas_input)))
                    elif len(rutas_input) > len(nombres):
                        print('\nLa cantidad de rutas excede la cantidad de nombres de archivos \n')
                        exit()
                    rutas = {nombre: ruta for nombre, ruta in zip(nombres, rutas_input)}
                else:
                    print('\nRespuesta inadecuada\n')
                    exit()
                
                print('\nLos archivos con sus respectivas ubicaciones son:\n')
                for nombre, ruta in rutas.items():
                    print("{} : {}".format(nombre, ruta))
                

    def generate_databases(self):
        data1 = {'nombre': ['Juan', 'Pedro', 'María', 'Luisa', 'Ana'],
                'id': [1, 2, 3, 4, 5],
                'edad': [25, 30, 27, 23, 28]}
        df1 = pd.DataFrame(data1)#convierte data1 en un dataframe guardandolo en df1

        data2 = {'id': ['Carlos', 'Sofía', 'Miguel', 'Laura', 'Andrés'],
                'nombre': [101, 102, 103, 104, 105],
                'edad': [35, 29, 33, 26, 31]}
        df2 = pd.DataFrame(data2)

        self.databases['Data_1'] = df1#diccionario con llave Database1 al que se le asigna df1 cono clave
        self.databases['Data_2'] = df2

        directory = os.path.dirname(os.path.abspath(__file__)) 

        ruta1 = os.path.join(directory, 'database1.csv')  # ruta COMPLETA de database1 al ser convertido en csv
        ruta2 = os.path.join(directory, 'database2.csv')  #se agrega nombre a las databases.csv nuevas

        df1.to_csv(ruta1)  # se guardan los df en csv
        df2.to_csv(ruta2)  

        print('\nSe generaron dos bases de datos y se han guardaron como archivos CSV en:', directory)
        print('\nDatabase1:')
        print(df1)
        print('\nDatabase2:')
        print(df2)

        borrar = input('¿Desea conservar los archivos generados? Responda si o no:\n')
        if borrar.lower() == 'no':
            if os.path.exists(ruta1):
                os.remove(ruta1)#borra el archivo en la direccion completa ruta1
                print('database1.csv eliminado.')

            if os.path.exists(ruta2):
                os.remove(ruta2)
                print('database2.csv eliminado.')
        else:
            exit()
            





x = int(input('que punto del parcial se va a exponer? 1, 3, 8, 10, 11, 12, 15\n'))

if x is None or x not in (1, 3, 8, 10, 11, 12, 15):
    print('Respuesta invalida')
    exit()
elif x==1:
    bd = BaseDeDatos()
    bd.procesar_archivos()
elif x==3:
    bd = BaseDeDatos()
    bd.bases_csv()

