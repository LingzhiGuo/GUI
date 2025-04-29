from tkinter import *
from tkinter import messagebox
root = Tk()  # 创建窗口对象的背景色
root.title("我的第一个GUI程序")  # 设置标题
root.geometry("500x300+500+200")  # 设置窗口大小与位置


btn01 = Button(root)
btn01['text'] = "点我就送花"  # 设置按钮文字

def songhua(e): # e是事件对象，用户点击按钮就会产生一个事件对象
    messagebox.showinfo(message="送你一朵花,亲亲我吧")  # 消息框
    print("送你99朵玫瑰")  # 打印

btn01.bind("<Button-1>",songhua)  # 绑定事件

btn01.pack()  # 按钮位置"紧缩"



root.mainloop()  # 进入消息循环

print("现在是dev分支")
print("从远程仓库拉下代码后,本地修改后再上传")