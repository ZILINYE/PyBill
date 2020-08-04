from pymongo import MongoClient

mongo_client = MongoClient("192.168.2.60", 27017)
db = mongo_client['pybill']
collection = db['BillRecord']

agr = [ {'$match':{'$and':[{'Period':'August/2020'},{'Name':'test'}]}},{'$group': {'_id': 1, 'all': { '$sum': '$Spend' } } } ]
val = list(collection.aggregate(agr))

print(val)