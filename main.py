from db.db import Database
class AulaDB:
    def __init__(self):
        self.db = Database(database="teste", collection="teste")
        # self.db.resetDatabase()
        self.collection = self.db.collection

    def getClasses(self):
        res = self.collection.find()
        allClasses = []
        for aula in res:
            allClasses.append(aula)
        return allClasses

aula = AulaDB;

aula.getClasses()
