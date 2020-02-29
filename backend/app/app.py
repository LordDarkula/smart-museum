from os import listdir
from os.path import isfile, join
import os
import shutil
import json
from . import firestore
from .image_ops import utils
from flask import Flask
from flask_cors import CORS, cross_origin
from markupsafe import escape
from flask import jsonify
from flask import send_file


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return os.environ.get("FIREBASE_API_KEY", "help")


@app.route('/all')
def all():
    db = firestore.MuseumDB()
    return jsonify(db.fetch_data())


@app.route('/image')
def image():
    onlyfiles = [f for f in listdir(mypath) if isfile(join('current', f))]
    return send_file(onlyfiles[0])


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

    if os.path.exists('current'):
        shutil.rmtree('current')
    os.makedirs('current')
    shutil.copyfile(os.path.join('images', 'image1.jpg'),
                    os.path.join('current', 'image1.jpg'))
    with open('current.txt', 'w') as f:
        f.write('image1')

    return "Museum {}, collection {}".format(escape(museum), escape(collection))


# @app.route('/update/<direction>')
# def update(direction):
#     if not os.path.exists('visited.json'):
#         with open('visited.json', 'w') as f:
#             json.dump({}, f)

#     with open('visited.json', 'r') as f:
#         visited = json.load(f)

#         with open('current.txt') as f:
#             current_name = f.readline()
#             with open('image_data.json', 'r') as f:
#                 image_data = json.load(f)

#                 for key, val in image_data:
#                     if key == current or key in visited:
#                         continue

#             for key, val in image_data:
