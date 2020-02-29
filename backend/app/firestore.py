from google.cloud import firestore

class MuseumDB:


    def __init__(self):
        self.db = firestore.Client()

    def fetch_data(self):
        data_ref = self.db.collection(u'test_data')
        return {'test_data': [doc.get().to_dict() for doc in data_ref.list_documents()]}

db = MuseumDB()
db.fetch_data()
