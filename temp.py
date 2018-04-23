import sqlite3
con = sqlite3.connect("MainDatabase.db")


def printData():
  cur = con.cursor()
  cur.execute("select * from rates")
  result = cur.fetchall()
  print result

con.execute("delete from history")
con.commit()

#printData()
'''
con.execute("create table if not exists rates(car int,bus int,truck int)")
con.execute(""" insert into rates(car,bus,truck) values(200,400,600) """) 
con.commit()'''
#printData()


