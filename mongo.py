from pymongo import MongoClient


class Mongo:
    def __init__(self, databasename, collectionname, savelist=None):
        mongo_client = MongoClient("192.168.2.60", 27017)
        db = mongo_client[databasename]
        self.collection = db[collectionname]
        self.savelist = savelist

    def selectionMongo(self):
        formatted = list(map(lambda x: {"name": x}, self.savelist))
        try:
            if formatted is not None:
                self.collection.drop()
                x = self.collection.insert_many(formatted)
        except EOFError as e:
            print(e)

    def selectionUi(self):
        datalist = self.collection.find()
        uilist = []
        for item in datalist:
            uilist.append(item["name"])
        return uilist

    # def recordMongo(self):

    # def recordUi(self):
