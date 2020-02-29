import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return os.environ.get("FIREBASE_API_KEY", "help")

