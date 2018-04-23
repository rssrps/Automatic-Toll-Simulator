import sqlite3
import datetime

ratelist = {"car":200 , "bus":400 , "truck": 600}

def insertUser(fnm,lnm,car,cont,bal,vtp):
  con = sqlite3.connect("MainDatabase.db")
  con.execute("create table if not exists users(fname varchar(30),lname varchar(30),carNumber varchar(30),contact int,balance int,vehicleType varchar(30))")  
  con.execute("""insert into users(fname,lname,carNumber,contact,balance,vehicleType) values('%s','%s','%s','%s','%s','%s')""" % (fnm,lnm,car,cont,bal,vtp))
  con.commit()

def registerAdmin(unm,pwd):
  con = sqlite3.connect("MainDatabase.db")
  con.execute("create table if not exists admin(username varchar(30),password varchar(30))")
  con.execute("""insert into admin(username,password) values('%s','%s') """ % (unm,pwd))
  con.commit()

def authenticateUser(unm,pwd):
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from admin")
   result = cur.fetchall()
   for line in result:
     if(line[0]==unm):
       if(line[1]==pwd): 
         return 1;
       else :
         return 0
   return -1

def deleteThisUser(carnm):
  con = sqlite3.connect("MainDatabase.db")
  flag = 0
  cur = con.cursor()
  cur.execute("select * from users")
  result = cur.fetchall()
  for line in result:
    if(line[2] == carnm):
      flag = 1
  if(flag==1):
   con.execute(''' delete from users where carNumber = '%s' ''' % (carnm))
   print "Vehicle deleted"
   con.commit()
   return 1
  else:
   print "This vehicle does not exist!"
   return 0

def getAdminList():
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from admin")
   result = cur.fetchall()
   return result

def getUserList():
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from users")
   result = cur.fetchall()
   return result

def getHistoryList():
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from history")
   result = cur.fetchall()
   return result

def getVehicleType(vno):
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from users")
   result = cur.fetchall()
   for line in result:
     if(line[2]==vno):
        print "Match found!"
        return line[5]
   return 0

def updateDict():
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from rates")
   result = cur.fetchall()
   for line in result:
     ratelist["car"] = int(line[0])
     ratelist["bus"] = int(line[1])
     ratelist["truck"] = int(line[2])

def updateBalance(vno,vtp):
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from users")
   result = cur.fetchall()
   for line in result:
     if(line[2]==vno):
       curBal = line[4]

   updateDict()
   
   if(curBal<ratelist[vtp]): 
     print "Insufficient Balance"
     return 0
   else:
     newBal = curBal - ratelist[vtp]
     con.execute("""update users set balance = '%s' where carNumber = '%s' """ % (newBal,vno))
     con.commit()
     print "Amount deducted"
     return 1 

def addBalDB(vno,amount):
   con = sqlite3.connect("MainDatabase.db")
   cur = con.cursor()
   cur.execute("select * from users")
   result = cur.fetchall()
   flag=0
   for line in result:
     if(line[2]==vno):
       curBal = line[4]
       flag=1
   
   if(flag==0): 
     print "Vehicle not found!"
   else:
     newBal = curBal + int(amount)
     con.execute("""update users set balance = '%s' where carNumber = '%s' """ % (newBal,vno))
     con.commit()
     print "Amount added!"
     return 1

   return 0

def updateHistory(vno,vtype,x):
  con = sqlite3.connect("MainDatabase.db")
  con.execute("create table if not exists history(vno varchar(30),vtp varchar(30),date varchar(40),time varchar(40),comment varchar(200))")
  
  if(x==0):
   comment = "Cash collected"
  else:
   comment = "Balance deducted successfully"

  date = str(datetime.datetime.today().strftime('%d-%m-%Y'))
  time = str(datetime.datetime.now().time().strftime('%H:%M:%S'))
 
  con.execute(""" insert into history(vno,vtp,date,time,comment) values('%s','%s','%s','%s','%s') """ % (vno,vtype,date,time,comment))  
  con.commit()

def updateToDB(c,b,t): 
   con = sqlite3.connect("MainDatabase.db")
   con.execute("create table if not exists rates(car int,bus int,truck int)")
   cur = con.cursor()
   cur.execute("select * from rates")
   result = cur.fetchall()
   for line in result:
     car    = line[0]
     bus    = line[1]
     truck  = line[2]

   if(len(c)!=0):
     car = int(c)
   if(len(b)!=0):
     bus = int(b)
   if(len(t)!=0):
     truck = int(t)

   con.execute("""update rates set car   = '%s'""" % (car))
   con.execute("""update rates set bus   = '%s'""" % (bus))
   con.execute("""update rates set truck = '%s'""" % (truck))

   print "Rates updates successfully!"
   con.commit()
   return 1


    
   
   
   

  

  
       
   
   
   
   
       
  






