from pymongo import MongoClient

mongo_client = MongoClient("192.168.2.60", 27017)
db = mongo_client['pybill']
coll = db['BillRecord']
x = coll.find({'Period':"October/2020" })
for item in x:

    print(item)
