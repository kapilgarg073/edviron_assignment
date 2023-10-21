import json
import pymongo
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://assignment:edviron@cluster1.focovdw.mongodb.net/"

def lambda_handler(event, context):
    try:
        client = MongoClient(MONGODB_URI)

        db = client.get_default_database()

        collections = db.list_collection_names()

        for collection_name in collections:
            collection = db[collection_name]

            defaulters = list(collection.find({"dueDate": {"$lt": "2023/10/01"}}))

        return {
            'statusCode': 200,
            'body': json.dumps(defaulters)
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
