'''
la clase recibe el nombre de uno o varios archivos y opcionalmente la ubicación de
cada uno. si no se ingresa de algun ruta del archivo el programa asume que es la ruta
actual y lee todos los archivos de esta ruta. si no se le ingresa el nombre de ninguna
base de datos el programa debe generar la base de datos.
'''
import os
import pandas as pd


class Punto1:
    def __init__(self, file_names=[], file_paths=[]):
        # Constructor de la clase
        # Inicializa las variables file_names, file_paths y df
        self.file_names = file_names
        self.file_paths = file_paths
        self.df = None

        # Si no se proporcionaron nombres de archivo, se genera una nueva base de datos
        # de lo contrario, se lee la base de datos
        if not self.file_names:
            self.generate_database()
        else:
            self.read_database()

    def read_database(self):
        # Función que lee los archivos de la base de datos y los almacena en un dataframe
        # Si no se proporcionaron rutas de archivo, se asume que los archivos están en la ruta actual

        # Se obtiene la ruta actual
        current_dir = os.getcwd()

        # Se crea una lista de rutas de archivo a partir de los nombres de archivo y las rutas proporcionadas
        file_paths = [os.path.join(self.file_paths[i] if i < len(self.file_paths) else current_dir, self.file_names[i])
                      for i in range(len(self.file_names))]

        # Se lee cada archivo y se almacena en una lista de dataframes
        dfs = [pd.read_csv(file_path) for file_path in file_paths]

        # Se realiza un join entre los dataframes utilizando la columna con valores únicos como llave primaria
        self.df = dfs[0].merge(dfs[1], on='id', how='inner')

    def generate_database(self):
        # Función que genera una nueva base de datos

        # Se crea un dataframe de ejemplo
        data = {'id': [1, 2, 3, 4, 5],
                'nombre': ['Juan', 'Pedro', 'María', 'Luisa', 'Ana'],
                'edad': [25, 30, 27, 23, 28]}
        self.df = pd.DataFrame(data)

    def print_database(self):
        # Función que imprime la base de datos

        print(self.df)

# Crea una nueva instancia de la clase Database sin proporcionar nombres de archivo
db = Punto1()

# Imprime la base de datos
db.print_database()

# Crea una nueva instancia de la clase Database proporcionando nombres de archivo y rutas de archivo
db2 = Punto1(file_names=['data1.csv', 'data2.csv'], file_paths=['/home/user/data', '/home/user/data'])

# Imprime la base de datos
db2.print_database()



