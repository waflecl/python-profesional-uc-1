import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient("mongodb://54.225.146.220:27017/")

db = client['alumnos']

print(db.list_collection_names())

coleccion = db['perfil']
usuario = {"_id":"165573129", "nombre":"Daniel", "apellido":"Henríquezz"}
coleccion.insert_one(usuario)
for x in db.perfil.find({"nombre":"Daniel"}):
    print(x['nombre'] + " " + x['apellido'])