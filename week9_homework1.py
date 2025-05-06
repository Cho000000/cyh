from tkinter import *
window = Tk()

photo = PhotoImage(file="C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\window programming\\dog1.gif")
label1 = Label(window, image=photo)

photo2 = PhotoImage(file="C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\window programming\\cat.gif")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack()

window.mainloop()