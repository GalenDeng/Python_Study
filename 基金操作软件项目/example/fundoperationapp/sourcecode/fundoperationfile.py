import tkinter as tk


class fundOperationFile():

    def __init__(self,master):
        self.master = master

    def printMsg(self):
        print("Happy Christmas")


    #实现text动态变化
    def fundMsgDetail(*args,value):
        #print(fundCodeChosen.get())
        global fundCodeDetailTxt
        if value == "310398":
            fundCodeDetailTxt.set("申万菱信沪深300价值指数A类")
        elif value == "090010":
            fundCodeDetailTxt.set("大成中证红利指数A")


    def fundMsgYear(*args,value):
        # 年份获取
        fundYear = tk.StringVar()
        print(value)
        fundYear.set(value)


    def fundMsgMonth(*args,value):
        # 月份获取
        fundMonth = tk.StringVar()
        print(value)
        fundMonth.set(value)


    def fundMsgDay(*args,value):
        # 天数获取
        fundDay = tk.StringVar()
        print(value)
        fundDay.set(value)


    def fundoperation(master):
        #列数值
        columnIndex = 1

        # 定投时间
        time = tk.Label(master, text="定投时间")
        time.grid(row=0, sticky=0)

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

        year = tk.StringVar()
        yearChosen = tk.ttk.Combobox(master, width=5, textvariable=year, state='readonly')
        yearChosen['values'] = yearList # 设置下拉列表的值
        yearChosen.grid(row=0,column=columnIndex) # 设置其在界面中出现的位置 column代表列 row 代表行
        yearChosen.current(1) # 设置下拉列表默认显示的值，1为yearChosen['values'] 的下标值
        yearChosen.bind("<<ComboboxSelected>>",master.fundMsgYear(yearChosen.get()))  #绑定事件,(下拉列表框被选中时，绑定fundMsgYear()函数)

        columnIndex += 1
        month = tk.StringVar()
        monthChosen = tk.ttk.Combobox(master, width=3, textvariable=month, state='readonly')
        monthChosen['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12') # 设置下拉列表的值
        monthChosen.grid(row=0,column=columnIndex) # 设置其在界面中出现的位置 column代表列 row 代表行
        monthChosen.current(0)
        monthChosen.bind("<<ComboboxSelected>>",master.fundMsgMonth(monthChosen.get()))


        columnIndex += 1
        day = tk.StringVar()
        dayChosen = tk.ttk.Combobox(master, width=3, textvariable=day, state='readonly')
        dayChosen['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31') # 设置下拉列表的值
        dayChosen.grid(row=0,column=columnIndex) # 设置其在界面中出现的位置 column代表列 row 代表行
        dayChosen.current(0)
        dayChosen.bind("<<ComboboxSelected>>",master.fundMsgDay(dayChosen.get()))


        columnIndex += 1
        tk.Label(master, text="基金代码").grid(row=0,column=columnIndex)

        # 一个下拉列表
        columnIndex += 1
        fundCode = tk.StringVar()
        fundCodeChosen = tk.ttk.Combobox(master, width=8, textvariable=fundCode, state='readonly')
        fundCodeChosen['values'] = ("310398","090010") # 设置下拉列表的值
        fundCodeChosen.grid(row=0,column=5) # 设置其在界面中出现的位置 column代表列 row 代表行
        fundCodeChosen.current(0) # 设置下拉列表默认显示的值，0为fundCodeChosen['values'] 的下标值
        fundCodeChosen.bind("<<ComboboxSelected>>",master.fundMsgDetail(fundCodeChosen.get()))  #绑定事件,(下拉列表框被选中时，绑定fundMsgDetail()函数)

        # by using textvariable to implement to change the text's content automaticlly
        # 显示选择的基金品种
        columnIndex += 1
        fundCodeDetailTxt = tk.StringVar()
        fundCodeDetailTxt.set("暂没选择基金类别")
        tk.Label(master,textvariable=fundCodeDetailTxt).grid(row=0,column=columnIndex)

        # 买入卖出金额
        columnIndex += 1
        money = tk.Label(master, text="买入卖出金额")
        money.grid(row=0, column=columnIndex)

        columnIndex += 1
        moneySet = tk.Entry(master,width=8)
        moneySet.grid(row=0, column=columnIndex)

        # 成交单价
        columnIndex += 1
        onePrice = tk.Label(master, text="成交单价")
        onePrice.grid(row=0, column=columnIndex)

        columnIndex += 1
        onePriceSet = tk.Entry(master,width=8)
        onePriceSet.grid(row=0, column=columnIndex)

        # 盈利收益率
        columnIndex += 1
        earningRate = tk.Label(master, text="盈利收益率")
        earningRate.grid(row=0, column=columnIndex)

        columnIndex += 1
        earningRateSet = tk.Entry(master,width=8)
        earningRateSet.grid(row=0, column=columnIndex)

        # 市盈率
        columnIndex += 1
        peRatio = tk.Label(master, text="市盈率")
        peRatio.grid(row=0, column=columnIndex)

        columnIndex += 1
        peRatioSet = tk.Entry(master,width=8)
        peRatioSet.grid(row=0, column=columnIndex)

