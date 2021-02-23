from tkinter import *
from AmountMenu import *

class DrinkMenu(Frame):
    def __init__(self, drinkMenu,main):
        """ Initialise the Frame. """
        self.master = drinkMenu
        self.mainW = main

    def create_widgets(self):
        self.button_drink1 = Button(self.master, text="น้ำเปล่า", width=13, height=6, font=30,
                                    bg="royalblue3", command=lambda: self.amountorder("น้ำเปล่า","10"))
        self.button_drink1.grid(row=0, column=0)
        self.button_drink2 = Button(self.master, text="โค้ก", width=13, height=6, font=30,
                                    bg="royalblue2", command=lambda: self.amountorder("โค้ก","15"))
        self.button_drink2.grid(row=0, column=1)
        self.button_drink3 = Button(self.master, text="อิชิตัน", width=13, height=6, font=30,
                                    bg="royalblue1", command=lambda: self.amountorder("อิชิตัน","20"))
        self.button_drink3.grid(row=0, column=2)
        self.button_drink4 = Button(self.master, text="เบียช้าง", width=13, height=6, font=30,
                                    bg="royalblue3", command=lambda: self.amountorder("เบียช้าง","60"))
        self.button_drink4.grid(row=1, column=0)
        self.button_drink5 = Button(self.master, text="เครื่องดื่ม5", width=13, height=6, font=30,
                                    bg="royalblue2", command=lambda: self.amountorder("เครื่องดื่ม5","60"),state=DISABLED)
        self.button_drink5.grid(row=1, column=1)
        self.button_drink6 = Button(self.master, text="เครื่องดื่ม6", width=13, height=6, font=30,
                                    bg="royalblue1", command=lambda: self.amountorder("เครื่องดื่ม6","50"),state=DISABLED)
        self.button_drink6.grid(row=1, column=2)
        self.button_drink7 = Button(self.master, text="เครื่องดื่ม7", width=13, height=6, font=30,
                                    bg="royalblue3", command=lambda: self.amountorder("เครื่องดื่ม7","50"),state=DISABLED)
        self.button_drink7.grid(row=2, column=0)
        self.button_drink8 = Button(self.master, text="เครื่องดื่ม8", width=13, height=6, font=30,
                                    bg="royalblue2", command=lambda: self.amountorder("เครื่องดื่ม8","50"),state=DISABLED)
        self.button_drink8.grid(row=2, column=1)
        self.button_back = Button(self.master, text="ย้อนกลับ", width=13, height=6, font=30, bg="red3",
                             command=self.master.destroy)
        self.button_back.grid(row=2, column=2)
    def amountorder(self, nameMenu, price):
        root = Tk()
        root.geometry("620x170+450+300")
        root["bg"] = "royalblue4"
        app = AmountMenu(root, self.mainW, nameMenu, price)
        app.create_widgets()
        root.mainloop()
def leftClickButton(event):
    pass

