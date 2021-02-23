from tkinter import *

class AmountMenu(Frame):
    amount = 1

    def __init__(self, amountMenu, main , nameMenu, pr):
        """ Initialise the Frame. """
        self.master = amountMenu
        self.mainW = main
        self.name = nameMenu
        self.price = pr

    def create_widgets(self):
        self.button_minus = Button(self.master, text="-", width=13, height=3, font=30, bg="red", command=self.minusAmount)
        self.button_minus.grid(row=0, column=0)
        self.amountLalel = Label(self.master, text="1", width=28, height=3, bg="white", font=1)
        self.amountLalel.grid(row=0, column=2, columnspan=2)
        self.button_plus = Button(self.master, text="+", width=13, height=3, font=30, bg="green", command=self.plusAmount)
        self.button_plus.grid(row=0, column=4)
        self.button_confirm = Button(self.master, text="ยืนยัน", width=13, height=3, font=30, bg="green",
                                command=self.addItem)
        self.button_confirm.grid(row=1, column=2)
        self.button_cancel = Button(self.master, text="ยกเลิก", width=13, height=3, font=30, bg="red",
                               command=self.master.destroy)
        self.button_cancel.grid(row=1, column=3)

    def plusAmount(self):
        amount = int(self.amountLalel.cget("text")) + 1
        self.amountLalel.config(text=amount)
    def minusAmount(self):
        amount = int(self.amountLalel.cget("text")) - 1
        self.amountLalel.config(text=amount)
    def leftClickButton(event):
        pass

    def Ok(self):
        self.master.destroy

    def addItem(self):
        tableName = self.mainW.tabelNumber.cget("text")
        num = 0
        temp = []
        count = 0
        total = 0

        if tableName == "โต๊ะ1":
            num = len(self.mainW.table1)

            self.mainW.labelOder[num].config(text=str(num + 1))
            self.mainW.labelList[num].config(text=self.name)
            self.mainW.labelAmount[num].config(text=self.amountLalel.cget("text"))
            self.mainW.labelPrice[num].config(text=int(self.price) * int(self.amountLalel.cget("text")))

            temp.append(str(num + 1))
            temp.append(self.name)
            temp.append(self.amountLalel.cget("text"))
            temp.append(int(self.price) * int(self.amountLalel.cget("text")))
            self.mainW.table1.append(temp)

            n = 0
            for i in self.mainW.labelAmount:
                n += 1
                if n > len(self.mainW.table1):
                    break
                else:
                    count += int(i.cget("text"))

            n = 0
            for i in self.mainW.labelPrice:
                n += 1
                if n > len(self.mainW.table1):
                    break
                else:
                    total += int(i.cget("text"))
        elif tableName == "โต๊ะ2":
            num = len(self.mainW.table2)

            self.mainW.labelOder[num].config(text=str(num + 1))
            self.mainW.labelList[num].config(text=self.name)
            self.mainW.labelAmount[num].config(text=self.amountLalel.cget("text"))
            self.mainW.labelPrice[num].config(text=int(self.price) * int(self.amountLalel.cget("text")))

            temp.append(str(num + 1))
            temp.append(self.name)
            temp.append(self.amountLalel.cget("text"))
            temp.append(int(self.price) * int(self.amountLalel.cget("text")))
            self.mainW.table2.append(temp)

            n = 0
            for i in self.mainW.labelAmount:
                n += 1
                if n > len(self.mainW.table2):
                    break
                else:
                    count += int(i.cget("text"))

            n = 0
            for i in self.mainW.labelPrice:
                n += 1
                if n > len(self.mainW.table2):
                    break
                else:
                    total += int(i.cget("text"))
        elif tableName == "โต๊ะ3":
            num = len(self.mainW.table3)

            self.mainW.labelOder[num].config(text=str(num + 1))
            self.mainW.labelList[num].config(text=self.name)
            self.mainW.labelAmount[num].config(text=self.amountLalel.cget("text"))
            self.mainW.labelPrice[num].config(text=int(self.price) * int(self.amountLalel.cget("text")))

            temp.append(str(num + 1))
            temp.append(self.name)
            temp.append(self.amountLalel.cget("text"))
            temp.append(int(self.price) * int(self.amountLalel.cget("text")))
            self.mainW.table3.append(temp)

            n = 0
            for i in self.mainW.labelAmount:
                n += 1
                if n > len(self.mainW.table3):
                    break
                else:
                    count += int(i.cget("text"))

            n = 0
            for i in self.mainW.labelPrice:
                n += 1
                if n > len(self.mainW.table3):
                    break
                else:
                    total += int(i.cget("text"))
        elif tableName == "โต๊ะ4":
            num = len(self.mainW.table4)

            self.mainW.labelOder[num].config(text=str(num + 1))
            self.mainW.labelList[num].config(text=self.name)
            self.mainW.labelAmount[num].config(text=self.amountLalel.cget("text"))
            self.mainW.labelPrice[num].config(text=int(self.price) * int(self.amountLalel.cget("text")))

            temp.append(str(num + 1))
            temp.append(self.name)
            temp.append(self.amountLalel.cget("text"))
            temp.append(int(self.price) * int(self.amountLalel.cget("text")))
            self.mainW.table4.append(temp)

            n = 0
            for i in self.mainW.labelAmount:
                n += 1
                if n > len(self.mainW.table4):
                    break
                else:
                    count += int(i.cget("text"))

            n = 0
            for i in self.mainW.labelPrice:
                n += 1
                if n > len(self.mainW.table4):
                    break
                else:
                    total += int(i.cget("text"))
        elif tableName == "โต๊ะ5":
            num = len(self.mainW.table5)

            self.mainW.labelOder[num].config(text=str(num + 1))
            self.mainW.labelList[num].config(text=self.name)
            self.mainW.labelAmount[num].config(text=self.amountLalel.cget("text"))
            self.mainW.labelPrice[num].config(text=int(self.price) * int(self.amountLalel.cget("text")))

            temp.append(str(num + 1))
            temp.append(self.name)
            temp.append(self.amountLalel.cget("text"))
            temp.append(int(self.price) * int(self.amountLalel.cget("text")))
            self.mainW.table5.append(temp)

            n = 0
            for i in self.mainW.labelAmount:
                n += 1
                if n > len(self.mainW.table5):
                    break
                else:
                    count += int(i.cget("text"))

            n = 0
            for i in self.mainW.labelPrice:
                n += 1
                if n > len(self.mainW.table5):
                    break
                else:
                    total += int(i.cget("text"))
        elif tableName == "โต๊ะ6":
            num = len(self.mainW.table6)

            self.mainW.labelOder[num].config(text=str(num + 1))
            self.mainW.labelList[num].config(text=self.name)
            self.mainW.labelAmount[num].config(text=self.amountLalel.cget("text"))
            self.mainW.labelPrice[num].config(text=int(self.price) * int(self.amountLalel.cget("text")))

            temp.append(str(num + 1))
            temp.append(self.name)
            temp.append(self.amountLalel.cget("text"))
            temp.append(int(self.price) * int(self.amountLalel.cget("text")))
            self.mainW.table6.append(temp)

            n = 0
            for i in self.mainW.labelAmount:
                n += 1
                if n > len(self.mainW.table6):
                    break
                else:
                    count += int(i.cget("text"))

            n = 0
            for i in self.mainW.labelPrice:
                n += 1
                if n > len(self.mainW.table6):
                    break
                else:
                    total += int(i.cget("text"))
        #print(len(self.mainW.table1))
        self.mainW.labelAmount[9].config(text=count)
        self.mainW.labelPrice[9].config(text=total)
        self.button_confirm.after(1,self.master.destroy)

