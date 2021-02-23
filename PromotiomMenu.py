from tkinter import *
from AmountMenu import *

class PromotionMenu:
    def __init__(self, promotionMenu,main):
        """ Initialise the Frame. """
        self.master = promotionMenu
        self.mainW = main

    def create_widgets(self):
        self.button_promotion1 = Button(self.master, text="โปรโมชั่น1", width=13, height=6, font=30,
                                        bg="royalblue3", command=lambda: self.amountorder("โปรโมชั่น1","50"),state=DISABLED)
        self.button_promotion1.grid(row=0, column=0)
        self.button_promotion2 = Button(self.master, text="โปรโมชั่น2", width=13, height=6, font=30,
                                        bg="royalblue2", command=lambda: self.amountorder("โปรโมชั่น2","50"),state=DISABLED)
        self.button_promotion2.grid(row=0, column=1)
        self.button_promotion3 = Button(self.master, text="โปรโมชั่น3", width=13, height=6, font=30,
                                        bg="royalblue1", command=lambda: self.amountorder("โปรโมชั่น3","50"),state=DISABLED)
        self.button_promotion3.grid(row=0, column=2)
        self.button_promotion4 = Button(self.master, text="โปรโมชั่น4", width=13, height=6, font=30,
                                        bg="royalblue3", command=lambda: self.amountorder("โปรโมชั่น4","50"),state=DISABLED)
        self.button_promotion4.grid(row=1, column=0)
        self.button_promotion5 = Button(self.master, text="โปรโมชั่น5", width=13, height=6, font=30,
                                        bg="royalblue2", command=lambda: self.amountorder("โปรโมชั่น5","50"),state=DISABLED)
        self.button_promotion5.grid(row=1, column=1)
        self.button_promotion6 = Button(self.master, text="โปรโมชั่น6", width=13, height=6, font=30,
                                        bg="royalblue1", command=lambda: self.amountorder("โปรโมชั่น6","50"),state=DISABLED)
        self.button_promotion6.grid(row=1, column=2)
        self.button_promotion7 = Button(self.master, text="โปรโมชั่น7", width=13, height=6, font=30,
                                        bg="royalblue3", command=lambda: self.amountorder("โปรโมชั่น7","50"),state=DISABLED)
        self.button_promotion7.grid(row=2, column=0)
        self.button_promotion8 = Button(self.master, text="โปรโมชั่น8", width=13, height=6, font=30,
                                        bg="royalblue2", command=lambda: self.amountorder("โปรโมชั่น8","50"),state=DISABLED)
        self.button_promotion8.grid(row=2, column=1)
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


