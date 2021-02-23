from tkinter import *
from AmountMenu import *


class RamenMenu:
    def __init__(self, ramenMenu, main):
        """ Initialise the Frame. """
        self.master = ramenMenu
        self.mainW = main

    def create_widgets(self):
        self.button_ramen1 = Button(self.master, text="ทงคตสึราเมง", width=13, height=6, font=30, bg="royalblue3",
                                    command=lambda: self.amountorder("ทงคตสึราเมง", "50"))
        self.button_ramen1.grid(row=0, column=0)
        self.button_ramen2 = Button(self.master, text="ราเมงมิโซะ", width=13, height=6, font=30, bg="royalblue2",
                                    command=lambda: self.amountorder("ราเมงมิโซะ", "50"))
        self.button_ramen2.grid(row=0, column=1)
        self.button_ramen3 = Button(self.master, text="โชยุราเมง", width=13, height=6, font=30, bg="royalblue1",
                                    command=lambda: self.amountorder("โชยุราเมง","50"))
        self.button_ramen3.grid(row=0, column=2)
        self.button_ramen4 = Button(self.master, text="ชิโอะราเมง", width=13, height=6, font=30, bg="royalblue3",
                                    command=lambda: self.amountorder("ชิโอะราเมง","50"))
        self.button_ramen4.grid(row=1, column=0)
        self.button_ramen5 = Button(self.master, text="ชิโอะราเมง", width=13, height=6, font=30, bg="royalblue2",
                                    command=lambda: self.amountorder("ราเมง5","50"),state=DISABLED)
        self.button_ramen5.grid(row=1, column=1)
        self.button_ramen6 = Button(self.master, text="ราเมง6", width=13, height=6, font=30, bg="royalblue1",
                                    command=lambda: self.amountorder("ราเมง 6","50"),state=DISABLED)
        self.button_ramen6.grid(row=1, column=2)
        self.button_ramen7 = Button(self.master, text="ราเมง7", width=13, height=6, font=30, bg="royalblue3",
                                    command=lambda: self.amountorder("ราเมง 7","50"),state=DISABLED)
        self.button_ramen7.grid(row=2, column=0)
        self.button_ramen8 = Button(self.master, text="ราเมง8", width=13, height=6, font=30, bg="royalblue2",
                                    command=lambda: self.amountorder("ราเมง 8","50"),state=DISABLED)
        self.button_ramen8.grid(row=2, column=1)
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





