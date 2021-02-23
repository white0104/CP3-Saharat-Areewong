from tkinter import *
from RamenMemu import *
from PromotiomMenu import *
from DrinkMenu import *
from SoupMenu import *
from AppetizerMenu import *
from ReprotMenu import  *
from ConfirmMenu import  *
import datetime
import csv
import pandas as pd
from openpyxl import load_workbook

class MainRamen(Frame):
    #table1Count = 1
    table1 = []
    table2 = []
    table3 = []
    table4 = []
    table5 = []
    table6 = []

    labelOder = []
    labelList = []
    labelPrice = []
    labelAmount = []

    def _init_(self, mainWindow):
        """ Initialise the Frame. """
        self.master = mainWindow

    def create_widgets(self):

        self.master["bg"]="royalblue4"
        self.button_tabel1=Button(self.master,text="โต้ะ1",width=13,height=6,font= 30,bg="royalblue3" , command=self.showTanble1)
        self.button_tabel1.grid(row=0,column=0,rowspan=6)
        self.button_tabel2=Button(self.master,text="โต้ะ2",width=13,height=6,font= 30,bg="royalblue2", command=self.showTanble2)
        self.button_tabel2.grid(row=0,column=1,rowspan=6)
        self.button_tabel3=Button(self.master,text="โต้ะ3",width=13,height=6,font= 30,bg="royalblue1",command=self.showTanble3)
        self.button_tabel3.grid(row=0,column=2,rowspan=6)
        self.button_tabel4=Button(self.master,text="โต้ะ4",width=13,height=6,font= 30,bg="royalblue3",command=self.showTanble4)
        self.button_tabel4.grid(row=6,column=0,rowspan=6)
        self.button_tabel5=Button(self.master,text="โต้ะ5",width=13,height=6,font= 30,bg="royalblue2",command=self.showTanble5)
        self.button_tabel5.grid(row=6,column=1,rowspan=6)
        self.button_tabel6=Button(self.master,text="โต้ะ6",width=13,height=6,font= 30,bg="royalblue1",command=self.showTanble6)
        self.button_tabel6.grid(row=6,column=2,rowspan=6)
        self.button_ramen=Button(self.master,text="ราเเมง",width=13,height=6,font= 30,bg="royalblue3" ,
                                 command=self.showRamenMenu)
        self.button_ramen.grid(row=12,column=0)
        self.button_soup=Button(self.master,text="ซุป",width=13,height=6,font= 30,bg="royalblue2",
                                command=self.showSoupMenu)
        self.button_soup.grid(row=12,column=1)
        self.button_appetizer=Button(self.master,text="อาหารว่าง",width=13,height=6,font= 30,bg="royalblue1",
                                     command=self.showAppetizerMenu)
        self.button_appetizer.grid(row=12,column=2)
        self.button_drink=Button(self.master,text="เครื่องดื่ม",width=13,height=6,font= 30,bg="royalblue3",
                                 command=self.showDrinkMenu)
        self.button_drink.grid(row=13,column=0,rowspan=2)
        self.button_promotion=Button(self.master,text="โปรโมชั่น",width=13,height=6,font= 30,bg="royalblue2",
                                     command=self.showPromotionMenu)
        self.button_promotion.grid(row=13,column=1,rowspan=2)
        self.button_salesSummary=Button(self.master,text="สรุปยอด",width=13,height=2,font=1,bg="royalblue1" , command=self.showConfirmReport)
        self.button_salesSummary.bind('<Button-1>',leftClickButton)
        self.button_salesSummary.grid(row=13,column=2,)
        self.button_report=Button(self.master,text="รายงาน",width=13,height=2,font=1,bg="skyblue",command=self.showReportMenu)
        self.button_report.grid(row=14,column=2,)
        self.button_cancel=Button(self.master,text="ยกเลิกรายการ",width=28,height=6,font= 30,bg='red2', command=self.clearTable)
        self.button_cancel.grid(row=13,column=3,columnspan=4,rowspan=2)
        self.button_pay=Button(self.master,text="ชำระ",width=28,height=6,font=1,bg="green2", command=self.showConfirmMenu)
        self.button_pay.grid(row=12,column=3,columnspan=4)


        self.tabelNumber = Label(self.master, text="โต้ะ", width=28, anchor='w', justify='left', bg="royalblue4", font=1)
        self.tabelNumber.grid(row=0, column=3, columnspan=4)
        self.orderhead = Label(self.master, text="ลำดับ", width=4, anchor='w', justify='left', bg="royalblue3", font=1)
        self.orderhead.grid(row=1, column=3)
        self.listhead = Label(self.master,text="รายการ",width=11,justify='left',bg="royalblue3",height=1,font=1)
        self.listhead.grid(row=1,column=4)
        self.amounthead = Label(self.master, text="จำนวน", width=5, justify='left', bg="royalblue3", height=1, font=1)
        self.amounthead.grid(row=1,column=5)
        self.pricehead = Label(self.master,text="ราคา",width=6,justify='right',bg="royalblue3",height=1,font=1)
        self.pricehead.grid(row=1,column=6)


        self.order1 = Label(self.master, text="1", width=4, anchor='w', justify='left', bg="skyblue", height=1, font=1)
        self.order1.grid(row=2, column=3)
        self.list1 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list1.grid(row=2, column=4)
        self.amount1 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount1.grid(row=2,column=5)
        self.price1 = Label(self.master,text="",width=6,justify='right',bg="skyblue",height=1,font=1)
        self.price1.grid(row=2,column=6)
        self.labelOder.append(self.order1)
        self.labelList.append(self.list1)
        self.labelAmount.append(self.amount1)
        self.labelPrice.append(self.price1)
        self.order2 = Label(self.master,text="2",width=4,anchor='w',justify='left',bg="skyblue",height=1,font=1)
        self.order2.grid(row=3,column=3)
        self.list2 = Label(self.master,text="",width=11,justify='left',bg="skyblue",height=1,font=1)
        self.list2.grid(row=3,column=4)
        self.amount2 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount2.grid(row=3,column=5)
        self.price2 = Label(self.master,text="",width=6,justify='right',bg="skyblue",height=1,font=1)
        self.price2.grid(row=3,column=6)
        self.labelOder.append(self.order2)
        self.labelList.append(self.list2)
        self.labelAmount.append(self.amount2)
        self.labelPrice.append(self.price2)
        self.order3 = Label(self.master,text="3",width=4,anchor='w',justify='left',bg="skyblue",height=1,font=1)
        self.order3.grid(row=4,column=3)
        self.list3 = Label(self.master,text="",width=11,justify='left',bg="skyblue",height=1,font=1)
        self.list3.grid(row=4,column=4)
        self.amount3 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount3.grid(row=4,column=5)
        self.price3 = Label(self.master, text="", width=6, justify='right', bg="skyblue", height=1, font=1)
        self.price3.grid(row=4, column=6)
        self.labelOder.append(self.order3)
        self.labelList.append(self.list3)
        self.labelAmount.append(self.amount3)
        self.labelPrice.append(self.price3)
        self.order4 = Label(self.master, text="4", width=4, anchor='w', justify='left', bg="skyblue", height=1, font=1)
        self.order4.grid(row=5, column=3)
        self.list4 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list4.grid(row=5, column=4)
        self.amount4 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount4.grid(row=5,column=5)
        self.price4 = Label(self.master,text="",width=6,justify='right',bg="skyblue",height=1,font=1)
        self.price4.grid(row=5,column=6)
        self.labelOder.append(self.order4)
        self.labelList.append(self.list4)
        self.labelAmount.append(self.amount4)
        self.labelPrice.append(self.price4)
        self.order5 = Label(self.master, text="5", width=4, anchor='w', justify='left', bg="skyblue", height=1, font=1)
        self.order5.grid(row=6, column=3)
        self.list5 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list5.grid(row=6, column=4)
        self.amount5 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount5.grid(row=6,column=5)
        self.price5 = Label(self.master, text="", width=6, justify='right', bg="skyblue", height=1, font=1)
        self.price5.grid(row=6, column=6)
        self.labelOder.append(self.order5)
        self.labelList.append(self.list5)
        self.labelAmount.append(self.amount5)
        self.labelPrice.append(self.price5)
        self.order6 = Label(self.master, text="6", width=4, anchor='w', justify='left', bg="skyblue", height=1, font=1)
        self.order6.grid(row=7, column=3)
        self.list6 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list6.grid(row=7, column=4)
        self.amount6 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount6.grid(row=7,column=5)
        self.price6 = Label(self.master, text="", width=6, justify='right', bg="skyblue", height=1, font=1)
        self.price6.grid(row=7, column=6)
        self.labelOder.append(self.order6)
        self.labelList.append(self.list6)
        self.labelAmount.append(self.amount6)
        self.labelPrice.append(self.price6)
        self.order7 = Label(self.master,text="7",width=4,anchor='w',justify='left',bg="skyblue",height=1,font=1)
        self.order7.grid(row=8,column=3)
        self.list7 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list7.grid(row=8, column=4)
        self.amount7 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount7.grid(row=8,column=5)
        self.price7 = Label(self.master, text="", width=6, justify='right', bg="skyblue", height=1, font=1)
        self.price7.grid(row=8, column=6)
        self.labelOder.append(self.order7)
        self.labelList.append(self.list7)
        self.labelAmount.append(self.amount7)
        self.labelPrice.append(self.price7)
        self.order8 = Label(self.master,text="8",width=4,anchor='w',justify='left',bg="skyblue",height=1,font=1)
        self.order8.grid(row=9,column=3)
        self.list8 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list8.grid(row=9, column=4)
        self.amount8 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount8.grid(row=9,column=5)
        self.price8 = Label(self.master,text="",width=6,justify='right',bg="skyblue",height=1,font=1)
        self.price8.grid(row=9,column=6)
        self.labelOder.append(self.order8)
        self.labelList.append(self.list8)
        self.labelAmount.append(self.amount8)
        self.labelPrice.append(self.price8)
        self.order9 = Label(self.master, text="9", width=4, anchor='w', justify='left', bg="skyblue", height=1, font=1)
        self.order9.grid(row=10, column=3)
        self.list9 = Label(self.master, text="", width=11, justify='left', bg="skyblue", height=1, font=1)
        self.list9.grid(row=10, column=4)
        self.amount9 = Label(self.master, text="", width=5, justify='left', bg="skyblue", height=1, font=1)
        self.amount9.grid(row=10, column=5)
        self.price9 = Label(self.master, text="", width=6, justify='right', bg="skyblue", height=1, font=1)
        self.price9.grid(row=10, column=6)
        self.labelOder.append(self.order9)
        self.labelList.append(self.list9)
        self.labelAmount.append(self.amount9)
        self.labelPrice.append(self.price9)
        self.order10 = Label(self.master, text="รวม", width=4, anchor='w', justify='left', bg="skyblue", height=1, font=1)
        self.order10.grid(row=11, column=3)
        self.list10 = Label(self.master,text="",width=11,justify='left',bg="skyblue",height=1,font=1)
        self.list10.grid(row=11,column=4)
        self.amount10 = Label(self.master,text="",width=5,justify='left',bg="skyblue",height=1,font=1)
        self.amount10.grid(row=11,column=5)
        self.price10 = Label(self.master,text="",width=6,justify='right',bg="skyblue",height=1,font=1)
        self.price10.grid(row=11,column=6)
        self.labelOder.append(self.order10)
        self.labelList.append(self.list10)
        self.labelAmount.append(self.amount10)
        self.labelPrice.append(self.price10)

    def report_Day(self):
        x = datetime.datetime.now()
        nameFile = str(x.year) + str(x.month) + str(x.day) + "billramen"
        path = "C:\\Users\\lenovo\\Documents\\BillRamen\\"

        df = pd.read_csv(path + nameFile + ".txt", sep='\t', header=None,names=['เมนู', 'จำนวน','ราคา'])
        df.to_excel(path + nameFile + 'output.xlsx', index=False)

    def writeBill(self):
        x = datetime.datetime.now()
        nameFile = str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second) + "billramen"
        path = "C:\\Users\\lenovo\\Documents\\BillRamen\\"
        f = open(path + nameFile + ".txt", "w" , encoding="utf-8")
        f.write("---------------------------\n")
        f.write("	ร้าน ราแมะราแมะ\n")
        f.write("---------------------------\n")
        f.write(str(x) + "\n")
        f.write("รายการ	จำนวน	ราคา\n")
        tempTable = []
        if self.tabelNumber.cget("text") == "โต๊ะ1":
            tempTable = self.table1
        elif self.tabelNumber.cget("text") == "โต๊ะ2":
            tempTable = self.table2
        elif self.tabelNumber.cget("text") == "โต๊ะ3":
            tempTable = self.table3
        elif self.tabelNumber.cget("text") == "โต๊ะ4":
            tempTable = self.table4
        elif self.tabelNumber.cget("text") == "โต๊ะ5":
            tempTable = self.table5
        elif self.tabelNumber.cget("text") == "โต๊ะ6":
            tempTable = self.table6

        i = 0
        sum = 0
        total = 0
        te = ""
        while i < len(tempTable):
            t = tempTable[i][1] + "\t" + tempTable[i][2] + "\t" + tempTable[i][3] +"\tบาท\n"
            te = tempTable[i][1] + "\t" + tempTable[i][2] + "\t" + tempTable[i][3] +"\n"
            sum += int(tempTable[i][2])
            total += int(tempTable[i][3])
            i += 1
            f.write(t)
        f.write("รวม\t" + str(sum) + "\t" + str(total) + "\tบาท\n")
        f.write("---------------------------\n")
        f.write("	     ขอบคุณครับ\n")
        f.write("---------------------------\n")
        f.close()

        nameFile = str(x.year) + str(x.month) + str(x.day) + "billramen"
        f = open(path + nameFile + ".txt", "a", encoding="utf-8")
        i = 0
        while i < len(tempTable):
            t = tempTable[i][1] + "\t" + tempTable[i][2] + "\t" + tempTable[i][3] + "\n"
            sum += int(tempTable[i][2])
            total += int(tempTable[i][3])
            i += 1
            f.write(t)
        f.close()



        tableName = self.tabelNumber.cget("text")
        if tableName == "โต๊ะ1":
            self.table1.clear()
        elif tableName == "โต๊ะ2":
            self.table2.clear()
        elif tableName == "โต๊ะ3":
            self.table3.clear()
        elif tableName == "โต๊ะ4":
            self.table4.clear()
        elif tableName == "โต๊ะ5":
            self.table5.clear()
        elif tableName == "โต๊ะ6":
            self.table6.clear()

        n = 0
        for i in self.labelOder:
            i.config(text=str(n + 1))
            n += 1

        for i in self.labelList:
            i.config(text="")

        n = 0
        for i in self.labelAmount:
            i.config(text="")

            if n == 9:
                i.config(text="0")
            n += 1

        n = 0
        for i in self.labelPrice:
            i.config(text="")

            if n == 9:
                i.config(text="0")
            n += 1

    def py2_unicode_to_str(u):
        import sys
        # unicode is only exist in python2
        assert isinstance(u, unicode)
        return u.encode('utf-8')

    def clearTable(self):
        tableName = self.tabelNumber.cget("text")
        if tableName == "โต๊ะ1":
            self.table1.clear()
        elif tableName == "โต๊ะ2":
            self.table2.clear()
        elif tableName == "โต๊ะ3":
            self.table3.clear()
        elif tableName == "โต๊ะ4":
            self.table4.clear()
        elif tableName == "โต๊ะ5":
            self.table5.clear()
        elif tableName == "โต๊ะ6":
            self.table6.clear()

        n = 0
        for i in self.labelOder:
            i.config(text=str(n + 1))
            n += 1

        for i in self.labelList:
            i.config(text="")

        n = 0
        for i in self.labelAmount:
            i.config(text="")

            if n == 9:
                i.config(text="0")
            n += 1

        n = 0
        for i in self.labelPrice:
            i.config(text="")

            if n == 9:
                i.config(text="0")
            n += 1



    def showTanble1(self):
        self.tabelNumber.config(text="โต๊ะ1")
        n = 0
        for i in self.labelOder:
            if n < len(self.table1):
                i.config(text=self.table1[n][0])
            else:
                i.config(text=str(n + 1))
            n += 1
            if n == 9:
                break

        n = 0
        for i in self.labelList:
            if n < len(self.table1):
                i.config(text=self.table1[n][1])
            else:
                i.config(text="")
            n += 1
            if n == 9:
                break

        n = 0
        count = 0
        for i in self.labelAmount:
            if n < len(self.table1):
                i.config(text=self.table1[n][2])
                count += int(self.table1[n][2])
            else:
                i.config(text="")
            if n == 9:
                i.config(text=count)
            n += 1

        n = 0
        total = 0
        for i in self.labelPrice:
            if n < len(self.table1):
                i.config(text=self.table1[n][3])
                total += int(self.table1[n][3])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=total)
            n += 1

    def showTanble2(self):
        self.tabelNumber.config(text="โต๊ะ2")
        n = 0
        for i in self.labelOder:
            if n < len(self.table2):
                i.config(text=self.table2[n][0])
            else:
                i.config(text=str(n + 1))
            n += 1
            if n == 9:
                break

        n = 0
        for i in self.labelList:
            if n < len(self.table2):
                i.config(text=self.table2[n][1])
            else:
                i.config(text="")
            n += 1
            if n == 9:
                break

        n = 0
        count = 0
        for i in self.labelAmount:
            if n < len(self.table2):
                i.config(text=self.table2[n][2])
                count += int(self.table2[n][2])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=count)
            n += 1

        n = 0
        total = 0
        for i in self.labelPrice:
            if n < len(self.table2):
                i.config(text=self.table2[n][3])
                total += int(self.table2[n][3])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=total)
            n += 1
    # leftClickButton(event):
        #pass
    def showTanble3(self):
        self.tabelNumber.config(text="โต๊ะ3")
        n = 0
        for i in self.labelOder:
            if n < len(self.table3):
                i.config(text=self.table3[n][0])
            else:
                i.config(text=str(n + 1))
            n += 1
            if n == 9:
                break

        n = 0
        for i in self.labelList:
            if n < len(self.table3):
                i.config(text=self.table3[n][1])
            else:
                i.config(text="")
            n += 1
            if n == 9:
                break

        n = 0
        count = 0
        for i in self.labelAmount:
            if n < len(self.table3):
                i.config(text=self.table3[n][2])
                count += int(self.table3[n][2])
            else:
                i.config(text="")
            if n == 9:
                i.config(text=count)
            n += 1

        n = 0
        total = 0
        for i in self.labelPrice:
            if n < len(self.table3):
                i.config(text=self.table3[n][3])
                total += int(self.table3[n][3])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=total)
            n += 1
    def showTanble4(self):
        self.tabelNumber.config(text="โต๊ะ4")
        n = 0
        for i in self.labelOder:
            if n < len(self.table4):
                i.config(text=self.table4[n][0])
            else:
                i.config(text=str(n + 1))
            n += 1
            if n == 9:
                break

        n = 0
        for i in self.labelList:
            if n < len(self.table4):
                i.config(text=self.table4[n][1])
            else:
                i.config(text="")
            n += 1
            if n == 9:
                break

        n = 0
        count = 0
        for i in self.labelAmount:
            if n < len(self.table4):
                i.config(text=self.table4[n][2])
                count += int(self.table4[n][2])
            else:
                i.config(text="")
            if n == 9:
                i.config(text=count)
            n += 1

        n = 0
        total = 0
        for i in self.labelPrice:
            if n < len(self.table4):
                i.config(text=self.table4[n][3])
                total += int(self.table4[n][3])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=total)
            n += 1
    def showTanble5(self):
        self.tabelNumber.config(text="โต๊ะ5")
        n = 0
        for i in self.labelOder:
            if n < len(self.table5):
                i.config(text=self.table5[n][0])
            else:
                i.config(text=str(n + 1))
            n += 1
            if n == 9:
                break

        n = 0
        for i in self.labelList:
            if n < len(self.table5):
                i.config(text=self.table5[n][1])
            else:
                i.config(text="")
            n += 1
            if n == 9:
                break

        n = 0
        count = 0
        for i in self.labelAmount:
            if n < len(self.table5):
                i.config(text=self.table5[n][2])
                count += int(self.table5[n][2])
            else:
                i.config(text="")
            if n == 9:
                i.config(text=count)
            n += 1

        n = 0
        total = 0
        for i in self.labelPrice:
            if n < len(self.table5):
                i.config(text=self.table5[n][3])
                total += int(self.table5[n][3])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=total)
            n += 1
    def showTanble6(self):
        self.tabelNumber.config(text="โต๊ะ6")
        n = 0
        for i in self.labelOder:
            if n < len(self.table6):
                i.config(text=self.table6[n][0])
            else:
                i.config(text=str(n + 1))
            n += 1
            if n == 9:
                break

        n = 0
        for i in self.labelList:
            if n < len(self.table6):
                i.config(text=self.table6[n][1])
            else:
                i.config(text="")
            n += 1
            if n == 9:
                break

        n = 0
        count = 0
        for i in self.labelAmount:
            if n < len(self.table6):
                i.config(text=self.table6[n][2])
                count += int(self.table6[n][2])
            else:
                i.config(text="")
            if n == 9:
                i.config(text=count)
            n += 1

        n = 0
        total = 0
        for i in self.labelPrice:
            if n < len(self.table6):
                i.config(text=self.table6[n][3])
                total += int(self.table6[n][3])
            else:
                i.config(text="")

            if n == 9:
                i.config(text=total)
            n += 1

    def showRamenMenu(self):
        root = Tk()
        root.geometry("460x465+500+150")
        root.title("เมนูราเมง")
        root["bg"] = "royalblue4"
        app = RamenMenu(root, self.app)
        app.create_widgets()
        root.mainloop()

    def showReportMenu(self):
        root = Tk()
        root.geometry("460x465+500+150")
        root.title("เมนูรายงาน")
        app = ReportMenu(root, self.app)
        app.create_widgets()
        root.mainloop()

    def showPromotionMenu(self):
        root = Tk()
        root.geometry("460x465+500+150")
        root.title("เมนูโปรโมชั่น")
        root["bg"] = "royalblue4"
        app = PromotionMenu(root, self.app)
        app.create_widgets()
        root.mainloop()

    def showDrinkMenu(self):
        root = Tk()
        root.geometry("460x465+500+150")
        root.title("เมนูเครื่องดื่ม")
        root["bg"] = "royalblue4"
        app = DrinkMenu(root, self.app)
        app.create_widgets()
        root.mainloop()

    def showSoupMenu(self):
        root = Tk()
        root.geometry("460x465+500+150")
        root.title("เมนูซุป")
        root["bg"] = "royalblue4"
        app = SoupMenu(root, self.app)
        app.create_widgets()
        root.mainloop()

    def showAppetizerMenu(self):
        root = Tk()
        root.geometry("460x465+500+150")
        root.title("เมนูอาหารว่าง")
        root["bg"] = "royalblue4"
        app = AppetizerMenu(root, self.app)
        app.create_widgets()
        root.mainloop()

    def showConfirmMenu(self):
        root = Tk()
        root.geometry("620x250+450+300")
        root["bg"] = "skyblue"
        app = ConfirmMenu(root, self.app, "1")
        app.create_widgets()
        root.mainloop()

    def showConfirmReport(self):
        root = Tk()
        root.geometry("620x250+450+300")
        root["bg"] = "skyblue"
        app = ConfirmMenu(root, self.app, "2")
        app.create_widgets()
        root.mainloop()

    def setApp(self, a):
        self.app = a

mainWindow = Tk()
mainWindow.geometry("777x660+350+50")
mainWindow.title("POSRAMEN by Saharat Areewong")
app = MainRamen(mainWindow)
app.create_widgets()
app.setApp(app)
mainWindow.mainloop()