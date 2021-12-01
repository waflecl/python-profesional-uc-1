import pymongo
import requests
url = "mongodb://54.225.146.220:27017"
cli = pymongo.MongoClient(url, username='mongouc', password='m0ng0uc')
db = cli.feriadosdb
col = db.feriados2020
url_api = "https://apis.digital.gob.cl/fl/feriados/2020"
data = requests.get(url_api, headers={ "User-Agent" : "MiniProyecto 3", "Accept" : "application/json"})
col.insert_many(data.json())

print('===== Todos los Feriados de 2020 =====')
for x in col.find({},{'_id':0}):
  print("El día de " + x['nombre'] + " es un feriado de tipo " + x['tipo'] + " y se celebra el " + x['fecha'])

print('===== Solo los Feriados Civiles de 2020 =====')
for x in col.find({'tipo':'Civil'}):
  print("El día de " + x['nombre'] + " es un feriado de tipo " + x['tipo'] + " y se celebra el " + x['fecha'])

print('===== Solo los Feriados Irrenunciables de 2020 =====')
for x in col.find({'irrenunciable':'1'}):
  print("El día de " + x['nombre'] + " es un feriado de tipo " + x['tipo'] + " y se celebra el " + x['fecha'])

print('===== Solo los Feriados que incluyen "Santo" o "Santos" =====')
for x in col.find({'nombre': {'$regex' : '\w*Santo\w*'}}):
  print("El día de " + x['nombre'] + " es un feriado de tipo " + x['tipo'] + " y se celebra el " + x['fecha'])

print('===== Leyes relacionadas con el Plebiscito de Abril =====')
print('Las leyes involucradas en el día del Plebiscito Constitucional son las siguientes:')
leyes = col.find_one({'nombre': 'Plebiscito Constitucional'})
for ley in leyes['leyes']:
  print(ley['nombre'] + " Revisar en: " + ley['url'])