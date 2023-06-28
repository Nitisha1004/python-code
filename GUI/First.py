import os
os.system('cls')
from tkinter import*
root = Tk()
root.title('First window')
root.geometry('350x300')
myLabel1 = Label(root, text="Name")
myLabel2 = Label(root, text="Surname")
myLabel1.place(x =10, y=30)
myLabel2.grid(row = 4, column=2)
myLabel2.place(x =30, y=40)
root.mainloop()
