from tkinter import *
from tkinter import ttk

master = Tk()
# application's name
master.title("基金操作软件")


# 实现text动态变化
def fundMsgDetail(*args):
	#print(fundCodeChosen.get())
	if fundCodeChosen.get() == "310398":
		fundCodeDetailTxt.set("申万菱信沪深300价值指数A类")
	elif fundCodeChosen.get() == "090010":
		fundCodeDetailTxt.set("大成中证红利指数A")

# 年份获取
fundYear = StringVar() 
def fundMsgYear(*args):
	print(yearChosen.get())
	fundYear.set(yearChosen.get())

# 月份获取
fundMonth = StringVar() 
def fundMsgMonth(*args):
	print(monthChosen.get())
	fundMonth.set(monthChosen.get())	

# 月份获取
fundDay = StringVar() 
def fundMsgDay(*args):
	print(dayChosen.get())
	fundDay.set(dayChosen.get())	


# 列数值
columnIndex = 1

# 定投时间
time = Label(master, text="定投时间")
time.grid(row=0, sticky=E)

# 定投时间设置
endYear = 3001 # not include 3001
startYear = 2018
n = endYear - startYear
yearList=[None] * n 
yearIndex = 0
for i in range(startYear,endYear):
	yearList[yearIndex] = i
	if i < (endYear -1):  # end year that we don't need to add 1
		yearIndex = yearIndex + 1;

year = StringVar()
yearChosen = ttk.Combobox(master, width=5, textvariable=year, state='readonly')
yearChosen['values'] = yearList # 设置下拉列表的值
yearChosen.grid(row=0,column=columnIndex) # 设置其在界面中出现的位置 column代表列 row 代表行
yearChosen.current(1) # 设置下拉列表默认显示的值，1为yearChosen['values'] 的下标值
yearChosen.bind("<<ComboboxSelected>>",fundMsgYear)  #绑定事件,(下拉列表框被选中时，绑定fundMsgYear()函数)

columnIndex += 1
month = StringVar()
monthChosen = ttk.Combobox(master, width=3, textvariable=month, state='readonly')
monthChosen['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12') # 设置下拉列表的值
monthChosen.grid(row=0,column=columnIndex) # 设置其在界面中出现的位置 column代表列 row 代表行
monthChosen.current(0) 
monthChosen.bind("<<ComboboxSelected>>",fundMsgMonth)  


columnIndex += 1
day = StringVar()
dayChosen = ttk.Combobox(master, width=3, textvariable=day, state='readonly')
dayChosen['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31') # 设置下拉列表的值
dayChosen.grid(row=0,column=columnIndex) # 设置其在界面中出现的位置 column代表列 row 代表行
dayChosen.current(0) 
dayChosen.bind("<<ComboboxSelected>>",fundMsgDay)  


columnIndex += 1
Label(master, text="基金代码").grid(row=0,column=columnIndex)

# 一个下拉列表
columnIndex += 1
fundCode = StringVar()
fundCodeChosen = ttk.Combobox(master, width=8, textvariable=fundCode, state='readonly')
fundCodeChosen['values'] = ("310398","090010") # 设置下拉列表的值
fundCodeChosen.grid(row=0,column=5) # 设置其在界面中出现的位置 column代表列 row 代表行
fundCodeChosen.current(0) # 设置下拉列表默认显示的值，0为fundCodeChosen['values'] 的下标值
fundCodeChosen.bind("<<ComboboxSelected>>",fundMsgDetail)  #绑定事件,(下拉列表框被选中时，绑定fundMsgDetail()函数)

# by using textvariable to implement to change the text's content automaticlly
# 显示选择的基金品种
columnIndex += 1
fundCodeDetailTxt = StringVar() 
fundCodeDetailTxt.set("暂没选择基金类别")
Label(master,textvariable=fundCodeDetailTxt).grid(row=0,column=columnIndex)

# 买入卖出金额
columnIndex += 1
money = Label(master, text="买入卖出金额")
money.grid(row=0, column=columnIndex)

columnIndex += 1
moneySet = Entry(master,width=8)
moneySet.grid(row=0, column=columnIndex)

# 成交单价
columnIndex += 1
onePrice = Label(master, text="成交单价")
onePrice.grid(row=0, column=columnIndex)

columnIndex += 1
onePriceSet = Entry(master,width=8)
onePriceSet.grid(row=0, column=columnIndex)

# 盈利收益率
columnIndex += 1
earningRate = Label(master, text="盈利收益率")
earningRate.grid(row=0, column=columnIndex)

columnIndex += 1
earningRateSet = Entry(master,width=8)
earningRateSet.grid(row=0, column=columnIndex)

# 市盈率
columnIndex += 1
peRatio = Label(master, text="市盈率")
peRatio.grid(row=0, column=columnIndex)

columnIndex += 1
peRatioSet = Entry(master,width=8)
peRatioSet.grid(row=0, column=columnIndex)

#e2 = Entry(master)
#e2.pack(side=LEFT)


def callback():
	print("hello")
    #print(e1.get())
    #print(e2.get())

b = Button(master, text="提交基金交易信息", width=20, command=callback)
#b.pack(side=LEFT)

mainloop()
