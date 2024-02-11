from tkinter import*

window = Tk()
window.geometry("500x500")

def C():
    print(i.get())

i = IntVar()

c = Checkbutton(window,text="Really?",variable=i)
c.pack()

b = Button(window,text="continue",command="C")
b.pack()

window.mainloop()