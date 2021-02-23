from tkinter import *
from AmountMenu import *

class SoupMenu(Frame):
    def __init__(self, soupMenu, main):
        """ Initialise the Frame. """
        self.master = soupMenu
        self.mainW = main

    def create_widgets(self):
        self.button_soup1 = Button(self.master, text="ซุปมิโสะ", width=13, height=6, font=30,
                                   bg="royalblue3", command=lambda: self.amountorder("ซุปมิโซะ","50"))
        self.button_soup1.grid(row=0, column=0)
        self.button_soup2 = Button(self.master, text="ซุป2", width=13, height=6, font=30,
                                   bg="royalblue2", command=lambda: self.amountorder("ซุป2","50"),state=DISABLED)
        self.button_soup2.grid(row=0, column=1)
        self.button_soup3 = Button(self.master, text="ซุป3", width=13, height=6, font=30,
                                   bg="royalblue1", command=lambda: self.amountorder("ซุป3","50"),state=DISABLED)
        self.button_soup3.grid(row=0, column=2)
        self.button_soup4 = Button(self.master, text="ซุป4", width=13, height=6, font=30,
                                   bg="royalblue3", command=lambda: self.amountorder("ซุป4","50"),state=DISABLED)
        self.button_soup4.grid(row=1, column=0)
        self.button_soup5 = Button(self.master, text="ซุป5", width=13, height=6, font=30,
                                   bg="royalblue2", command=lambda: self.amountorder("ซุป5","50"),state=DISABLED)
        self.button_soup5.grid(row=1, column=1)
        self.button_soup6 = Button(self.master, text="ซุป6", width=13, height=6, font=30,
                                   bg="royalblue1", command=lambda: self.amountorder("ซุป6","50"),state=DISABLED)
        self.button_soup6.grid(row=1, column=2)
        self.button_soup7 = Button(self.master, text="ซุป7", width=13, height=6, font=30,
                                   bg="royalblue3", command=lambda: self.amountorder("ซุป7","50"),state=DISABLED)
        self.button_soup7.grid(row=2, column=0)
        self.button_soup8 = Button(self.master, text="ซุป8", width=13, height=6, font=30,
                                   bg="royalblue2", command=lambda: self.amountorder("ซุป8","50"),state=DISABLED)
        self.button_soup8.grid(row=2, column=1)
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


