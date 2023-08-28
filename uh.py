from tkinter import Tk, Label, Entry, StringVar

app = Tk()

labelText=StringVar()
labelText.set("Enter directory of log files")
labelDir=Label(app, textvariable=labelText, height=4)
labelDir.grid(row=1,column=1)

directory=StringVar(None)
dirname=Entry(app,textvariable=directory,width=50)
dirname.grid(row=1,column=2)

labelText2=StringVar()
labelText2.set("Enter directory of log files2")
labelDir2=Label(app, textvariable=labelText2, height=4)
labelDir2.grid(row=2,column=1)

directory2=StringVar(None)
dirname2=Entry(app,textvariable=directory2,width=50)
dirname2.grid(row=2,column=2)

app.mainloop()