import pyrebase

PROJECT_ID = "smart-museum-3a325"
config = {
    "apiKey": "apiKey",
    "authDomain": "{}.firebaseapp.com".format(PROJECT_ID),
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "{}.appspot.com".format(PROJECT_ID)
}

firebase = pyrebase.initialize_app(config)
