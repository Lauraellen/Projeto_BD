import pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://root:PmlpZvVhk4LQpdD0@cluster0.uao55dy.mongodb.net/test"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True  # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
        except Exception as e:
            print(e)

    def resetDatabase(self):
        self.db.drop_collection(self.collection)