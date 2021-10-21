# Import de librerias a utilizar
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

# Query Lista de directores que tienen más de 3 películas ordenadas en orden decreciente
cur.execute("SELECT d.last_name, d.first_name, COUNT(movie_id) AS 'How Many' FROM movies_directors AS md JOIN directors AS d ON d.id = md.director_id GROUP by d.last_name, d.first_name HAVING COUNT(movie_id) > 3 ORDER BY COUNT(movie_id) DESC;")
rows = cur.fetchall()
print("== Consulta 3.1 ==")
for d in rows:
    print(d)

# Ranking de actores y se despliega la cuenta de películas para todos ordenados por apellido
cur.execute("SELECT a.last_name, a.first_name, COUNT(movie_id) FROM actors AS a JOIN movies_actors as ma on ma.actor_id = a.id GROUP BY a.last_name, a.first_name ORDER BY a.last_name, a.first_name;")
rows = cur.fetchall()
print("")
print("== Consulta 3.2 ==")
for d in rows:
    print(d)

# Lista de películas, el año, su director y el puntaje (rank) solo para las películas con rank mayor a 8 ordenadas en forma decreciente
cur.execute("SELECT m.name as 'Movie', m.year AS 'Year', d.last_name AS 'Director', m.rank as 'Rank' FROM (movies_directors AS md JOIN movies as m on m.id = md.movie_id) JOIN directors AS d ON d.id = director_id WHERE m.rank > 8 ORDER BY m.rank DESC;")
rows = cur.fetchall()
print("")
print("== Consulta 3.3 ==")
for d in rows:
    print(d)