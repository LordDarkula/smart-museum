from google.cloud import firestore

class MuseumDB:


    def __init__(self):
        self.db = firestore.Client()

    def fetch_data(self):
        data_ref = self.db.collection(u'test_data')
        return {'test_data': [doc.get().to_dict() for doc in data_ref.list_documents()]}

    def fetch_images(self, museum, collection):
        museum_ref = self.db.collection(u'test_data').where(u'name', u'==', museum)
        for m in museum_ref.stream():
            for col in m.to_dict()['collections']:
                if col['name'] == collection:
                    return col['images']

db = MuseumDB()
print(db.fetch_images('ATL High Museum', 'Photography'))
