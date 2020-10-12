from pymongo import MongoClient
from View.Report import Report_Ui
class Calculator:
    def __init__(self,selected_period):
        self.selected_period = selected_period
        mongo_client = MongoClient("192.168.2.60", 27017)
        db = mongo_client['pybill']
        self.record = db['BillRecord']
        self.cate = db['Category']
        self.person = db['Person']
        self.owerecord = db['OweRecord']
        self.personlist = []
        self.catelist =[]
        self.allpersonCost = {}
        self.cateCost = {}
        self.borrow = {}
        self.owe = {}
        self.total_cost = 0
        self.avagcost = 0
        self.solutionList = []
        self.init_cate()
        self.init_person()
        self.GetPerCateCost()
        self.GetPerpersonCost()
        self.seperate()
        self.OweRecord()
        self.CostSolution()

   
    def init_person(self):
        datalist = self.person.find()
        for item in datalist:
            self.personlist.append(item["name"])

    def init_cate(self):
        datalist = self.cate.find()
        for item in datalist:
            self.catelist.append(item["name"])
    

    def OweRecord(self):
        owe = self.owerecord.find({'Period':self.selected_period })
        for item in owe:
            self.solutionList.append([item['Name'],item['Cate'],item['Spend']])

    def BasicCalculate(self,filtername,valname):
        agr = [ {'$match':{'$and':[{'Period':self.selected_period},{filtername:valname}]}},{'$group': {'_id': 1, 'all': { '$sum': '$Spend' } } } ]
        val = list(self.record.aggregate(agr))
        if len(val) > 0:
            return val[0]['all']
        else:
            return 0

    def GetPerpersonCost(self):
        for item in self.personlist:
            x = self.BasicCalculate(filtername='Name',valname=item)
            self.allpersonCost[item]=x
    
    
    def GetPerCateCost(self):
        for item in self.catelist:
            x = self.BasicCalculate(filtername='Cate',valname=item)

            self.cateCost[item]=x
 

    def seperate(self):
        
        for key, value in self.allpersonCost.items():
            self.total_cost += value
        self.avagcost = self.total_cost / len(self.personlist)

        for key,value in self.allpersonCost.items():
            t = value - self.avagcost
            if t > 0:
                self.borrow[key] = t
            else:
                self.owe[key] = -t


    def CostSolution(self):

        dic1 = {k: v for k, v in sorted(self.owe.items(), key=lambda item: item[1],reverse=True)}
        dic2 = {k: v for k, v in sorted(self.borrow.items(), key=lambda item: item[1],reverse=True)}
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
                        self.solutionList.append([list1k[i],list2k[y],str(list2v[y])])                               
                        list2v[y] = 0

                    elif t == 0:
                        self.solutionList.append([list1k[i],list2k[y],str(list2v[y])])
                        list2v[y] = 0
                        break

                    
                    else:
                        list2v[y] = -t
                        self.solutionList.append([list1k[i],list2k[y],str(list1v[i])])
                        break
        i = 0
        while i < len(self.solutionList):
            y = i + 1 
            while y < len(self.solutionList):
                if self.solutionList[i][0]== self.solutionList[y][0] and self.solutionList[i][1] == self.solutionList[y][1]  :
                    total = float(self.solutionList[i][2])+float(self.solutionList[y][2])
                    owe = self.solutionList[i][0]
                    borrow = self.solutionList[i][1]
                    
                    self.solutionList[i][2] = str(total)
                    del self.solutionList[y]
                elif self.solutionList[i][0]== self.solutionList[y][1] and self.solutionList[i][1] == self.solutionList[y][0]  :
                    new = float(self.solutionList[i][2])-float(self.solutionList[y][2])
                    if new > 0:
                        self.solutionList[i][2] = str(new)
                    elif new < 0:
                        self.solutionList[i][0] = self.solutionList[y][1]
                        self.solutionList[i][1] = self.solutionList[y][0]
                        self.solutionList[i][2] = str(-new)
                    else:
                        del self.solutionList[i]
                        y -= 1
                    
                    del self.solutionList[y]
                else:
                    y+=1

                
            i+=1
        
    def returnData(self):
        return self.total_cost,self.avagcost,self.allpersonCost,self.cateCost,self.solutionList
