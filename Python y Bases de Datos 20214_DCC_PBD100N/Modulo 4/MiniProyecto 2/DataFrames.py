# Import de librerias a utilizar
import mysql.connector as db

# Creación de conexión
import pandas as pd

mydb = db.connect(
    host = 'localhost',
    port = "8889",
    user = 'root',
    passwd = 'root',
    database = 'Cine'
)

# Crear cursor
cur = mydb.cursor()

# Lista de películas, el año, su director y el puntaje (rank) solo para las películas con rank mayor a 8 ordenadas en forma decreciente
cur.execute("SELECT m.name as 'Pelicula', m.year AS 'Agno', d.last_name AS 'Director', m.ranking as 'Puntaje' FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id) JOIN directors AS d ON d.id = director_id WHERE m.ranking > 8 ORDER BY m.ranking DESC;")
rows = cur.fetchall()
lista = []
for d in rows:
    lista.append(d)
df1 = pd.DataFrame(lista, columns=['Pelicula','Agno','Director','Puntaje'])
print(df1)
# Escriba un programa Python Dataframes.py que efectúe la consulta 3.3,
# pero el resultado lo cargue en un dataframe Pandas df1 con las
# siguientes columnas: Pelicula, Agno, Director, Puntaje

# • Recorte ese dataframe usando loc de modo de tomar solo
# las primeras 10 filas y solo las columnas Película y Puntaje.
# Imprima el nuevo Dataframe resultante.
df2 = df1.loc[:9, ['Pelicula','Puntaje']]
print(df2)
# • Recorte nuevamente df1 ahora usando iloc de modo de tomar las
# filas 20 a la 50 y todas las columnas. Imprima el nuevo Dataframe resultante.
df3 = df1.iloc[19:49,:]
print(df3)