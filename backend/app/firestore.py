from google.cloud import firestore

DATA = u'mark_data'


class MuseumDB:

    def __init__(self):
        self.db = firestore.Client()

    def fetch_data(self):
        data_ref = self.db.collection(DATA)
        return {'test_data': [doc.get().to_dict() for doc in data_ref.list_documents()]}

    def fetch_images(self, museum, collection):
        print("Museum is " + museum)
        print("Collection is " + collection)
        museum_ref = self.db.collection(
            u'mark_data').where(u'name', u'==', museum)
        for m in museum_ref.stream():
            for col in m.to_dict()['collections']:
                if col['name'] == collection:
                    return col['images']


def import_json():
    db = firestore.Client()
    data_ref = db.collection(DATA)

    import json

    with open('MUSEUM.json') as f:
        d = json.load(f)
        print(d)
        print(type(d))
        for doc in d:
            data_ref.add(doc)
