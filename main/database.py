import sqlite3

class Connector():
    def __init__(self,table):
        self.conn = sqlite3.connect('G:\Программы\SQLiteStudio\db01.db')
        self.cursor = self.conn.cursor()
        self.table = table
    def insert(self,Name,Weight,Glass):
        self.cursor.execute('INSERT INTO '+ self.table + ' VALUES(?, ?, ?, NULL)',(Name,Weight,Glass))
        self.conn.commit()
    def insertID(self,thing_id,place_id,category):
        self.cursor.execute('INSERT INTO Car_info VALUES(?, ?, ?)',(thing_id,place_id,category))
        self.conn.commit()
    def selectAll(self):
        self.cursor.execute('SELECT * FROM '+ self.table)
        results = self.cursor.fetchall()
        print(results)
        self.conn.commit()
    def returnID(self):
        self.cursor.execute('SELECT ID FROM Everything ORDER BY ID ASC')
        ID_thing = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.execute('SELECT ID FROM Place ORDER BY ID ASC')
        ID_place = self.cursor.fetchall()
        self.conn.commit()
        list = (ID_thing,ID_place)
        return list
    def deleteAll(self):
        self.cursor.execute('DELETE FROM '+ self.table)
        self.conn.commit()
    def close(self):
        self.conn.close()
    def returnAll(self):
        self.cursor.execute('SELECT * FROM Everything JOIN Car_info ON Everything.ID = Car_info.thing_id JOIN Place ON Place.ID = Car_info.place_id')
        results = self.cursor.fetchall()
        self.conn.commit()
        return results
'''
everything = Connector('Everything')
everything.deleteAll()
everything.insert('sofa','30','0')
everything.insert('mixer','3','0')
everything.selectAll()

place = Connector('Place')
place.deleteAll()
place.insert('Kulakova 22','Severnaya 6','6')
place.insert('Pavlova 16','Kalinina 22','12')
place.selectAll()
car_info = place.returnID()

car_info = Connector('Car_info')
car_info.deleteAll()
list_id = car_info.returnID()
car_info.insertID(str(list_id[0][-1][-1]),str(list_id[1][-1][-1]),'econom')
car_info.selectAll()

data = car_info.returnAll()

print(data[-1])

minidom.updateXML(data[-1])
l = minidom.readXML()
print(l)
'''
