from pymongo import MongoClient
from abc import abstractmethod,ABCMeta
from loadconf import Conf
import sqlite3

class MakeConnection:
    def __init__(self):
        config_data = Conf()
        data = config_data.Get_config()
        stype = data['RecordType']
        mongo_ip = data['mongo']['ServerIP']
        dbname = data['mongo']['DBName']
        username = data['mongo']['Username']
        password = data['mongo']['Password']
        sql_file = data['sqlite']['FileName']
        sql_db = data['sqlite']['DBName']
 
        try:
            if stype == 'sqlite':
                    
                    self.conn = sqlite3.connect(sql_file)
                    
                    self.cur = self.conn.cursor()
            else:
            
                    mongo_client = MongoClient(mongo_ip,27017)
                    self.db = mongo_client[dbname]

        except:
            print("Cannot make connection with Database")

        


class Mongo(MakeConnection,metaclass = ABCMeta):
    def __init__(self, collectionname, savelist=None,select_period=None):

        
        MakeConnection.__init__(self)
        self.collection = self.db[collectionname]

        self.savelist = savelist
        self.select_period = select_period


    def Ui_Selec_Mongo(self):
        formatted = list(map(lambda x: {"name": x}, self.savelist))
        try:
            if formatted is not None:
                self.collection.drop()
                x = self.collection.insert_many(formatted)
        except EOFError as e:
            print(e)

    def Mongo_Selec_Ui(self):
        datalist = self.collection.find()
        uilist = []
        for item in datalist:
            uilist.append(item["name"])
        return uilist

    def Ui_Record_Mongo(self):
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
                



    def Mongo_Record_Ui(self):
        mongodata = self.collection.find({'Period':self.select_period })
        level2 = []
        for items in mongodata:
            
            level1 = []
            for i in range(1,len(items)-1):
                level1.append(list(items.values())[i])
            
            level2.append(level1)
     
        return level2

class Sqlite(MakeConnection,metaclass = ABCMeta):
    def __init__(self, collectionname, savelist=None,select_period=None):
        MakeConnection.__init__(self)
        self.table = collectionname
        self.savelist = savelist
        self.select_period = select_period
        self.tablelist = {'Category': 'Category(cate_id,cate_name)', 'Person': 'Person(person_id,person_name)',
                          'OweRecord': 'OweRecord(owe_id,Name,Cate,Date,Spend,Description,Period)', 'BillRecord': 'BillRecord(bill_id,Name,Cate,Date,Spend,Description,Period)'}
        self.tablelistUi = {'Category':'cate_name','Person':'person_name'}

    def Ui_Selec_Sql(self):
        formatted = list(map(lambda x: (None, x), self.savelist))
        try:
            if formatted is not None:
                dele = "DELETE FROM "+self.table
                insert = "INSERT INTO "+self.tablelist[self.table]+" VALUES(?,?)"
                self.cur.execute(dele)
                self.cur.executemany(insert,formatted)
                self.conn.commit()
        except EOFError as e:
            print(e)

    def Sql_Selec_Ui(self):
        datalist = self.cur.execute("Select "+self.tablelistUi[self.table]+" from "+self.table)
        uilist = []
        for item in datalist:
            uilist.append(item[0])
        return uilist

    def Ui_Record_Sql(self):
        mongolist = []
        for items in self.savelist:
            items.insert(0,None)
            items.append(self.select_period)           
            mongolist.append(tuple(items))
        try:
            if len(mongolist) > 0:
                x = self.cur.execute("SELECT * FROM "+self.table+" WHERE Period= '"+self.select_period+"' ")
                if x is not None:
                    
                    self.cur.execute("DELETE  FROM "+self.table+" WHERE Period= '"+self.select_period+"' ")
                    self.cur.executemany("INSERT INTO "+self.tablelist[self.table]+" VALUES (?,?,?,?,?,?,?)",mongolist)
                else:
                    self.cur.executemany("INSERT INTO "+self.tablelist[self.table]+" VALUES (?,?,?,?,?,?,?)",mongolist)
            else:
                    self.cur.execute("DELETE  FROM "+self.table+" WHERE Period= '"+self.select_period+"' ")

            self.conn.commit()
        except EOFError as e:
            print(e)
                



    def Sql_Record_Ui(self):
        print(self.select_period)

        mongodata = self.cur.execute("SELECT * FROM "+self.table+" WHERE Period = '"+self.select_period+"' ") 

        level2 = []
        for items in mongodata:
            level1 = []
            for i in range(1,len(items)):
                level1.append(items[i])
            
            level2.append(level1)
        return level2
class Storage(Mongo,Sqlite):
    def __init__(self,collectionname, savelist=None,select_period=None):
        config_data = Conf()
        data = config_data.Get_config()
        self.sType = data['RecordType']
        if self.sType == 'mongo':

            Mongo.__init__(self,collectionname, savelist,select_period)
        else:

            Sqlite.__init__(self,collectionname, savelist,select_period)

        


    def Record_DB(self):
        if self.sType == 'mongo':
            return self.Ui_Record_Mongo()
        else:
            return self.Ui_Record_Sql()
    def Record_Ui(self):
        if self.sType == 'mongo':
            return self.Mongo_Record_Ui()
  
        else:
            return self.Sql_Record_Ui()
    def Selec_DB(self):
        if self.sType == 'mongo':
            return self.Ui_Selec_Mongo()
        else:
            return self.Ui_Selec_Sql()
    def Selec_Ui(self):
        if self.sType == 'mongo':
            return self.Mongo_Selec_Ui()
        else:
            return self.Sql_Selec_Ui()