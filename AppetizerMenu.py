from tkinter import *
from AmountMenu import *

class AppetizerMenu(Frame):
    def __init__(self, appetizerMenu,main):
        """ Initialise the Frame. """
        self.master = appetizerMenu
        self.mainW = main

    def create_widgets(self):
        self.button_appetizer1 = Button(self.master, text="ไก่คาราเกะ", width=13, height=6, font=30,
                                        bg="royalblue3", command=lambda: self.amountorder("ไก่คาราเกะ","40"))
        self.button_appetizer1.grid(row=0, column=0)
        self.button_appetizer2 = Button(self.master, text="เกี๊ยวซ่า", width=13, height=6, font=30,
                                        bg="royalblue2", command=lambda: self.amountorder("เกี๊ยวซ่า","40"))
        self.button_appetizer2.grid(row=0, column=1)
        self.button_appetizer3 = Button(self.master, text="กุ้งเท็มปุระ", width=13, height=6, font=30,
                                        bg="royalblue1", command=lambda: self.amountorder("กุ้งเท็มปุระ","60"))
        self.button_appetizer3.grid(row=0, column=2)
        self.button_appetizer4 = Button(self.master, text="อาหารว่าง4", width=13, height=6, font=30,
                                        bg="royalblue3", command=lambda: self.amountorder("อาหารว่าง4","50"),state=DISABLED)
        self.button_appetizer4.grid(row=1, column=0)
        self.button_appetizer5 = Button(self.master, text="อาหารว่าง5", width=13, height=6, font=30,
                                        bg="royalblue2", command=lambda: self.amountorder("อาหารว่าง5","50"),state=DISABLED)
        self.button_appetizer5.grid(row=1, column=1)
        self.button_appetizer6 = Button(self.master, text="อาหารว่าง6", width=13, height=6, font=30,
                                        bg="royalblue1", command=lambda: self.amountorder("อาหารว่าง6","50"),state=DISABLED)
        self.button_appetizer6.grid(row=1, column=2)
        self.button_appetizer7 = Button(self.master, text="อาหารว่าง7", width=13, height=6, font=30,
                                        bg="royalblue3", command=lambda: self.amountorder("อาหารว่าง7","50"),state=DISABLED)
        self.button_appetizer7.grid(row=2, column=0)
        self.button_appetizer8 = Button(self.master, text="อาหารว่าง8", width=13, height=6, font=30,
                                        bg="royalblue2", command=lambda: self.amountorder("อาหารว่าง8","50"),state=DISABLED)
        self.button_appetizer8.grid(row=2, column=1)
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




