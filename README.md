
------------

## PARCIAL 2 DE PROGRAMACIÓN😁

------------
##### Hecho por: *Juan jose paz hormiga*
 
Se evaluaran los siguientes puntos y como estudiante F se realizaran los apartados

	importar datos: puntos 1,3
	procesar datos: puntos 8, 10, 11
	Graficar: puntos 12, 15
	Requisitos generales: puntos 16, 17, 18


importar datos: 

1.Construya una clase que pueda recibir como argumentos al momento de definirla el nombre de uno o varios archivos y opcionalmente la ubicación de cada uno. Si no se ingresa la ruta de algun archivo el programa supone que es la ruta actual y lee todos.
   
3.Las bases de datos que lee el programa son solo dos y las debe conseguir o generar, una de ellas tiene una columna con valores únicos. La segunda tabla hace referencia a elementos de esa primera tabla por medio de esos índices. Guarde las tablas de forma que el programa sea capaz de unir ambas tablas de forma correcta en una sola. Ver estructura de tablas en Fig. 1 Si lo resuleve usando SQL no debe hacer los ejercicios de procesar datos.

Procesar datos:

8.La clase debe tener un método que reciba condiciones para los datos tipo cadena y filtre los datos de la tabla con base en esa condición.

10.La clase debe tener un método que genere una matriz que tenga en cada elemento i, j la correlación entre la columna i y la columna j.

11.La clase debe tener un método que calcule los coeficientes de regresión lineal para dos columnas elegidas por el usuario. (Si hace regresión multi-lineal gana puntos adicionales, si la hace multi-lineal con regularización, gana aún más puntos adicionales).

Graficar:

12.Grafique el resultado del numeral anterior. En scatter los valores de la tabla y en línea la regresión lineal.

15.Implemente un método que al recibir una función matemática en dos variables definida a partir de una lambda, y el nombre de dos columnas de la tabla, grafique en 3D o en contornos esa gráfica.



para la ejecucion del codigo se importan las bibliotecas:

	 import pandas as pd
		#debido al uso de dataframes y la forma de configurarlos.
	
	import os
		#Para acceder a archivos del dispositivo, obtener rutas y crear documentos
	
	from sklearn.linear_model import LinearRegression
		#se importa la clase LinearRegression para hacer procesos relacionados a la regresión lineal
	
	import seaborn as sns
		# Para realizar la gráfica de dispersión y regresión lineal.
	
	import matplotlib.pyplot as plt
		#Para la gráficación en 3d.
	
	import random
		#Para generar tablas con valores genericos numéricos.

Para la ejecucion de la clase y viajar entre las lineas de codigo que corresponden a cada pregunta se usó:

	pregunta = int(input('punto del parcial: Elija un valor( 1, 3, 8, 10, 11, 12, 15)\n'))

donde la respuesta lleva la ejecucion del codigo que corresponde a los puntos del parcial.

#### Punto 1
se ejecuta cuando

	elif pregunta == 1: 
		rutas = obtener_rutas()
		if rutas:
			bd = BaseDeDatos(**rutas) 
		else:
			bd = BaseDeDatos()

#### punto 3
se ejecuta igual que el 3, 8, 10, 11 y se ejecutan cuando:

	elif pregunta == 3 or pregunta == 8 or pregunta == 10 or pregunta == 11 or pregunta == 12:
		bd = BaseDeDatos()
		bd.cargar_tablas()
		bd.unir_tablas()
A través de cargar tablase se ingresan dos documentos del tipo csv, se ingresan sus rutas y luego se verifican si estoss documentos estan en la ruta indicada usando comandos de os.

al finalizar la funcion 'def unir_tablas(self):' se ejecuta la sección del codigo que permite la ejecucion de las preguntas 8-11:

            self.filtrado(tabla_merge_df)
            self.generarar_matriz(tabla_merge_df)
            self.coeficientes(tabla_merge_df)
            self.grafica_dispersion(tabla_merge_df)


#### punto 8
se realiza en el método

	def filtrado(self, tabla_merge_df):
#### punto 10
Método

	def generarar_matriz(self, tabla_merge_df):
#### punto 11
Método

	def coeficientes(self, tabla_merge_df):
#### punto 12
Método

	def grafica_dispersion(self, tabla_merge_df):
#### punto 15
Es ejecutado a través de la funcion lambda:

	elif pregunta == 15:
		graficar_3d((lambda x, y: x**y), 'peso', 'edad') 

Para usar la funcion gráficar_3d se usan las columnas peso, edad creadas con ramdom en la funcion
	def generar_tabla_prueba(cant_valores):

