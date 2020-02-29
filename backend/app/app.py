import os
import json
from . import firestore
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return os.environ.get("FIREBASE_API_KEY", "help")

@app.route('/all')
def all():
    db = firestore.MuseumDB()
    return json.dumps(db.fetch_data())
