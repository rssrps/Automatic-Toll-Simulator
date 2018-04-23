import Tkinter as tk
from PIL import ImageTk, Image
from DBconnect import *
from imageProcess import *
from threading import Timer
from main import finishProject

# --------------------------------------------- Declerations -------------------------------------------------------------- 

LoginPage = None
RegisterPage = None
ThanksPage = None
ControlPage = None

usernameInput = None
passwordInput = None
confirmInput = None

loginUsername = None
loginPassword = None

insfnm = None
inslnm = None
inscar = None
inscon = None
insbal = None
insVeh = None

insU = None
delU = None

delcar = None

R1 = None
R2 = None
R3 = None

panel = None
vehImg = None

carAmount = None
amountEntry = None

imgCount = 1
xa = None

ya = None
carrate = None
busrate = None
truckrate = None

# ------------------------------------------------ Functions() ---------------------------------------------------------------- 


def verifyAndInsert():
  fnm1 = insfnm.get()
  lnm1 = inslnm.get()
  carno1 = inscar.get()
  cont1 = inscon.get()
  bal1 = insbal.get()
  vhe1 = insVeh.get()

  if(len(fnm1)==0 or len(lnm1)==0 or len(carno1)==0 or len(cont1)==0 or len(bal1)==0 or len(vhe1)==0):
      print "All feilds are mandatory!"
  else:
    insertUser(fnm1,lnm1,carno1,cont1,bal1,vhe1)
    print "Insertion Successful!"
    insU.destroy()

#---------------------------------------------------------------------------------------------------------------------------------

def delFromDB():
  carnm = delcar.get()
  res = deleteThisUser(carnm)
  if(res == 1 ):
    delU.destroy()

#-------------------------------------------------------------------------------------------------------------------------------
def validate():
  unm = usernameInput.get()
  pwd = passwordInput.get()
  conf = confirmInput.get()
  if(len(unm)==0 or len(pwd)==0 or len(conf)==0):
      print "All feilds are mandatory!"
  elif(not(pwd==conf)):
      print "Passwords do not match!"
  else:
     registerAdmin(unm,pwd)
     print "Admin is registered"
     LoginPage.lift()

#------------------------------------------------------------------------------------------------------------------------------

def authenticate():
  unm = loginUsername.get()
  pwd = loginPassword.get()
  if(len(unm)==0 or len(pwd)==0):
      print "All feilds are mandatory!"
  else:
     result = authenticateUser(unm,pwd)
     if(result==1):
       ControlPage.lift()
       print "Login Successful!"
     elif(result==0):
       print "Password is invalid!"
     else:
       print "Admin is not registered!"

#------------------------------------------------------------------------------------------------------------------------------

def showAdmin():
  adminWindow = tk.Tk()
  adminWindow.title("Admin Table")
  adminWindow.geometry("350x400")
  adminWindow.configure(background = "#333333")
  
  tk.Label(adminWindow,text = "Username",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.25, rely=0.05, anchor=tk.CENTER)
  tk.Label(adminWindow,text = "Password",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.75, rely=0.05, anchor=tk.CENTER)
  adminList = getAdminList()
  
  currentY = 0.2
  incrementY = 0.08

  for line in adminList:
    tk.Label(adminWindow,text = line[0],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.25, rely=currentY, anchor=tk.CENTER)
    tk.Label(adminWindow,text = line[1],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.75, rely=currentY, anchor=tk.CENTER)
    currentY = currentY + incrementY

  adminWindow.mainloop()

#------------------------------------------------------------------------------------------------------------------------------

def addUser():
  
  global insU
  insU = tk.Tk()
  insU.title("Add Vehicle User")
  insU.geometry("500x350")
  insU.configure(background = "#333333")
  
  tk.Label(insU,text =  "First Name",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.15, rely=0.08, anchor=tk.CENTER)
  tk.Label(insU,text =   "Last Name",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.15, rely=0.22, anchor=tk.CENTER)
  tk.Label(insU,text =  "Vehicle Number",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.15, rely=0.36, anchor=tk.CENTER)
  tk.Label(insU,text =     "Contact",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.15, rely=0.50, anchor=tk.CENTER)
  tk.Label(insU,text =        "Cash",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.15, rely=0.64, anchor=tk.CENTER)
  tk.Label(insU,text ="Vehicle type",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.15, rely=0.78, anchor=tk.CENTER)

  global insfnm
  insfnm = tk.Entry(insU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  insfnm.place(relx=0.6, rely=0.08, anchor=tk.CENTER)
  insfnm.config(highlightthickness=0)

  global inslnm
  inslnm = tk.Entry(insU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  inslnm.place(relx=0.6, rely=0.22, anchor=tk.CENTER)
  inslnm.config(highlightthickness=0)

  global inscar
  inscar = tk.Entry(insU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  inscar.place(relx=0.6, rely=0.36, anchor=tk.CENTER)
  inscar.config(highlightthickness=0)

  global inscon
  inscon = tk.Entry(insU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  inscon.place(relx=0.6, rely=0.50, anchor=tk.CENTER)
  inscon.config(highlightthickness=0)

  global insbal
  insbal = tk.Entry(insU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  insbal.place(relx=0.6, rely=0.64, anchor=tk.CENTER)
  insbal.config(highlightthickness=0)

  global insVeh
  insVeh = tk.Entry(insU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  insVeh.place(relx=0.6, rely=0.78, anchor=tk.CENTER)
  insVeh.config(highlightthickness=0)

  addMe = tk.Button(insU, text = "Add User"  ,width = 15,font = ("Arial"),command = verifyAndInsert,bg="#444444",fg="#cccccc")
  addMe.place(relx=0.5,rely=0.92, anchor=tk.CENTER)  
  
  addMe.config(highlightthickness=0)

 
  insU.mainloop()  

#--------------------------------------------------------------------------------------------------------------------------

def delUser():
  global delU
  delU = tk.Tk()
  delU.title("Delete Vehicle User")
  delU.geometry("300x150")
  delU.configure(background = "#333333")

  tk.Label(delU,text =  "Vehicle number",font = ("Times new roman", 14),bg="#333333",fg="#999999").place(relx=0.5, rely=0.1, anchor=tk.CENTER)

  global delcar
  delcar = tk.Entry(delU,font = ("Arial", 16),bg="#555555",fg="#ffffff")
  delcar.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
  delcar.config(highlightthickness=0)
 
  delBtn = tk.Button(delU, text = "Delete"  ,width = 15,font = ("Arial"),command = delFromDB,bg="#444444",fg="#cccccc")
  delBtn.place(relx=0.5,rely=0.8, anchor=tk.CENTER)
  delBtn.config(highlightthickness=0)  
  
#-------------------------------------------------------------------------------------------------------------------------

def deductBal():
  vehNo = processImage(imgCount)
  vehType = getVehicleType(vehNo)                                             

  print "vehicleType = " , str(vehType)
  if(vehType == 0):
    print "Vehicle not registered!"
    updateHistory(vehNo,vehType,0)
  else:
    c = updateBalance(vehNo, vehType)
    updateHistory(vehNo,vehType,c)


#-------------------------------------------------------------------------------------------------------------------------

def addThisAmount():
  if(len(amountEntry.get())==0):
    print "Enter some amount!"
  else:
    result = addBalDB(carAmount.get(),amountEntry.get())
    if(result==1):
      xa.destroy()
    
      

#--------------------------------------------------------------------------------------------------------------------------

def addBalance():
  global xa
  xa = tk.Tk()
  xa.title("Add Balance")
  xa.geometry("460x230") 
  xa.configure(background = "#333333")

  global carAmount
  global amountEntry

  tk.Label(xa,text =  "Vehicle number",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.2, rely=0.3, anchor=tk.CENTER)
  carAmount = tk.Entry(xa,font = ("Arial", 15),width=17,bg="#555555",fg="#ffffff")
  carAmount.place(relx=0.65, rely=0.3, anchor=tk.CENTER)
  carAmount.config(highlightthickness=0)

  tk.Label(xa,text =  "Amount",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.2, rely=0.55, anchor=tk.CENTER)
  amountEntry = tk.Entry(xa,font = ("Arial", 15),width=17,bg="#555555",fg="#ffffff")
  amountEntry.place(relx=0.65, rely=0.55, anchor=tk.CENTER)
  amountEntry.config(highlightthickness=0)

  delBtn = tk.Button(xa, text = "Add"  ,width = 15,font = ("Arial"),command = addThisAmount,bg="#444444",fg="#cccccc")
  delBtn.place(relx=0.5,rely=0.8, anchor=tk.CENTER)  
  delBtn.config(highlightthickness=0)

#-----------------------------------------------------------------------------------------------------------------------------------

def updateThis():
   if(len(carrate.get())==0 and len(busrate.get())==0 and len(truckrate.get())==0 ):
    print "Enter rates!"
   else:
    result = updateToDB(carrate.get(),busrate.get(),truckrate.get())
    if(result==1):
      ya.destroy()


#-----------------------------------------------------------------------------------------------------------------------------------

def updateRates():
  global ya
  ya = tk.Tk()
  ya.title("Update Rates")
  ya.geometry("460x300") 
  ya.configure(background = "#333333")

  global carrate
  global busrate
  global truckrate

  tk.Label(ya,text =  "Car",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.2, rely=0.15, anchor=tk.CENTER)
  carrate = tk.Entry(ya,font = ("Arial", 15),width=17,bg="#555555",fg="#ffffff")
  carrate.place(relx=0.65, rely=0.15, anchor=tk.CENTER)
  carrate.config(highlightthickness=0)

  tk.Label(ya,text =  "Bus",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.2, rely=0.37, anchor=tk.CENTER)
  busrate = tk.Entry(ya,font = ("Arial", 15),width=17,bg="#555555",fg="#ffffff")
  busrate.place(relx=0.65, rely=0.37, anchor=tk.CENTER)
  busrate.config(highlightthickness=0)

  tk.Label(ya,text =  "Truck",font = ("Times new roman", 15),bg="#333333",fg="#eeeeee").place(relx=0.2, rely=0.59, anchor=tk.CENTER)
  truckrate = tk.Entry(ya,font = ("Arial", 15),width=17,bg="#555555",fg="#ffffff")
  truckrate.place(relx=0.65, rely=0.59, anchor=tk.CENTER)
  truckrate.config(highlightthickness=0)

  delBtn = tk.Button(ya, text = "Update"  ,width = 12,font = ("Arial"),command = updateThis,bg="#444444",fg="#cccccc")
  delBtn.place(relx=0.5,rely=.87, anchor=tk.CENTER)  
  delBtn.config(highlightthickness=0)
  

#--------------------------------------------------------------------------------------------------------------------------

def showUserTable():

  userWindow = tk.Tk()
  userWindow.title("Vehicle Users Table")
  userWindow.geometry("850x600")
  userWindow.configure(background = "#333333")
  
  tk.Label(userWindow,text = "First Name  ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.1, rely=0.05, anchor=tk.CENTER)
  tk.Label(userWindow,text = "Last Name   ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.23, rely=0.05, anchor=tk.CENTER)
  tk.Label(userWindow,text = "Car Number  ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.39, rely=0.05, anchor=tk.CENTER)
  tk.Label(userWindow,text = "Contact     ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.58, rely=0.05, anchor=tk.CENTER)
  tk.Label(userWindow,text = "Balance (Rs)",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.74, rely=0.05, anchor=tk.CENTER)
  tk.Label(userWindow,text = "Vehicle Type",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.9, rely=0.05, anchor=tk.CENTER)

  userList = getUserList()
  
  currentY = 0.15
  incrementY = 0.05

  for line in userList:
    tk.Label(userWindow,text = line[0],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.1, rely=currentY, anchor=tk.CENTER)
    tk.Label(userWindow,text = line[1],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.23, rely=currentY, anchor=tk.CENTER)
    tk.Label(userWindow,text = line[2],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.39, rely=currentY, anchor=tk.CENTER)
    tk.Label(userWindow,text = line[3],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.58, rely=currentY, anchor=tk.CENTER)
    tk.Label(userWindow,text = line[4],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.74, rely=currentY, anchor=tk.CENTER)
    tk.Label(userWindow,text = line[5],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.9, rely=currentY, anchor=tk.CENTER)
    currentY = currentY + incrementY

  userWindow.mainloop()

#--------------------------------------------------------------------------------------------------------------------------

def changeImage():
    path = "image/" + str(imgCount) + ".png"
    image = Image.open(path)
    image = image.resize((330, 330), Image.ANTIALIAS)
    
    img2 = ImageTk.PhotoImage(image)
    panel.configure(image=img2)
    panel.image = img2

#--------------------------------------------------------------------------------------------------------------------------

def loadLogin():
  LoginPage.lift()

#-------------------------------------------------------------------------------------------------------------------------

def gotoThanks():
  ThanksPage.lift()

#--------------------------------------------------------------------------------------------------------------------------

def nextImg():
    global imgCount 
    f = open("/home/raman/Desktop/Project/vc","r")
    for word in f:
      num = word
    f.close()
 
    imgCount = ( imgCount )% int(num) + 1;
    changeImage()

#--------------------------------------------------------------------------------------------------------------------------

def prevImg():
    global imgCount 
    imgCount = imgCount - 1;
    f = open("/home/raman/Desktop/Project/vc","r")
    for word in f:
      num = word
    f.close()
 
    if(imgCount==0):
      imgCount = int(num); 
    changeImage() 
#----------------------------------------------------------------------------------------------------------------------------------

def showHistWindow():
  rWindow = tk.Tk()
  rWindow.title("History")
  rWindow.geometry("850x600")
  rWindow.configure(background = "#333333")
  
  tk.Label(rWindow,text = "Vehicle No  ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.1, rely=0.05, anchor=tk.CENTER)
  tk.Label(rWindow,text = "Type   ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.25, rely=0.05, anchor=tk.CENTER)
  tk.Label(rWindow,text = "Date  ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.39, rely=0.05, anchor=tk.CENTER)
  tk.Label(rWindow,text = "Time     ",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.58, rely=0.05, anchor=tk.CENTER)
  tk.Label(rWindow,text = "Comment",font = ("Times new roman", 13),bg="#333333",fg="#eeeeee").place(relx=0.81, rely=0.05, anchor=tk.CENTER)

  rList = getHistoryList()
  
  currentY = 0.15
  incrementY = 0.05

  for line in rList:
    tk.Label(rWindow,text = line[0],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.1, rely=currentY, anchor=tk.CENTER)
    tk.Label(rWindow,text = line[1],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.24, rely=currentY, anchor=tk.CENTER)
    tk.Label(rWindow,text = line[2],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.39, rely=currentY, anchor=tk.CENTER)
    tk.Label(rWindow,text = line[3],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.57, rely=currentY, anchor=tk.CENTER)
    tk.Label(rWindow,text = line[4],font = ("Arial", 12),bg="#333333",fg="#aaaaaa").place(relx=0.82, rely=currentY, anchor=tk.CENTER)
    currentY = currentY + incrementY

  rWindow.mainloop()
  

# ---------------------------------------------------- Base Class(Page) ---------------------------------------------------------- 

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# ------------------------------------------------------ Login Page -------------------------------------------------------------- 

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global LoginPage 
       LoginPage = self

       LoginPage.configure(background = "#333333")

       heading = tk.Label(self, text = "Welcome to Automatic Toll Simulator",font=("Times new roman", 20),bg="#333333",fg="#ffffff")
       heading.place(relx=0.5, rely=0.09, anchor=tk.CENTER)

       tk.Label(self,text = "Username",font = ("Arial", 12),bg="#333333",fg="#999999").place(relx=0.27, rely=0.34, anchor=tk.CENTER)
       tk.Label(self,text = "Password",font = ("Arial", 12),bg="#333333",fg="#999999").place(relx=0.27, rely=0.44, anchor=tk.CENTER)
  
       global loginUsername
       loginUsername = tk.Entry(self,font = ("Arial", 18),bg="#555555",fg="#ffffff")
       loginUsername.place(relx=0.5, rely=0.34, anchor=tk.CENTER)
       global loginPassword
       loginPassword = tk.Entry(self,font = ("Arial", 18), show = "*",bg="#555555",fg="#ffffff")
       loginPassword.place(relx=0.5, rely=0.44, anchor=tk.CENTER)

       login = tk.Button(self, text = "Login" ,width = 6,font = ("Arial"),command = authenticate,bg="#2B4988",fg="#dddddd")
       login.place(relx=0.50, rely=.55, anchor=tk.CENTER)
       login.config(highlightthickness=0)
       quit  = tk.Button(self, text = "Quit"  ,width = 10,font = ("Arial"),command = gotoThanks,bg="#444444",fg="#cccccc")
       quit.place(relx=0.40, rely=.75, anchor=tk.CENTER)
       quit.config(highlightthickness=0)
       register = tk.Button(self, text = "Register"  ,width = 10,font = ("Arial"),command = RegisterPage.lift,bg="#444444",fg="#cccccc")
       register.place(relx=0.60, rely=.75, anchor=tk.CENTER)
       register.config(highlightthickness=0)

# ---------------------------------------------------- Register Page -------------------------------------------------------------- 

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global RegisterPage
       RegisterPage = self

       RegisterPage.configure(background = "#333333")

       heading = tk.Label(self, text = "Register Admin",font=("Times new roman", 20),bg="#333333",fg="#ffffff")
       heading.place(relx=0.5, rely=0.09, anchor=tk.CENTER)

       tk.Label(self,text = "Username",font = ("Arial", 12),bg="#333333",fg="#999999").place(relx=0.27, rely=0.34, anchor=tk.CENTER)
       tk.Label(self,text = "Password",font = ("Arial", 12),bg="#333333",fg="#999999").place(relx=0.27, rely=0.44, anchor=tk.CENTER)  
       tk.Label(self,text = "Confirm Password",font = ("Arial", 12),bg="#333333",fg="#999999").place(relx=0.23, rely=0.54, anchor=tk.CENTER)

       global usernameInput
       usernameInput = tk.Entry(self,font = ("Arial", 18),bg="#555555",fg="#ffffff")
       usernameInput.place(relx=0.5, rely=0.34, anchor=tk.CENTER)
       global passwordInput
       passwordInput = tk.Entry(self,font = ("Arial", 18), show = "*",bg="#555555",fg="#ffffff")
       passwordInput.place(relx=0.5, rely=0.44, anchor=tk.CENTER)
       global confirmInput
       confirmInput = tk.Entry(self,font = ("Arial", 18), show = "*",bg="#555555",fg="#ffffff")
       confirmInput.place(relx=0.5, rely=0.54, anchor=tk.CENTER) 

       registerBtn =tk.Button(self, text = "Register now"  ,width = 12,font = ("Arial"),command = validate,bg="#91070e",fg="#ffffff") 
       registerBtn.place(relx=0.50, rely=.68, anchor=tk.CENTER)
       registerBtn.config(highlightthickness=0)

       back = tk.Button(self,text = "back",bg="#555555",fg="#dddddd",command = loadLogin)
       back.place(relx=0.02,rely=0.02)
       back.config(highlightthickness=0)

  

# ----------------------------------------------------- Thanks Page -------------------------------------------------------------- 

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global ThanksPage
       ThanksPage = self   

       ThanksPage.configure(background = "#ffffff")

       thanks = tk.Label(self, text = "Thank you for using Automatic Toll Simulator",font=("Arial black", 20),background = "#ffffff")
       thanks.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

       img = ImageTk.PhotoImage(Image.open('image/thankyou.png'))
       panel = tk.Label(self, image=img)
       panel.image = img
       panel.place(relx=0.5,rely=0.4,anchor = tk.CENTER)
    
# ------------------------------------------------------ Control Page --------------------------------------------------------------

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global ControlPage
       ControlPage = self 

       ControlPage.configure(background = "#333333")
     
       makeChanges =tk.Button(self, text = "Deduct Balance"  ,width = 15,font = ("Arial"),command = deductBal,bg="#444444",fg="#cccccc") 
       makeChanges.place(relx=0.63, rely=.83, anchor=tk.CENTER)

       showadm =tk.Button(self, text = "Show Admin Table"  ,width = 15,font = ("Arial"),command = showAdmin,bg="#444444",fg="#cccccc") 
       showadm.place(relx=0.63, rely=.94, anchor=tk.CENTER)

       showusrBtn =tk.Button(self, text = "Show User Table"  ,width = 15,font = ("Arial"),command = showUserTable,bg="#444444",fg="#cccccc") 
       showusrBtn.place(relx=0.88, rely=.94, anchor=tk.CENTER)

       insUserBtn =tk.Button(self, text = "Add Vehicle User"  ,width = 15,font = ("Arial"),command = addUser,bg="#444444",fg="#cccccc") 
       insUserBtn.place(relx=0.12, rely=.94, anchor=tk.CENTER)

       delUserBtn =tk.Button(self, text = "Delete Vehicle User"  ,width = 15,font = ("Arial"),command = delUser,bg="#444444",fg="#cccccc") 
       delUserBtn.place(relx=0.37, rely=.94, anchor=tk.CENTER)

       nextBtn =tk.Button(self, text = ">"  ,width = 1,font = ("Arial"),command = nextImg,bg="#555555",fg="#ffffff") 
       nextBtn.place(relx=0.72, rely=.35, anchor=tk.CENTER)

       prevBtn =tk.Button(self, text = "<"  ,width = 1,font = ("Arial"),command = prevImg,bg="#555555",fg="#ffffff") 
       prevBtn.place(relx=0.28, rely=.35, anchor=tk.CENTER)

       addBalBtn =tk.Button(self, text = "Add Balance"  ,width = 15,font = ("Arial"),command = addBalance,bg="#444444",fg="#cccccc") 
       addBalBtn.place(relx=0.37, rely=.83, anchor=tk.CENTER)

       showHistoryBtn =tk.Button(self, text = "Show History"  ,width = 15,font = ("Arial"),command = showHistWindow,bg="#444444",fg="#cccccc") 
       showHistoryBtn.place(relx=0.88, rely=.83, anchor=tk.CENTER)

       changeBtn =tk.Button(self, text = "Update Rates"  ,width = 15,font = ("Arial"),command = updateRates,bg="#444444",fg="#cccccc") 
       changeBtn.place(relx=0.12, rely=.83, anchor=tk.CENTER)

       makeChanges.config(highlightthickness=0)
       showadm.config(highlightthickness=0)
       showusrBtn.config(highlightthickness=0)
       insUserBtn.config(highlightthickness=0)
       delUserBtn.config(highlightthickness=0)
       nextBtn.config(highlightthickness=0)
       prevBtn.config(highlightthickness=0)
       addBalBtn.config(highlightthickness=0)
       showHistoryBtn.config(highlightthickness=0)
       changeBtn.config(highlightthickness=0)

       image = Image.open('image/1.png')
       image = image.resize((330, 330), Image.ANTIALIAS)
       img = ImageTk.PhotoImage(image)

       global panel
       panel = tk.Label(self, image=img)
       panel.image = img
       panel.place(relx=0.5,rely=0.35,anchor = tk.CENTER)

       back = tk.Button(self,text = "back",bg="#555555",fg="#dddddd",command = LoginPage.lift)
       back.place(relx=0.02,rely=0.02)
       back.config(highlightthickness=0)

# ------------------------------------------------------ Main View -------------------------------------------------------------- 

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
	
	p3 = Page3(self)        
	p2 = Page2(self)
        p1 = Page1(self)
        p4 = Page4(self)

        container = tk.Frame(self)
	container.pack(side="top", fill="both", expand=True)

        LoginPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        RegisterPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
	ControlPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        LoginPage.show()

