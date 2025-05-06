from tkinter import *
import random

btn_list = [None] * 9
fnamelist = ["bear.gif", "bee.gif", "cartoon.gif", "cat.gif", "cartoon1.gif", "dog1.gif", "dog3.gif", "joy.gif", "whale.gif"]
photolist = [None] * 9

random.shuffle(fnamelist) # 이미지 리스트를 무작위로 섞음

window = Tk()
window.title("이미지 랜덤 배치치")


image_width = 300
image_height = 300
window_width = image_width * 3
window_height = image_height * 3
window.geometry(f"{window_width}x{window_height}")
window.resizable(width=TRUE, height=TRUE)

for i in range(9):
    photolist[i] = PhotoImage(file="C:/Users/yongh/OneDrive/바탕 화면/python/window programming/pic\\"+fnamelist[i])
    row = i // 3  # 행 인덱스 (0, 1, 2)
    col = i % 3   # 열 인덱스 (0, 1, 2)
    x_pos = col * image_width
    y_pos = row * image_height
    btn_list[i] = Button(window, image=photolist[i])
    btn_list[i].place(x=x_pos, y=y_pos)

window.mainloop()