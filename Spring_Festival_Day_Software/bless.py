from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("2020 新年快乐！")
root["background"] = "white"
width = 400  # 把窗口宽度(单位:像素)300赋值给变量width
height = 340  # 把窗口高度(单位:像素)300赋值给变量height
root.geometry('{}x{}'.format(width, height))  # 改变窗口大小

# ,slant=tkFont.ITALIC  size=15
customFont = tkFont.Font(family="Arial Narrow",size=15, weight=tkFont.BOLD,slant=tkFont.ITALIC)

centerText = Label(root, text="武汉加油",font = customFont,fg="red",bg="white")
centerText.place(x = 150,y = 10)


img_gif = PhotoImage(file = 'pig.gif')
label_img = Label(root, image = img_gif)
label_img.place(x = 60, y = 50)


addValue = 40

leftX = 20
leftY = 50

leftText = Label(root, text="阖",font = customFont,fg="red",bg="white")
leftText.place(x = leftX , y= leftY)

leftText = Label(root, text="家",font = customFont,fg="red",bg="white")
leftY = leftY + addValue
leftText.place(x = leftX , y = leftY)

leftText = Label(root, text="安",font = customFont,fg="red",bg="white")
leftY = leftY + addValue
leftText.place(x = leftX , y = leftY)

leftText = Label(root, text="康",font = customFont,fg="red",bg="white")
leftY = leftY + addValue
leftText.place(x = leftX , y = leftY)

leftText = Label(root, text="过",font = customFont,fg="red",bg="white")
leftY = leftY + addValue
leftText.place(x = leftX , y = leftY)

leftText = Label(root, text="大",font = customFont,fg="red",bg="white")
leftY = leftY + addValue
leftText.place(x = leftX , y = leftY)

leftText = Label(root, text="年",font = customFont,fg="red",bg="white")
leftY = leftY + addValue
leftText.place(x = leftX , y = leftY)

rightX = 340
rightY = 50
rightText = Label(root, text="万",font = customFont,fg="red",bg="white")
rightText.place(x = rightX , y = rightY)

rightText = Label(root, text="众",font = customFont,fg="red",bg="white")
rightY = rightY + addValue
rightText.place(x = rightX , y = rightY)

rightText = Label(root, text="一",font = customFont,fg="red",bg="white")
rightY = rightY + addValue
rightText.place(x = rightX , y = rightY)

rightText = Label(root, text="心",font = customFont,fg="red",bg="white")
rightY = rightY + addValue
rightText.place(x = rightX , y = rightY)

rightText = Label(root, text="渡",font = customFont,fg="red",bg="white")
rightY = rightY + addValue
rightText.place(x = rightX , y = rightY)

rightText = Label(root, text="难",font = customFont,fg="red",bg="white")
rightY = rightY + addValue
rightText.place(x = rightX , y = rightY)

rightText = Label(root, text="关",font = customFont,fg="red",bg="white")
rightY = rightY + addValue
rightText.place(x = rightX , y = rightY)

root.mainloop()