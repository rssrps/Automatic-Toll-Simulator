from Tkinter import *
from PIL import ImageTk, Image
#import ttk

def check():
  print "Hello"

root=Tk()
root.title('NMIMS GROCERY STORE')
#root.wm_iconbitmap('favicon.ico')
root.configure(background="#d3d3d3")
img = ImageTk.PhotoImage(Image.open('thankyou.png'))
panel = Label(root, image = img).grid(row=0, column=0,columnspan=5)
  
Label(root,text='NMIMS GROCERY STORE',background="#d3d3d3").grid(row=1,column=0,columnspan=5)
Label(root,text="Mukesh Patel School of Technology Management & Engineering, Shirpur",background="#d3d3d3").grid(row=2,column=0,columnspan=5)
Label(root,text='--------------------------------------------------------------',background="#d3d3d3").grid(row=3,column=0,columnspan=5)
Label(root, text='Username',background="#d3d3d3").grid(row=4, column=1)
un=Entry(root,width=20)
un.grid(row=4, column=2)
Label(root, text='Password',background="#d3d3d3").grid(row=5, column=1)
pwd=Entry(root,width=20, show="*")
pwd.grid(row=5, column=2)
Label(root,text='',background="#d3d3d3").grid(row=6,column=0,columnspan=5)
Button(root,width=6,text='Enter',command=check).grid(row=7, column=1)
Button(root,width=6,text='Close',command=root.destroy).grid(row=7, column=2)
root.mainloop()
