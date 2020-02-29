import os
import json
from . import firestore
from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def hello_world():
    return os.environ.get("FIREBASE_API_KEY", "help")

@app.route('/all')
def all():
    db = firestore.MuseumDB()
    return json.dumps(db.fetch_data())

@app.route('/start/<museum>/<collection>')
def start(museum, collection):
    if os.path.exists():
        shutil.rmtree(images)
    os.makedirs('images')
    images = firestore.fetch_images(
    return "Museum {}, collection {}".format(escape(museum), escape(collection))
