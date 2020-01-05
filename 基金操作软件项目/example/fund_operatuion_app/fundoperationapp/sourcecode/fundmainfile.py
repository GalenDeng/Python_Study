import tkinter as tk
import fundoperationfile as fundWork





if __name__ == '__main__':
    root = tk.Tk()
    root.title("基金操作软件")
    width = 1000  # 把窗口宽度(单位:像素)300赋值给变量width
    height = 400  # 把窗口高度(单位:像素)300赋值给变量height
    root.geometry('{}x{}'.format(width, height))  # 改变窗口大小
    #fundoperationapp = fundWork.fundOperationFile(root)
    #fundoperationapp.fundNumberViewSet()
    fundoperationapp = fundWork.fundOperationNumber(root)
    fundoperationapp.fundNumberViewSet()
    #fundoperationapp.fundoperation()
    root.mainloop()