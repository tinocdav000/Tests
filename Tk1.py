import time as r

root = Tk()

label = Label(root, text='Hello, this is the first test with tkinter', fg='blue', bg='red')
label.pack(fill=X)

Tframe = Frame(root)
Tframe.pack(side=TOP)
Bframe = Frame(root)
Bframe.pack(side=BOTTOM)

B1 = Button(Tframe, text='Button 1', fg="red")
B2 = Button(Tframe, text='Button 2', fg='green')
B3 = Button(Tframe, text='Button 3', fg='blue')
B4 = Button(Bframe, text='Button 4', fg='red')

B1.pack(side=LEFT)
B2.pack(side=LEFT)
B3.pack(side=LEFT)
B4.pack(side=LEFT)

root.mainloop()
