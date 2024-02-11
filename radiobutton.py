from tkinter import *

window = Tk()
window.geometry("200x200")
window.config(bg="orange")

I = IntVar()
I.set(0)

Menu = {"Optsion A:":1,"Optsion B:":2,"Optsion C:":3}
for txt,val in Menu.items():
    Radiobutton(window,text=txt,variable=I,value=val).pack(side=TOP,pady=7)

window.mainloop()