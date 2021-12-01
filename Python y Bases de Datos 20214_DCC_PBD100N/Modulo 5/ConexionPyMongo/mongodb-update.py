import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient("mongodb://54.225.146.220:27017/")

db = client['alumnos']

db.perfil.find_one_and_update({"_id":"165573129"}, { '$set' : {"apellido": "Henriquez Sandoval"}})