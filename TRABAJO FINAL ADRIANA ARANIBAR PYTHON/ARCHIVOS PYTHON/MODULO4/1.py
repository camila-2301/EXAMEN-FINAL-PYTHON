#IMPORTAR PANDAS
import pandas as ps
ps.__version__

#CREAR UNA SERIE
# Crea una Serie de los numeros 10, 20 and 10.
numeros = ps.Series([10, 20, 10])
print(numeros)

# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
objetos = ps.Series(['rojo', 'verde', 'azul'])
print(objetos)

#CREAR UN DATAFRAME
# Crea un dataframe vacío llamado 'df'
df=ps.DataFrame
print(df)

# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
dic={}
dic["NUMERO"]=numeros
df=ps.DataFrame(dic)
print(df)

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
dic["OBJETO"]=objetos
df=ps.DataFrame(dic)
print(df)

#LEER UN DATAFRAME
#LEER ARCHIVO
lectura = ps.read_csv('./data/pandas/avengers.csv')
print(lectura)

#CREAR UN DATAFRAME
avengers=ps.DataFrame

#SERIE 1 DEL DATAFRAME CREADO
Nombres = ps.Series(['Tony Stark', 'Bruce Banner', 'Steve Rogers', 'Henry Pym', 'Thor Odinson', 'Janet Van Dyne', 'Clinton Francis Barton'])
#SERIE 2 DEL DATAFRAME CREADO
Heroes = ps.Series(['Iron Man', 'Hulk', 'Capitán América', 'Hombre Hormiga', 'Thor', 'Avispa', 'Ojo de Halcón'])

#COLOCAR INFORMACIÓN EN DATAFRAME
dic={}
dic["NOMBRE"]=Nombres
avengers=ps.DataFrame(dic)

dic["HEROE"]=Heroes
avengers=ps.DataFrame(dic)

print(avengers)

# Muestra las primeras 5 filas del DataFrame.
print(lectura.head())

# Muestra las primeras 10 filas del DataFrame. 
print(lectura.head(10))

# Muestra las últimas 5 filas del DataFrame.
print(lectura.tail())

# Muestra el tamaño del DataFrame
print(lectura.shape)

# Muestra los data types del dataframe
print(lectura.dtypes)

# Cambia el indice a la columna "fecha_inicio".
lectura1 = lectura.set_index("fecha_inicio")
print(lectura1)

# Ordena el índice de forma descendiente
lectura_des = lectura1.sort_values(by="fecha_inicio", ascending=False)
print(lectura_des)

# Resetea el índice
lectura1.reset_index(drop=True)
print(lectura1)