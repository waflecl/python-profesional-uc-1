# Import de librerias a utilizar
import pandas as pd
import mysql.connector as db

# Creación de conexión
mydb = db.connect(
    host = 'localhost',
    port = "8889",
    user = 'root',
    passwd = 'root',
    database = 'Cine'
)

# Crear cursor
cur = mydb.cursor()

# Cargar CSV's en DF y cambiar NaN por None
dfActors = pd.read_csv('datos/actors.csv', sep=';')
dfActors = dfActors.where((pd.notnull(dfActors)), None)
dfDirectors = pd.read_csv('datos/directors.csv', sep=';')
dfDirectors = dfDirectors.where((pd.notnull(dfDirectors)), None)
dfMovies = pd.read_csv('datos/movies.csv', sep=';')
dfMovies = dfMovies.where((pd.notnull(dfMovies)), None)
dfMoviesActors = pd.read_csv('datos/movies_actors.csv', sep=';')
dfMoviesActors = dfMoviesActors.where((pd.notnull(dfMoviesActors)), None)
dfMoviesDirectors = pd.read_csv('datos/movies_directors.csv', sep=';')
dfMoviesDirectors = dfMoviesDirectors.where((pd.notnull(dfMoviesDirectors)), None)

# Revisar carga correcta de DF
print('=== Dataframe Actors ===')
print(dfActors)
print('=== Dataframe Directos ===')
print(dfDirectors)
print('=== Dataframe Movies ===')
print(dfMovies)
print('=== Dataframe Movies Actors ===')
print(dfMoviesActors)
print('=== Dataframe Movies Directors ===')
print(dfMoviesDirectors)

# Generacion de tuplas para hacer insert
tuplaActors = [tuple(d) for d in dfActors.values.tolist()]
tuplaDirectors = [tuple(d) for d in dfDirectors.values.tolist()]
tuplaMovies = [tuple(d) for d in dfMovies.values.tolist()]
tuplaMoviesActors = [tuple(d) for d in dfMoviesActors.values.tolist()]
tuplaMoviesDirectors = [tuple(d) for d in dfMoviesDirectors.values.tolist()]

# Query y commit para hacer insert en cada tabla
sql = 'INSERT INTO actors(id, first_name, last_name)VALUES(%s,%s,%s)'
cur.executemany(sql, tuplaActors)
mydb.commit()

sql = 'INSERT INTO directors(id, first_name, last_name)VALUES(%s,%s,%s)'
cur.executemany(sql, tuplaDirectors)
mydb.commit()

sql = 'INSERT INTO movies(id, name, year, ranking)VALUES(%s,%s,%s,%s)'
cur.executemany(sql, tuplaMovies)
mydb.commit()

sql = 'INSERT INTO movies_actors(actor_id, movie_id, role)VALUES(%s,%s,%s)'
cur.executemany(sql, tuplaMoviesActors)
mydb.commit()

sql = 'INSERT INTO movies_directors(director_id, movie_id)VALUES(%s,%s)'
cur.executemany(sql, tuplaMoviesDirectors)
mydb.commit()