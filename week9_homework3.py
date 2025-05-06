from tkinter import *
from time import *

fnameList = ["bear.gif", "bee.gif", "cartoon.gif", "cat.gif", "cartoon1.gif", "dog1.gif", "dog3.gif", "joy.gif", "whale.gif"]
photoList = [None]*9
num=0

def clickNext():
    global num
    num+=1
    if num>8:
        num=0
    photo = PhotoImage(file="C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\window programming\\pic\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    photoName()
    

def clickPrev():
    global num
    num-=1
    if num<0:
        num=8
    photo = PhotoImage(file="C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\window programming\\pic\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    photoName()
    
    
def photoName():
    global num
    name = fnameList[num]
    pNameLabel.configure(text=name)
  

window = Tk()
window.geometry("500x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<<이전", command = clickPrev)
btnNext = Button(window, text="다음>>", command = clickNext)
pNameLabel = Label(window, text=fnameList[num])
pNameLabel.pack()


photo = PhotoImage(file="C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\window programming\\pic\\"+fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=50, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=155, y=70)

window.mainloop()