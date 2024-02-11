from tkinter import*

Window = Tk()
Window.geometry("500x500")
Window.title("Scroll bar")

Scroll = Scrollbar(Window)
Scroll.pack(side=RIGHT,fill=BOTH)

lst_box = Listbox(Window)
lst_box.pack(side=LEFT,fill=BOTH)

for i in range(50):
    lst_box.insert(END,"line"+str(i+1))

Scroll.config(command=lst_box.yview)

Window.mainloop()