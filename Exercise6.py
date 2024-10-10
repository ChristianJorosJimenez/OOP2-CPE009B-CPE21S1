from tkinter import*

class MyWindow:
    def __init__(self, win):
        #common widgets
        self.Label1=Label(win, fg="Black", text="Jimenez's Calculator", bg="bisque", font=("Broadway", 19) )
        self.Label1.place(x=60,y=10)

        self.Label2=Label(win, text="First Number: ", bg="bisque")
        self.Label2.place(x=50,y=70)

        self.Entry1=Entry(win, bd=5)
        self.Entry1.place(x=150,y=70)

        self.Label3 = Label(win, text="Second Number ", bg="bisque")
        self.Label3.place(x=50, y=110)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=150, y=110)

        self.Label4 = Label(win, text="Result: ", bg="bisque")
        self.Label4.place(x=50, y=150)

        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=150, y=150)

        self.Button1=Button(win,fg="Black",text="Add", bg="bisque",command=self.add)
        self.Button1.place(x=140,y=230)
        self.Button1.bind('<Button-1>',self.add)

        self.Button2 = Button(win, fg="Black", text="Subtract", bg="bisque",command=self.subtract)
        self.Button2.place(x=130, y=280)

        self.Button3 = Button(win, fg="Black", text="Multiply", bg="bisque",command=self.multiply)
        self.Button3.place(x=200, y=280)

        self.Button4 = Button(win, fg="Black", text="Divide", bg="bisque",command=self.divide)
        self.Button4.place(x=200, y=230)

        win.config(bg="brown")

    def add(self):
        self.Entry3.delete(0,'end')
        num1=int(self.Entry1.get())
        num2=int(self.Entry2.get())
        result=num1 + num2
        self.Entry3.insert(END,str(result))

    def subtract(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))


    def multiply(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))


    def divide(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))


window=Tk()
MyWin=MyWindow(window)
window.geometry("400x400+20+20")
window.title("Standard Calculator")
window.mainloop()

