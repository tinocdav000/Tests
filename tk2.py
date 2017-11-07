from tkinter import *
import time as t

root = Tk()

L0 = Label(root, text='NAME')
L1 = Label(root, text='PASSWORD')

E0 = Entry(root)
E1 = Entry(root)

L0.grid(row=0,column=0,sticky=E)
L1.grid(row=1,column=0,sticky=W)
E0.grid(row=0,column=1)
E1.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2,row=2)


root.mainloop()
