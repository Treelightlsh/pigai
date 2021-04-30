from tkinter import *


#
# # frame
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
# leftframe = Frame(root)
# leftframe.pack(side=LEFT)
# rightframe = Frame(root)
# rightframe.pack(side=RIGHT)
# label = Label(frame, text='Hello World')
# label.pack()
# button1 = Button(leftframe, text='Button1')
# button1.pack(padx=1, pady=1)
# button2 = Button(rightframe, text='Button2')
# button2.pack(padx=3, pady=3)
# button3 = Button(leftframe, text='Button3')
# button3.pack(padx=3, pady=3)
# root.title('test')
# root.mainloop()

# 可显示点击次数
def dianwo():
    global click
    # global label
    click += 1
    label.config(text='点击了%s次' % click)


root = Tk()
click = 0
label = Label(root, text='点击了%s次' % click)
label.pack()
button = Button(root, text='点我', command=dianwo)
button.pack(padx=100, pady=10)
root.mainloop()
