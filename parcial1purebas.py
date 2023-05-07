import os
import pandas as pd

class CSVReader:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = os.getcwd()  # Si no se proporciona una ruta, usar la ruta actual
        else:
            self.file_path = file_path
            if not os.path.exists(file_path):
                raise ValueError(f"La ruta proporcionada '{file_path}' no existe")

    def prompt_file_path(self):
        file_path = input("Por favor, ingrese la ruta del archivo o presione Enter para usar la ruta actual:\n")
        if file_path == "":
            self.file_path = os.getcwd()
        else:
            self.file_path = file_path
            if not os.path.exists(file_path):
                raise ValueError(f"La ruta proporcionada '{file_path}' no existe")

    def choose_files(self):
        files = os.listdir(self.file_path)
        csv_files = [f for f in files if f.endswith('.csv')]
        if len(csv_files) < 2:
             raise ValueError("Se necesitan al menos dos archivos CSV en la ruta especificada")
        print("Archivos CSV encontrados:")
        for i, file in enumerate(csv_files):
            print(f"{i+1}. {file}")
        file_indexes = input("Seleccione los archivos que desea abrir separados por comas (por ejemplo, 1,2): ").split(",")
        if len(file_indexes) != 2:
            raise ValueError("Debe seleccionar exactamente dos archivos CSV")
        selected_files = []
        for index in file_indexes:
            file_index = int(index) - 1
            if file_index < 0 or file_index >= len(csv_files):
                raise ValueError("Índice de archivo inválido")
            selected_files.append(os.path.join(self.file_path, csv_files[file_index]))
        return selected_files

    def read_csv_files(self):
        csv_files = self.choose_files()
        data1 = pd.read_csv(csv_files[0])
        data2 = pd.read_csv(csv_files[1])
        if len(data1) != len(data1.drop_duplicates()):
            raise ValueError("La primera tabla debe tener una columna con valores únicos")
        if not data2[data2.columns[0]].isin(data1[data1.columns[0]]).all():
            raise ValueError("La segunda tabla debe hacer referencia a elementos de la primera tabla")
        merged_data = pd.merge(data1, data2, on=data1.columns[0])  # Unir marcos de datos en una sola tabla
        return merged_data

csv_reader = CSVReader()
csv_reader.prompt_file_path()  # Preguntar al usuario por la ruta del archivo
data = csv_reader.read_csv_files()
print(data)

