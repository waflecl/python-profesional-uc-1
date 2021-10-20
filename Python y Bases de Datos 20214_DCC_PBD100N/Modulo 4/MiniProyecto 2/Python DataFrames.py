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

# Lista de películas, el año, su director y el puntaje (rank) solo para las películas con rank mayor a 8 ordenadas en forma decreciente
cur.execute("SELECT m.name as 'Movie', m.year AS 'Year', d.last_name AS 'Director', m.rank as 'Rank' FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id) JOIN directors AS d ON d.id = director_id WHERE m.rank > 8 ORDER BY m.rank DESC;")
rows = cur.fetchall()
print("== Consulta 3.3 ==")
for d in rows:
    print(d)