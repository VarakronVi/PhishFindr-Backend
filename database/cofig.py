from pymongo.mongo_client import MongoClient
import certifi

uri = "mongodb+srv://homydoct:UE1k22VgG1oKV9Wg@cluster0.pk770ka.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client.phishfindr_test

collection = db['dangerous_link']
