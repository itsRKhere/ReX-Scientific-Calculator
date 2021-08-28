from tkinter import *
import math
import tkinter.messagebox

window = Tk()

window.iconbitmap(r'C:\Users\Mahadev\Documents\RK Documents\Code\Projects\Scientific Calc with GUI\icon.ico')
window.geometry("375x587+200-70")
window.configure(bg = "#ffffff")
window.resizable(width=False, height=False)

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 587,
    width = 775,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

class Calc():
    def __init__(self):
        self.total=0
        self.currentValue=''
        self.inputValue=True
        self.checkSum=False
        self.operator=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=myScreen.get()
        secondnum=str(num)
        if self.inputValue:
            self.currentValue = secondnum
            self.inputValue=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.currentValue = firstnum+secondnum
        self.display(self.currentValue)

    def sum_of_total(self):
        self.result=True
        self.currentValue=float(self.currentValue)
        if self.checkSum==True:
            self.valid_function()
        else:
            self.total=float(myScreen.get())

    def display(self, value):
        myScreen.delete(0, END)
        myScreen.insert(0, value)

    def valid_function(self):
        if self.operator == "add":
            self.total += self.currentValue
        if self.operator == "sub":
            self.total -= self.currentValue
        if self.operator == "multi":
            self.total *= self.currentValue
        if self.operator == "divide":
            self.total /= self.currentValue
        if self.operator == "mod":
            self.total %= self.currentValue
        self.inputValue=True
        self.checkSum=False
        self.display(self.total)

    def operation(self, operator):
        self.currentValue = float(self.currentValue)
        if self.checkSum:
            self.valid_function()
        elif not self.result:
            self.total=self.currentValue
            self.inputValue=True
        self.checkSum=True
        self.operator=operator
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.currentValue = "0"
        self.display(0)
        self.inputValue=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.currentValue = math.pi
        self.display(self.currentValue)

    def tau(self):
        self.result =  False
        self.currentValue = math.tau
        self.display(self.currentValue)

    def e(self):
        self.result =  False
        self.currentValue = math.e
        self.display(self.currentValue)

    def mathPM(self):
        self.result = False
        self.currentValue = -(float(myScreen.get()))
        self.display(self.currentValue)

    def squared(self):
        self.result = False
        self.currentValue = math.sqrt(float(myScreen.get()))
        self.display(self.currentValue)

    def cos(self):
        self.result = False
        self.currentValue = math.cos(math.radians(float(myScreen.get())))
        self.display(self.currentValue)

    def cosh(self):
        self.result = False
        self.currentValue = math.cosh(math.radians(float(myScreen.get())))
        self.display(self.currentValue)

    def tan(self):
        self.result = False
        self.currentValue = math.tan(math.radians(float(myScreen.get())))
        self.display(self.currentValue)

    def tanh(self):
        self.result = False
        self.currentValue = math.tanh(math.radians(float(myScreen.get())))
        self.display(self.currentValue)

    def sin(self):
        self.result = False
        self.currentValue = math.sin(math.radians(float(myScreen.get())))
        self.display(self.currentValue)

    def sinh(self):
        self.result = False
        self.currentValue = math.sinh(math.radians(float(myScreen.get())))
        self.display(self.currentValue)

    def log(self):
        self.result = False
        self.currentValue = math.log(float(myScreen.get()))
        self.display(self.currentValue)

    def exp(self):
        self.result = False
        self.currentValue = math.exp(float(myScreen.get()))
        self.display(self.currentValue)

    def acosh(self):
        self.result = False
        self.currentValue = math.acosh(float(myScreen.get()))
        self.display(self.currentValue)

    def asinh(self):
        self.result = False
        self.currentValue = math.asinh(float(myScreen.get()))
        self.display(self.currentValue)

    def expm1(self):
        self.result = False
        self.currentValue = math.expm1(float(myScreen.get()))
        self.display(self.currentValue)

    def lgamma(self):
        self.result = False
        self.currentValue = math.lgamma(float(myScreen.get()))
        self.display(self.currentValue)

    def degrees(self):
        self.result = False
        self.currentValue = math.degrees(float(myScreen.get()))
        self.display(self.currentValue)

    def log2(self):
        self.result = False
        self.currentValue = math.log2(float(myScreen.get()))
        self.display(self.currentValue)

    def log10(self):
        self.result = False
        self.currentValue = math.log10(float(myScreen.get()))
        self.display(self.currentValue)

    def log1p(self):
        self.result = False
        self.currentValue = math.log1p(float(myScreen.get()))
        self.display(self.currentValue)

EnterVal = Calc()

myScreen = Entry(window, font=('Helvetica',48),bg='white',fg='black',
                     width=28,justify=RIGHT,relief=FLAT)
myScreen.insert(0,"0")

myScreen.place(
    x = 10, y = 41,
    width = 347,
    height = 60)


canvas.create_rectangle(
    0, 123, 0+755, 123+464,
    fill = "#dcfffb",
    outline = "")

img=PhotoImage(file ='images/Titleimage.png')
canvas.create_image(573,50,image=img)

img0 = PhotoImage(file = f"images/img0.png")
btn0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=0:EnterVal.numberEnter(x),
    relief = SUNKEN)

btn0.place(
    x = 120, y = 502,
    width = 66,
    height = 66)

img1 = PhotoImage(file = f"images/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    highlightbackground='#dcfffb',
    command = lambda x=2:EnterVal.numberEnter(x),
    relief = SUNKEN)

b1.place(
    x = 120, y = 412,
    width = 66,
    height = 66)

img2 = PhotoImage(file = f"images/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    highlightbackground='#dcfffb',
    command = lambda x=5:EnterVal.numberEnter(x),
    relief = SUNKEN)
    
b2.place(
    x = 120, y = 321,
    width = 66,
    height = 66)

img3 = PhotoImage(file = f"images/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=8:EnterVal.numberEnter(x),
    relief = SUNKEN)

b3.place(
    x = 120, y = 237,
    width = 66,
    height = 66)

img4 = PhotoImage(file = f"images/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:EnterVal.numberEnter("."),
    relief = SUNKEN)

b4.place(
    x = 216, y = 502,
    width = 66,
    height = 66)

img5 = PhotoImage(file = f"images/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=3:EnterVal.numberEnter(x),
    relief = SUNKEN)

b5.place(
    x = 216, y = 412,
    width = 66,
    height = 66)

img6 = PhotoImage(file = f"images/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.Clear_Entry,
    relief = SUNKEN)

b6.place(
    x = 22, y = 142,
    width = 66,
    height = 66)

img7 = PhotoImage(file = f"images/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.All_Clear_Entry,
    relief = SUNKEN)

b7.place(
    x = 120, y = 142,
    width = 66,
    height = 66)

img8 = PhotoImage(file = f"images/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:EnterVal.operation("divide"),
    relief = SUNKEN)

b8.place(
    x = 292, y = 147,
    width = 66,
    height = 66)

img9 = PhotoImage(file = f"images/img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:EnterVal.operation("multi"),
    relief = SUNKEN)

b9.place(
    x = 292, y = 237,
    width = 66,
    height = 66)

img10 = PhotoImage(file = f"images/img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:EnterVal.operation("sub"),
    relief = SUNKEN)

b10.place(
    x = 292, y = 321,
    width = 66,
    height = 66)

img11 = PhotoImage(file = f"images/img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=0:EnterVal.operation("add"),
    relief = SUNKEN)

b11.place(
    x = 296, y = 412,
    width = 66,
    height = 66)

img12 = PhotoImage(file = f"images/img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.sum_of_total,
    relief = SUNKEN)

b12.place(
    x = 296, y = 502,
    width = 66,
    height = 66)

img13 = PhotoImage(file = f"images/img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=1:EnterVal.numberEnter(x),
    relief = SUNKEN)

b13.place(
    x = 22, y = 412,
    width = 66,
    height = 66)

img14 = PhotoImage(file = f"images/img14.png")
b14 = Button(
    image = img14,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=4:EnterVal.numberEnter(x),
    relief = SUNKEN)

b14.place(
    x = 22, y = 321,
    width = 66,
    height = 66)

img15 = PhotoImage(file = f"images/img15.png")
b15 = Button(
    image = img15,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=7:EnterVal.numberEnter(x),
    relief = SUNKEN)

b15.place(
    x = 22, y = 237,
    width = 66,
    height = 66)

img16 = PhotoImage(file = f"images/img16.png")
b16 = Button(
    image = img16,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=6:EnterVal.numberEnter(x),
    relief = SUNKEN)

b16.place(
    x = 216, y = 321,
    width = 66,
    height = 66)

img17 = PhotoImage(file = f"images/img17.png")
b17 = Button(
    image = img17,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda x=9:EnterVal.numberEnter(x),
    relief = SUNKEN)

b17.place(
    x = 216, y = 237,
    width = 66,
    height = 66)

img18 = PhotoImage(file = f"images/img18.png")
b18 = Button(
    image = img18,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.mathPM,
    relief = SUNKEN)

b18.place(
    x = 22, y = 502,
    width = 66,
    height = 66)

img19 = PhotoImage(file = f"images/img19.png")
b19 = Button(
    image = img19,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.squared,
    relief = SUNKEN)

b19.place(
    x = 216, y = 147,
    width = 66,
    height = 66)


img20 = PhotoImage(file = f"images/img20.png")
b20 = Button(
    image = img20,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.degrees,
    relief = "flat")

b20.place(
    x = 481, y = 502,
    width = 68,
    height = 68)

img21 = PhotoImage(file = f"images/img21.png")
b21 = Button(
    image = img21,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.log1p,
    relief = "flat")

b21.place(
    x = 481, y = 412,
    width = 68,
    height = 68)

img22 = PhotoImage(file = f"images/img22.png")
b22 = Button(
    image = img22,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.exp,
    relief = "flat")

b22.place(
    x = 481, y = 321,
    width = 68,
    height = 68)

img23 = PhotoImage(file = f"images/img23.png")
b23 = Button(
    image = img23,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.cosh,
    relief = "flat")

b23.place(
    x = 481, y = 237,
    width = 68,
    height = 68)

img24 = PhotoImage(file = f"images/img24.png")
b24 = Button(
    image = img24,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.acosh,
    relief = "flat")

b24.place(
    x = 577, y = 502,
    width = 68,
    height = 68)

img25 = PhotoImage(file = f"images/img25.png")
b25 = Button(
    image = img25,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.expm1,
    relief = "flat")

b25.place(
    x = 577, y = 412,
    width = 68,
    height = 68)

img26 = PhotoImage(file = f"images/img26.png")
b26 = Button(
    image = img26,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.pi,
    relief = "flat")

b26.place(
    x = 383, y = 142,
    width = 68,
    height = 68)

img27 = PhotoImage(file = f"images/img27.png")
b27 = Button(
    image = img27,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.cos,
    relief = "flat")

b27.place(
    x = 481, y = 142,
    width = 68,
    height = 68)

img28 = PhotoImage(file = f"images/img28.png")
b28 = Button(
    image = img28,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.sin,
    relief = "flat")

b28.place(
    x = 653, y = 147,
    width = 68,
    height = 68)

img29 = PhotoImage(file = f"images/img29.png")
b29 = Button(
    image = img29,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.sinh,
    relief = "flat")

b29.place(
    x = 653, y = 237,
    width = 68,
    height = 68)

img30 = PhotoImage(file = f"images/img30.png")
b30 = Button(
    image = img30,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.e,
    relief = "flat")

b30.place(
    x = 653, y = 321,
    width = 68,
    height = 68)

img31 = PhotoImage(file = f"images/img31.png")
b31 = Button(
    image = img31,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.lgamma,
    relief = "flat")

b31.place(
    x = 657, y = 412,
    width = 88,
    height = 68)

img32 = PhotoImage(file = f"images/img32.png")
b32 = Button(
    image = img32,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.asinh,
    relief = "flat")

b32.place(
    x = 667, y = 502,
    width = 68,
    height = 68)

img33 = PhotoImage(file = f"images/img33.png")
b33 = Button(
    image = img33,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.log10,
    relief = "flat")

b33.place(
    x = 383, y = 412,
    width = 68,
    height = 68)

img34 = PhotoImage(file = f"images/img34.png")
b34 = Button(
    image = img34,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.log,
    relief = "flat")

b34.place(
    x = 383, y = 321,
    width = 68,
    height = 68)

img35 = PhotoImage(file = f"images/img35.png")
b35 = Button(
    image = img35,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.tau,
    relief = "flat")

b35.place(
    x = 383, y = 237,
    width = 68,
    height = 68)

img36 = PhotoImage(file = f"images/img36.png")
b36 = Button(
    image = img36,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:EnterVal.operation("mod"),
    relief = "flat")

b36.place(
    x = 577, y = 321,
    width = 68,
    height = 68)

img37 = PhotoImage(file = f"images/img37.png")
b37 = Button(
    image = img37,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.tanh,
    relief = "flat")

b37.place(
    x = 577, y = 237,
    width = 68,
    height = 68)

img38 = PhotoImage(file = f"images/img38.png")
b38 = Button(
    image = img38,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.log2,
    relief = "flat")

b38.place(
    x = 383, y = 502,
    width = 68,
    height = 68)

img39 = PhotoImage(file = f"images/img39.png")
b39 = Button(
    image = img39,
    borderwidth = 0,
    highlightthickness = 0,
    command = EnterVal.tan,
    relief = "flat")

b39.place(
    x = 580, y = 142,
    width = 68,
    height = 68)

def iExit():
    iExit = tkinter.messagebox.askyesno(" ReX Scientific Calculator","Do you want to exit ?")
    if iExit>0:
        window.destroy()
        return

def Scientific():
    window.resizable(width=False, height=False)
    window.geometry("755x587+0+0")


def Standard():
    window.resizable(width=False, height=False)
    window.geometry("375x587+0+0")


menubar = Menu(window)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)


window.config(menu=menubar)
window.mainloop()
