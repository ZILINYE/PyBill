from pymongo import MongoClient


class Mongo:
    def __init__(self, databasename, collectionname, savelist=None,select_period=None):
        mongo_client = MongoClient("<IP Address>", 27017)
        db = mongo_client[databasename]
        self.collection = db[collectionname]
        self.savelist = savelist
        self.select_period = select_period


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

    def recordMongo(self):
        mongolist = []
        key_list = ['Name','Cate','Date','Spend','Description']
        for items in self.savelist:
            dic = {}
            for item in items:
                
                title_index = items.index(item)
                # if title_index ==3:
                #     item = int(item)
                title = key_list[title_index]
                dic.update({title:item})
            dic.update({'Period':self.select_period })
            mongolist.append(dic)
        try:
            if len(mongolist) > 0:
                x = self.collection.find_one({'Period':self.select_period })
                if x is not None:
                    
                    self.collection.delete_many({'Period':self.select_period })
                    self.collection.insert_many(mongolist)
                else:
                    self.collection.insert_many(mongolist)
            else:
                self.collection.delete_many({'Period':self.select_period })

        except EOFError as e:
            print(e)
                



    def recordUi(self):
        mongodata = self.collection.find({'Period':self.select_period })
        level2 = []
        for items in mongodata:
            level1 = []
            for i in range(1,len(items)-1):
                level1.append(list(items.values())[i])
            
            level2.append(level1)
        return level2
