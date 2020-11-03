from abc import abstractmethod, ABCMeta
from loadconf import Conf
from datachan import MakeConnection


def CostSolution(owedata,allpersonCost,personlist):

    solutionList = []
    borrow = {}
    owe = {}
    total_cost = 0
    avagcost = 0
  
    for item in owedata:
        try: 
            solutionList.append(
            [item['Name'], item['Cate'], item['Spend']])
        except:

            solutionList.append(
            [list(item)[1], list(item)[2], list(item)[4]])
    # Calculate Total Cost and Avg Cost        
    for key, value in allpersonCost.items():
        total_cost += value
    avagcost = total_cost / len(personlist)
    # Seperate per-person cost
    for key, value in allpersonCost.items():
        t = value - avagcost
        if t > 0:
            borrow[key] = t
        else:
            owe[key] = -t
    dic1 = {k: v for k, v in sorted(
        owe.items(), key=lambda item: item[1], reverse=True)}
    dic2 = {k: v for k, v in sorted(
        borrow.items(), key=lambda item: item[1], reverse=True)}
    list1k = list(dic1.keys())  # owe
    list1v = list(dic1.values())
    list2k = list(dic2.keys())  # borrow
    list2v = list(dic2.values())
    for i in range(len(list1v)):
        for y in range(len(list2v)):
            if(list2v[y] != 0):
                t = list1v[i] - list2v[y]
                if t > 0:
                    list1v[i] = t
                    solutionList.append(
                        [list1k[i], list2k[y], str(round(list2v[y], 1))])
                    list2v[y] = 0

                elif t == 0:
                    solutionList.append(
                        [list1k[i], list2k[y], str(round(list2v[y], 1))])
                    list2v[y] = 0
                    break

                else:
                    list2v[y] = -t
                    solutionList.append(
                        [list1k[i], list2k[y], str(round(list1v[i], 1))])
                    break
    i = 0
    while i < len(solutionList):
        y = i + 1
        while y < len(solutionList):
            if solutionList[i][0] == solutionList[y][0] and solutionList[i][1] == solutionList[y][1]:
                total = float(
                    solutionList[i][2])+float(solutionList[y][2])
                owe = solutionList[i][0]
                borrow = solutionList[i][1]

                solutionList[i][2] = str(total)
                del solutionList[y]
            elif solutionList[i][0] == solutionList[y][1] and solutionList[i][1] == solutionList[y][0]:
                new = float(solutionList[i][2]) - \
                    float(solutionList[y][2])
                if new > 0:
                    solutionList[i][2] = str(new)
                elif new < 0:
                    solutionList[i][0] = solutionList[y][1]
                    solutionList[i][1] = solutionList[y][0]
                    solutionList[i][2] = str(-new)
                else:
                    del solutionList[i]
                    y -= 1

                del solutionList[y]
            else:
                y += 1

        i += 1
    return total_cost, round(avagcost, 2), solutionList

class MongoCalculate(MakeConnection):
    def __init__(self, selected_period):
        MakeConnection.__init__(self)
        self.selected_period = selected_period
        self.record = self.db['BillRecord']
        self.cate = self.db['Category']
        self.person = self.db['Person']
        self.owerecord = self.db['OweRecord']

        self.personlist = []
        self.catelist = []
        self.allpersonCost = {}
        self.cateCost = {}

        self.init_list()
        self.MGetPerCost()

    def init_list(self):
        catelist = self.cate.find()
        personlist = self.person.find()
        for item in catelist:
            self.catelist.append(item["name"])
        for item in personlist:
            self.personlist.append(item["name"])

    def MBasicCalculate(self, filtername, valname):
        agr = [{'$match': {'$and': [{'Period': self.selected_period}, {
            filtername: valname}]}}, {'$group': {'_id': 1, 'all': {'$sum': '$Spend'}}}]
        val = list(self.record.aggregate(agr))
        if len(val) > 0:
            return val[0]['all']
        else:
            return 0

    def MGetPerCost(self):
        for item in self.personlist:
            x = self.MBasicCalculate(filtername='Name', valname=item)
            self.allpersonCost[item] = x
        for item in self.catelist:
            x = self.MBasicCalculate(filtername='Cate', valname=item)

            self.cateCost[item] = x

    def returnDataMongo(self):
        owedata= self.owerecord.find({'Period': self.selected_period})
        total_cost, avagcost, solutionList = CostSolution(owedata,self.allpersonCost,self.personlist)
        return total_cost, avagcost, self.allpersonCost,self.cateCost,solutionList


class SqliteCalculate(MakeConnection):
    def __init__(self, selected_period):
        MakeConnection.__init__(self)

        self.selected_period = selected_period
        self.cate = self.cur.execute("SELECT cate_name FROM Category ").fetchall()
        self.person = self.cur.execute("SELECT person_name FROM Person ").fetchall()
        self.owerecord = list(self.cur.execute("SELECT * FROM OweRecord WHERE Period= '"+self.selected_period+"' ").fetchall())


        self.allpersonCost = {}
        self.cateCost = {}


        self.SGetPerCost()

    def SBasicCalculate(self, filtername, valname) -> float:
        val =self.cur.execute("Select sum(Spend) from BillRecord WHERE Period ='"+self.selected_period+"' and "+filtername+" = '"+valname+"'").fetchall()  

        if val[0][0] != None:
            return val[0][0]
        else:
            return 0

    def SGetPerCost(self):
        for item in self.person:
            x = self.SBasicCalculate(filtername='Name', valname=item[0])     
            self.allpersonCost[item[0]] = x
        for item in self.cate:
            x = self.SBasicCalculate(filtername='Cate', valname=item[0])
            self.cateCost[item[0]] = x
     
    def returnDataSql(self):
        
        formatted_owe_list = []
        for item in self.owerecord:
            formatted_owe = {}
            formatted_owe['Name'] = list(item)[1]
            formatted_owe['Cate'] = list(item)[2]
            formatted_owe['Spend'] = list(item)[4]
            formatted_owe_list.append(formatted_owe)
        formatted_person_list = []
        for item in self.person:
            formatted_person_list.append(item[0])
        total_cost, avagcost, solutionList = CostSolution(formatted_owe_list,self.allpersonCost,self.person)
        return total_cost, avagcost, self.allpersonCost,self.cateCost,solutionList




        


class Calculator(MongoCalculate,SqliteCalculate):
    def __init__(self, select_period):
        config_data = Conf()
        data = config_data.Get_config()
        self.sType = data['RecordType']
        if self.sType == 'mongo':

            MongoCalculate.__init__(self, select_period)
        else:

            SqliteCalculate.__init__(self, select_period)

    def returnData(self):
        if self.sType == 'mongo':
            return self.returnDataMongo()
        else:
            return self.returnDataSql()
