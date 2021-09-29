import mysql.connector as db

# a) Crear conexión a MySQL
mydb = db.connect(
    host="localhost",
    port = "8889",
    user="root",
    passwd="root",
    database="InfoAeropuertos"
)

# b) Crear cursor
cur = mydb.cursor()

# c) Agregar datos a la tabla
cur.execute("INSERT INTO Aeropuertos(id, ident, type, name, elevation_ft, municipality, iata_code, score)VALUES('39340','SHCC','heliport','Clínica Las Condes Heliport','2461','Santiago','','25');")
cur.execute("INSERT INTO Aeropuertos(id, ident, type, name, elevation_ft, municipality, iata_code, score)VALUES('39379','SHMA','heliport','Clínica Santa María Heliport','2028','Santiago','','25');")
cur.execute("INSERT INTO Aeropuertos(id, ident, type, name, elevation_ft, municipality, iata_code, score)VALUES('39390','SHPT','heliport','Portillo Heliport','9000','Los Andes','','25');")
mydb.commit()

cur.execute("SELECT name as Nombre, type as Tipo, municipality as Municipalidad, elevation_ft as Altura FROM InfoAeropuertos.Aeropuertos WHERE elevation_ft > 5000")
for d in cur:
    print(d)