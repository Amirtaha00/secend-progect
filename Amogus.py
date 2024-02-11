from tkinter import*

window = Tk()

H_Screen = window.winfo_screenheight()
W_Screen = window.winfo_screenwidth()



Half_W = W_Screen // 2
Half_H = H_Screen // 2


Mainplace_X = 450#It can be changeble with numbers
Mainplace_Y = 450#It can be changeble with numbers


geometry_1 = int(Half_W-Mainplace_X//2)
geometry_2 = int(Half_H-Mainplace_Y//2)

window.title("screen!")
window.config(bg="tan")
window.resizable(0,0)
window.iconbitmap("Rook image")

window.geometry(f"{Mainplace_X}x{Mainplace_Y}+{geometry_1}+{geometry_2}")

window.mainloop()