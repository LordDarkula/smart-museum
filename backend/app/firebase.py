import os
import pyrebase

from dotenv import load_dotenv
load_dotenv()

PROJECT_ID = os.environ.get("FIREBASE_PROJECT_ID", "no-project-id-found")
API_KEY = os.environ.get("FIREBASE_API_KEY", "no-api-key-found")

print(PROJECT_ID)
print(API_KEY)
config = {
    "apiKey": API_KEY,
    "authDomain": "{}.firebaseapp.com".format(PROJECT_ID),
    "databaseURL": "https://{}.firebaseio.com".format(PROJECT_ID),
    "storageBucket": "{}.appspot.com".format(PROJECT_ID),
    "serviceAccount": "smart-museum-3a325-firebase-adminsdk-4ge8x-0581f69440.json"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()
museum = db.child("test_data").child("S6DL7mIZ767UWNYw1B0N").child("name").get()
museum = db.child("db").get()
print(museum.val())
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
