import os
import shutil
import json
from . import firestore
from .image_ops import utils
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
    if os.path.exists('images'):
        shutil.rmtree('images')
    os.makedirs('images')
    db = firestore.MuseumDB()
    images = db.fetch_images(museum, collection)
    for key, val in images.items():
        utils.download_image_with_url(val, os.path.join('images', key))

    with open('image_data.json', 'w') as fp:
            json.dump(images, fp)
    return "Museum {}, collection {}".format(escape(museum), escape(collection))
