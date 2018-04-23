from Tkinter import *
from DBconnect import *
from pages import *
import sqlite3

root = None

def finishProject():
  global root 
  return root

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Automatic Toll Simulator")
    root.geometry("900x550") 
    root.resizable(0, 0) 
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
   
    root.mainloop()


