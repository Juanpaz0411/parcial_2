import pandas as pd
import os

from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import random



class BaseDeDatos:
    """
    posee un conjunto de funciones que le permitirán al usuario 
    realizar una serie de operaciones sobre archivos, bien sean de su elección o autogenerados
    """
    #decorador
    def print_function_name(func):
        def wrapper(*args, **kwargs):
            print(f"\nEjecutando función {func.__name__}\n")
            return func(*args, **kwargs)
        return wrapper

    def __init__(self, **kwargs):#El método constructor de la clase recibe el nombre y la ruta de los archivos como  parámetros opcionales 
        self.databases = {}
        if kwargs:
            for nombre, ruta in kwargs.items(): #El diccionario contiene los nombres de los archivos y sus rutas correspondientes
                df = pd.read_csv(ruta+"/"+nombre)#La ruta completa se obtiene al concatenar el nombre y la ubicación del archivO, TAMBIEN FUNCION os.path.abspath(os.path.join(directorio, nombre_archivo))
                self.databases[nombre] = df# Cada base de datos es guardada en el diccionario databases teniendo su nombre como clave 
        else:
            generar = input('No hay base de datos csv, desea generar una? s [si] o n [no]: ')
            if generar.lower() == 's':
                self.generar_tablas()# Si no existen argumentos, el programa debe crear las bases de datos automáticamente 
            else:
                print('no se crearan archivos .CSV')
    
    #parte del punto 1
    @print_function_name
    def generar_tablas(self):
        '''
        Se construyen las tablas a partir de dos diccionarios
        Las tablas genéricas son empleados y ocupaciones, las cuales 
        están relacionadas por la columna id_ocupacion
        '''
        empleados = {'nombre': ['Juan', 'Pedro', 'María', 'Luisa', 'Ana'],
                     'id': [1, 2, 3, 4, 5],
                     'edad': [25, 30, 27, 23, 28],
                     'id_ocupacion': [1, 2, 3, 4,3],}

        ocupaciones = {'id': [1, 2, 3, 4],
                       'nombre': ['Administrador', 'Contador', 'RH', 'Ingeniero civil'],
                       'salario': [3500000, 2900000, 3300000, 2600000]}

        tabla_empleados = pd.DataFrame(empleados) #Cada diccionario es convertido en DataFrame
        tabla_ocupaciones = pd.DataFrame(ocupaciones)

        self.databases['empleados.csv'] = tabla_empleados #Los dataframes son añadidos a la base de datos 
        self.databases['ocupaciones.csv'] = tabla_ocupaciones

        ruta_actual = os.path.dirname(os.path.abspath(__file__))

        ruta_empleados = os.path.join(ruta_actual, 'empleados.csv') #Se genera la ruta completa para los nuevos archivos en formato CSV 
        ruta_ocupaciones = os.path.join(ruta_actual, 'ocupaciones.csv')

        tabla_empleados.to_csv(ruta_empleados)  # Cada Data Frame es guardado como archivo CSV 
        tabla_ocupaciones.to_csv(ruta_ocupaciones)

        print('\nTabla empleados:')
        print(tabla_empleados)
        print('\nTabla ocupaciones:')
        print(tabla_ocupaciones)
 
    #punto 3: 
    #parte del punto 3
    @print_function_name
    def cargar_tablas(self):
        """
        La función cargar_tablas() permite al usuario cargar las tablas necesarias a la base de datos
        """
        continuar = True
        while continuar:
            respuesta_usuario = input("\n¿Desea cargar una nueva tabla? Responda S [sí] o N [no]: \n")
            if respuesta_usuario.lower() == 's':
                self.cargar_tabla('Por favor ingrese el nombre del archivo:\n',
                                  'Por favor ingrese la ruta en la que se encuentra el archivo:\n')
            else:
                continuar = False


    #parte del punto 3
    @print_function_name
    def cargar_tabla(self, mensaje_archivo, mensaje_ruta):
        """
        La función cargar_tabla() permite obtener el dataframe correspondiente a un archivo
        """
        nombre = input(mensaje_archivo)
        ruta = input(mensaje_ruta)
        archivo = os.path.join(ruta, nombre)#obtiene la direccion completa

        try:
            tabla = pd.read_csv(archivo)
            self.databases[nombre] = tabla#se añáde a un diccionario databases.
            print("La tabla fue añadida exitosamente")
        except FileNotFoundError:#el archivo no se encontro en la ruta especificada.
            print("No se encontró el archivo en la ruta especificada")

    #parte del punto 3
    @print_function_name
    def unir_tablas(self):
        """
        La función unir_tablas() permite mezclar dos tablas relacionadas por un identificador
        """
        print('\nMerge sobre tablas relacionadas\n')
        nombre_1 = input('Ingrese el nombre de la primera tabla:\n')
        tabla_1 = self.databases[nombre_1] if nombre_1 != '' else pd.DataFrame()#si nombre no es valido se crea un DataFrame vacío para asegurarse de que tabla_1 tenga un valor válido y no sea None.
        while tabla_1.empty:# Mientras el DataFrame tabla_1 esté vacío, el bucle se ejecutará, .empty dice si esta vacio el dataframe
            print('La tabla no existe en la base de datos. Por favor ingrese un nombre válido')
            nombre_1 = input('Ingrese el nombre de la primera tabla. Si desea salir escriba exit\n')
            if nombre_1.lower() == 'exit':
                exit()
            else:
                tabla_1 = self.databases[nombre_1] if nombre_1 != '' else pd.DataFrame()#si se no se ingresa nada en nombre_1 se repite el bucle
        nombre_2 = input('Ingrese el nombre de la segunda tabla:\n')
        tabla_2 = self.databases[nombre_2] if nombre_2 != '' else pd.DataFrame()
        while tabla_2.empty:
            print('La tabla no existe en la base de datos. Por favor ingrese un nombre válido')
            nombre_2 = input('Ingrese el nombre de la segunda tabla. Si desea salir escriba exit\n')
            if nombre_2.lower() == 'exit':
                exit()
            else:
                tabla_2 = self.databases[nombre_2] if nombre_2 != '' else pd.DataFrame()
        columna_1 = input('Ingrese el nombre de la columna que relaciona ambas tablas para la tabla 1:\n')# Se solicitan los nombres de los identificadores que relacionan las tablas 
        columna_2 = input('Ingrese el nombre de la columna que relaciona ambas tablas para la tabla 2:\n')

        if columna_1 != '' and columna_2 != '':
            tabla_merge = pd.merge(tabla_1, tabla_2, left_on=columna_1,right_on=columna_2)# La función merge() permite unir las tablas de acuerdo a identificadores comunes , or defecto se agregan sufijos "_x" y "_y" a los nombres de las columnas que existen en ambas tablas para distinguirlas. 
            # left_on: Se utiliza para especificar la(s) columna(s) del DataFrame de la izquierda (tabla_1) que se utilizará(n) para la combinación.
            print(tabla_merge)
            tabla_merge_df = pd.DataFrame(tabla_merge)
            self.filtrado(tabla_merge_df)
            self.generarar_matriz(tabla_merge_df)
            self.coeficientes(tabla_merge_df)
            self.grafica_dispersion(tabla_merge_df)
        else:
            print('Las columnas indicadas no son válidas')

        #punto 8
    @print_function_name
    def filtrado(self, tabla_merge_df):
        '''
        recibe condiciones para los datos tipo cadena y filtre los datos de la tabla con base en esa condición.
        usando sintaxis de consulta de Pandas ejemplo 'nombre_columna'=>2, ==2,<=2 e incluso (edad > 30) & (salario <= 5000)
        '''
        condicion = input("Ingrese la condición de filtrado (usando sintaxis de consulta de Pandas ejemplo 'nombre_columna' => 25 , == 2, <= 2): ")
        tabla_filtrada = tabla_merge_df.query(condicion)#query() se aplica a tabla_merge con la condición proporcionada por el usuario. La condición debe seguir la sintaxis de consulta de Pandas para filtrar los datos.
        print("Tabla filtrada:")
        print(tabla_filtrada)


        #puntos 10
    @print_function_name
    def generarar_matriz(self, tabla_merge_df):
        '''
        genera una matriz que tiene en cada elemento i, j la correlación entre la columna i y la columna j de la tabla mezclada.
        '''
        matriz_corr = tabla_merge_df.corr(numeric_only=True)# El método corr() se aplica directamente a tabla_merge para calcular la matriz de correlación entre las columnas numéricas. Luego, la matriz de correlación se imprime en la salida.
        #numeric_only=True se le dice a pandas que solo tenga en cuenta las columnas numéricas 
        print("Matriz de correlación:")
        print(matriz_corr)

        #punto 11
    @print_function_name
    def coeficientes(self, tabla_merge_df):
        '''
        calcula los coeficientes de regresión lineal para dos columnas elegidas por el usuario.
        '''
        columna_1 = input("Ingrese el nombre de la primera columna para el cálculo de los coeficientes de regresión lineal: ")
        columna_2 = input("Ingrese el nombre de la segunda columna para el cálculo de los coeficientes de regresión lineal: ")

        if columna_1 in tabla_merge_df.columns and columna_2 in tabla_merge_df.columns:
            if tabla_merge_df[columna_1].dtype == 'object' or tabla_merge_df[columna_2].dtype == 'object':#devuelve el tipo de datos de la columna columna_1 en tabla_merge_df.
                print('Error: Solo se pueden utilizar columnas numéricas para el cálculo de los coeficientes de regresión lineal.')
                exit()
            else:
                X = tabla_merge_df[columna_1].values.reshape(-1, 1)
                y = tabla_merge_df[columna_2].values.reshape(-1, 1)
                # tabla_merge[columna_1]: Accede a la columna columna_1 en la tabla combinada (tabla_merge).
                # .values: Obtiene los valores de la columna.
                # .reshape(-1, 1): Reshapea el array a una matriz de una sola columna, donde el número de filas se ajusta automáticamente (-1) y el número de columnas se establece en 1.
                    #realiza una reorganización de la forma del array NumPy. La función .reshape() se utiliza para cambiar la forma de un array sin cambiar los datos. 
                regresion = LinearRegression()
                regresion.fit(X, y)#.fit() se encarga de encontrar los coeficientes del modelo de regresión lineal que mejor se ajusten a los datos proporcionados.
                # Realiza el proceso de aprendizaje utilizando los datos de entrenamiento y ajusta los parámetros internos del modelo para minimizar el error entre los valores reales y los valores predichos por el modelo.

                coeficiente_intercepto = regresion.intercept_[0] #coeficiente_intercepto es el valor de la variable dependiente cuando todas las variables independientes son cero. 
                coeficiente_pendiente = regresion.coef_[0][0]#coeficiente_pendiente es el coeficiente de pendiente que indica el cambio esperado en la variable dependiente por unidad de cambio en la variable independiente.


                print("Coeficientes de regresión lineal:")
                print(f"Intercepto: {coeficiente_intercepto}")
                print(f"Pendiente: {coeficiente_pendiente}")
        else:
            print("Las columnas ingresadas no existen en la tabla mezclada.")

    # def grafica_dispersion(self, tabla_merge_df):
    #     '''
    #     Genera una gráfica de dispersión y una línea de regresión lineal en el mismo gráfico para dos columnas elegidas por el usuario.
    #     '''
    #     sns.set(style='whitegrid')  # Establecer el estilo del gráfico

    #     columna_1 = input('Ingrese el nombre de la primera columna para la gráfica de dispersión: ')
    #     columna_2 = input('Ingrese el nombre de la segunda columna para la gráfica de dispersión: ')

    #     if columna_1 in tabla_merge_df.columns and columna_2 in tabla_merge_df.columns:
    #         if tabla_merge_df[columna_1].dtype == 'object' or tabla_merge_df[columna_2].dtype == 'object':
    #             print('La columna 1 o la columna 2 no es de tipo numérico.')
    #             exit()
    #         else:
    #             plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la gráfica
    #             sns.lmplot(data=tabla_merge_df, x=columna_1, y=columna_2, marker='D')  # Utilizar 'D' para representar diamantes como marcadores
    #             # Personalizar la gráfica
    #             plt.xlabel(columna_1)
    #             plt.ylabel(columna_2)
    #             plt.title('Gráfica de Dispersión')

    #             # Agregar leyenda
    #             plt.legend(labels=['Datos'])

    #             # Mostrar la gráfica
    #             plt.show()
    #     else:
    #         print('Las columnas indicadas no existen en la tabla combinada.')


    #punto 12
    @print_function_name
    def grafica_dispersion(self, tabla_merge_df):
        '''
        Genera una gráfica de dispersión y una línea de regresión lineal en el mismo gráfico para dos columnas elegidas por el usuario.
        '''
        sns.set(style='whitegrid')  # Establecer el estilo del gráfico

        columna_1 = input('Ingrese el nombre de la primera columna para la gráfica de dispersión: ')
        columna_2 = input('Ingrese el nombre de la segunda columna para la gráfica de dispersión: ')

        if columna_1 in tabla_merge_df.columns and columna_2 in tabla_merge_df.columns:
            if tabla_merge_df[columna_1].dtype == 'object' or tabla_merge_df[columna_2].dtype == 'object':
                print('La columna 1 o la columna 2 no es de tipo numérico.')
                exit()
            else:
                plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la gráfica
                sns.lmplot(data=tabla_merge_df, x=columna_1, y=columna_2)  # Utilizar 'D' para representar diamantes como marcadores
                # Personalizar la gráfica
                plt.xlabel(columna_1)
                plt.ylabel(columna_2)
                plt.title('Gráfica de Dispersión')

                # Agregar leyenda
                plt.legend(labels=['Datos'])

                # Mostrar la gráfica
                plt.show()
        else:
            print('Las columnas indicadas no existen en la tabla combinada.')
#PUNTO 1
def obtener_rutas():
    """
    La función obtener_rutas() permite solicitar al usuario tanto el nombre de los 
    archivos como la ruta correspondiente a cada uno. Hace uso de las funciones 
    imprimir_rutas() y validar_rutas(), las cuales permiten mostrar cada ubicación y 
    validarla respectivamente. Retorna un diccionario con las rutas indicadas por 
    el usuario (en caso de que hayan sido ingresadas) Si el usuario no indica los
    archivos a ser cargados, retorna None
    """
    nombres = input('\nIngrese los nombres de los archivos separados por comas:\n').split(',') #La función split() convierte la cadena en una lista según un caracter separador 

    nombres = list(map(lambda nombre: nombre.strip(),nombres))# La función map() hace uso de la función strip() para eliminar los espacios en blanco al inicio y al final de cada cadena de la lista de nombres
    
    if nombres != ['']: # Si el usuario no especifica el nombre de los archivos, nombres será una lista con un caracter vación en su interior. Así, el programa debe generar automáticamente las tablas

        ruta_actual = os.path.dirname(os.path.abspath(__file__))# Se toma como referencia el archivo actual (__file__) para obtener la ruta 
        respuesta_rutas = input('\n¿Los archivos se encuentran en una ruta diferente a la actual: {}?'.format(ruta_actual)+'\nResponda S [sí] o N [no]: ')

        isIngresar = True if respuesta_rutas.lower() == 's' else False # Se verifica si el usuario desea ingresar las rutas manualmente
        rutas = {}

        if isIngresar:
            for nombre in nombres:
                ruta = input('\nIngrese las ruta correspondiente al archivo {}:\n'.format(nombre))
                if not ruta or ruta == '': # Se debe verificar si el usuario ha ingresado una ruta ,Si lo hizo, la ruta es agregada al diccionario tomando como clave el nombre del archivo 
                        rutas[nombre] = ruta_actual
                # Si el usuario no ingresa una ruta, se asigna la ruta actual por defecto 
                else:
                        rutas[nombre] = ruta  # Si el usuario no quiere ingresar las rutas de manera manual, se hace uso de la ruta por defecto 
                        
        else:
            rutas = {nombre: ruta_actual for nombre in nombres}

        imprimir_rutas(rutas) # Se muestran las rutas ingresadas por el usuario 

        is_rutas_validas = validar_rutas(rutas) # Si las rutas ingresadas son válidas, se retornan

        if is_rutas_validas: # De lo contrario, se retorna None por defecto 
            return rutas
        

#parte del punto 1
def imprimir_rutas(rutas):
    """
    La función imprimir_rutas permite mostrar las rutas que han sido ingresadas  por el usuario
    """
    print('\nLos archivos con sus respectivas ubicaciones son:\n')

    for nombre, ruta in rutas.items(): #items() regresa los pares clave  [nombre] - valor [ruta] en forma de tuplas 
        print("{} : {}".format(nombre, ruta))

#parte del punto 1
def validar_rutas(rutas):
    """
    La función validar_rutas permite verificar la existencia de los archivos indicados por el usuario
    Retorna True si todos los archivos han sido encontrados. De cualquier otra manera, retorna False
    """
    ruta_incorrecta = "" # Se concatenan los nombres de las rutas que no sean encontradas
    for nombre, ruta in rutas.items():
        archivo = os.path.join(ruta, nombre) # Se obtiene la ruta del archivo 
        if not os.path.exists(archivo): #Si el archivo no se encuentra, la ruta se considera como incorrecta 
           ruta_incorrecta += "\n"+nombre#agregar el nombre del archivo a la variable ruta_incorrecta.
    if ruta_incorrecta == "":
        print("Todas las rutas han sido ingresadas correctamente")
        return True
    else:
        print("Los siguientes archivos no se encuentran en la ruta indicada:"+ruta_incorrecta)
        return False


#punto 15
def graficar_3d(funcion, nombre_col_x, nombre_col_y):
    """
    La función graficar_3d() permite obtener una gráfica a partir de una función lambda
    y el nombre las columnas correspondientes a los valores x - y
    Hace uso de la función generar_tabla_prueba() para crear una tabla con valores aleatorios
    a modo de prueba del método
    """
    tabla = generar_tabla_prueba(250)
    col_x = tabla[nombre_col_x]
    col_y = tabla[nombre_col_y]

    col_z = list(map(funcion, col_x, col_y))#utiliza la función map() para aplicar la función funcion a cada par de elementos de las listas col_x y col_y
    fig = plt.figure()#crea una nueva figura en blanco utilizando la biblioteca Matplotlib.
    plano = fig.add_subplot(111, projection='3d')#crea un nuevo conjunto de ejes en una figura existente y configura el tipo de proyección como 3D.
    plano.scatter(col_x, col_y, col_z, c='b', marker='D')

    plt.xlabel(nombre_col_x)
    plt.ylabel(nombre_col_y)
    plt.title('Gráfico en 3D')

    plt.show()

#parte del punto 15
def generar_tabla_prueba(cant_valores):
    """
    La función generar_tabla_prueba() crea una tabla con datos numéricos genéricos de acuerdo
    a una cantidad de valores especificada
    """
    tabla = {
        'peso': [random.randint(30, 80) for _ in range(cant_valores)],
        'altura': [random.uniform(1.5, 2) for _ in range(cant_valores)],#random genera un número decimal aleatorio dentro del rango especificado. 
        'edad': [random.randint(10, 80) for _ in range(cant_valores)],
        'distancia': [random.randint(20, 100) for _ in range(cant_valores)],
    }
    df = pd.DataFrame(tabla)
    return df




# empleados.csv ocupaciones.csv   #Los empleados están relacionados con las ocupaciones a través del id_ocupacion las ocupaciones con los empleados con id
# C:\Users\USUARIO WINDOWS\programacion\p2 help 

#exo_2.csv   libro1.csv
#C:\Users\USUARIO WINDOWS\programacion\parcial_2\parcial_2

"""
    Ejecución principal del programa
"""

pregunta = int(input('punto del parcial: Elija un valor( 1, 3, 8, 10, 11, 12, 15)\n'))

if pregunta is None or pregunta not in (1, 3, 8, 10, 11, 12, 15):
    print('El valor indicado no se encuentra dentro del rango')
    exit()

elif pregunta == 1: # El primer punto es resuelto a través de las funciones obtenerRutas() validar_rutas() e imprimir_rutas()  
    # Las rutas son solicitadas al usuario para poder iniciar la clase 
    rutas = obtener_rutas()
    if rutas:
        bd = BaseDeDatos(**rutas)
    # Si las rutas no son encontradas, se crea una base de datos con tablas por defecto 
    else:
        bd = BaseDeDatos()

elif pregunta == 3 or pregunta == 8 or pregunta == 10 or pregunta == 11 or pregunta == 12:#al ejecutar seccion se resuelven las preguntas 3, 8, 10, 11
    bd = BaseDeDatos() #Se instancia la base de datos 
    ### En caso de que el usuario desee cargar nuevas tablas, se le solicitan las rutas ###
    bd.cargar_tablas()
    ### A partir de dos tablas elegidas por el usuario, se genera una nueva tabla correspondiente ###
    ### a la unión de estas ###
    bd.unir_tablas()
    # Los empleados están relacionados con las ocupaciones a través del id_ocupacion

elif pregunta == 15:
    ### Se llama a la función graficar_3d() con la función lambda y los valores x - y ###
    graficar_3d((lambda x, y: x**y), 'peso', 'edad')#aca se ingresa la funcion matemática en X y Y

else:
    print('respuesta invalida ')
