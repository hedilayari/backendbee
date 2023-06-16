import pymongo
import requests
import time

# connexion à la base de données MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://work:work@cluster0.sbwnosv.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]
collection = db["iot"]

# boucle while infinie pour récupérer et insérer les données en temps réel
while True:
    # récupération des données de ThingSpeak
    url = "https://api.thingspeak.com/channels/2146934/feeds.json?api_key=5UZ3FXRAXRYM20O8"
    response = requests.get(url)
    data = response.json()

    # insertion des données dans MongoDB
    for feed in data["feeds"]:
        doc = {
            "timestamp": feed["created_at"],
            "temp": feed["field1"],
            "hum": feed["field2"],
            "poid": feed["field3"],
            "latitude": feed["field4"],
            "longitude": feed["field5"],
            # ajoutez autant de champs que nécessaire
        }
        collection.insert_one(doc)

    # attendre 50 secondes avant de récupérer les nouvelles données
    time.sleep(90)
