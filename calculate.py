import pymongo

class Calculator:
    def __init__(self,selected_period):
        self.selected_period = selected_period
        mongo_client = MongoClient("192.168.2.60", 27017)
        db = mongo_client['pybill']
        self.record = db['BillRecord']
        self.cate = db['Category']
        self.person = db['Person']
        self.personlist = []
        self.catelist =[]
        self.init_cate()
        self.init_person()
        self.allpersonCost = {}
        self.cateCost = {}

        self.borrow = {}
        self.owe = {}

     

    def init_person(self):
        datalist = self.person.find()

        for item in datalist:
            self.personlist.append(item["name"])

    def init_cate(self):
        datalist = self.cate.find()
        for item in datalist:
            self.catelist.append(item["name"])
    


    def BasicCalculate(self,filtername,valname):
        agr = [ {'$match':{'$and':[{'Period':'August/2020'},{filtername:valname}]}},{'$group': {'_id': 1, 'all': { '$sum': '$Spend' } } } ]
        val = list(self.record.aggregate(agr))

        return val[0]['all']

    def GetPerpersonCost(self):
        for item in self.person:
            x = self.BasicCalculate(filtername='Name',valname=item)
            self.allpersonCost[item]=x
    
    
    def GetPerCateCost(self):
        for item in self.cate:
            x = self.BasicCalculate(filtername='Cate',valname=item)
            self.cateCost[item]=x
 

    def seperate(self):
        for key,value in self.allpersonCost.items():
            if value > 0:
                self.borrow[key] = value
            else:
                self.owe[key] = value


    def CostSolution(self):

        dic1 = {k: v for k, v in sorted(self.borrow.items(), key=lambda item: item[1],reverse=True)}
        dic2 = {k: v for k, v in sorted(self.owe.items(), key=lambda item: item[1],reverse=True)}
        list1k = list(dic1.keys())# owe
        list1v = list(dic1.values())
        list2k = list(dic2.keys())#borrow
        list2v = list(dic2.values())    
        for i in range(len(list1v)):
            for y in range(len(list2v)):
                if(list2v[y] != 0):
                    t = list1v[i]  - list2v[y]
                    if t > 0:
                        list1v[i] = t                               
                        print('Owe'+list1k[i]+' owe  Borrow'+list2k[y]+' '+str(list2v[y]))
                        list2v[y] = 0

                    elif t == 0:
                        print('Owe'+list1k[i]+' owe  Borrow'+list2k[y]+' '+str(list2v[y]))
                        list2v[y] = 0
                        break

                    
                    else:
                        list2v[y] = -t
                        print('Owe'+list1k[i]+' owe  Borrow'+list2k[y]+' '+str(list1v[i]))
                        break