# 通过下拉菜单选择不同类别的内容，文本的提示信息跟着变化

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("software app")

# 实现text动态变化
def fundMsgDetail(*args):
	#print(fundCodeChosen.get())
	if fundCodeChosen.get() == "310398":
		fundCodeDetailTxt.set("申万菱")
	elif fundCodeChosen.get() == "090010":
		fundCodeDetailTxt.set("大成中证")


Label(root, text="基金详情").grid(row=0,column=0)
# 一个下拉列表
fundCode = StringVar()
fundCodeChosen = ttk.Combobox(root, width=12, textvariable=fundCode, state='readonly')
fundCodeChosen['values'] = ("310398","090010") # 设置下拉列表的值
fundCodeChosen.grid(row=0,column=1) # 设置其在界面中出现的位置 column代表列 row 代表行
fundCodeChosen.current(0) # 设置下拉列表默认显示的值，0为fundCodeChosen['values'] 的下标值
fundCodeChosen.bind("<<ComboboxSelected>>",fundMsgDetail)  #绑定事件,(下拉列表框被选中时，绑定fundMsgDetail()函数)

# by using textvariable to implement to change the text's content automaticlly
fundCodeDetailTxt = StringVar() 
fundCodeDetailTxt.set("暂没选择基金类别")
Label(root,textvariable=fundCodeDetailTxt).grid(row=0,column=2)

root.mainloop()