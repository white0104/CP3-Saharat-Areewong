from tkinter import *
import datetime
import pandas as pd
import csv


class ConfirmMenu(Frame):
    def __init__(self, confirmMenu,main,n):
        """ Initialise the Frame. """
        self.master = confirmMenu
        self.mainW = main
        self.header = n
        if n == "1":
            self.textLabel = "ต้องการจะชำระเงินใช่ไหม ?"
        elif n == "2":
            self.textLabel = "ต้องการจะสรุปยอดใช่ไหม ?"

    def create_widgets(self):

        self.text = Label(self.master, text=self.textLabel, anchor='w', justify='left', height=1, font=1,bg="skyblue")
        self.text.place(relx = 0.5,rely = 0.3,anchor = 'center')
        self.button_confirm = Button(self.master, text="ยืนยัน", width=12, height=3,font=1,bg="green" ,command=self.writeBill)
        self.button_confirm.place(relx = 0.3,rely = 0.7,anchor = 'center')
        self.button_back = Button(self.master, text="ย้อนกลับ", width=12, height=3,font=1,bg="red",
                                  command=self.master.destroy)
        self.button_back.place(relx=0.7, rely=0.7, anchor='center')

    def writeBill(self):
        #ชำระรายการอาหาร
        if self.header == "1":
            x = datetime.datetime.now()
            nameFile = str(x.year) + str(x.month) + str(x.day) + str(x.hour) + str(x.minute) + str(x.second) + "billramen"
            path = "C:\Program Files\\BillRamen\\"
            f = open(path + "Bill\\" + nameFile + ".txt", "w" , encoding="utf-8")
            f.write("---------------------------\n")
            f.write("	ร้าน ราแมะราแมะ\n")
            f.write("---------------------------\n")
            f.write(str(x) + "\n")
            f.write("รายการ	จำนวน	ราคา\n")
            tempTable = []
            if self.mainW.tabelNumber.cget("text") == "โต๊ะ1":
                tempTable = self.mainW.table1
            elif self.mainW.tabelNumber.cget("text") == "โต๊ะ2":
                tempTable = self.mainW.table2
            elif self.mainW.tabelNumber.cget("text") == "โต๊ะ3":
                tempTable = self.mainW.table3
            elif self.mainW.tabelNumber.cget("text") == "โต๊ะ4":
                tempTable = self.mainW.table4
            elif self.mainW.tabelNumber.cget("text") == "โต๊ะ5":
                tempTable = self.mainW.table5
            elif self.mainW.tabelNumber.cget("text") == "โต๊ะ6":
                tempTable = self.mainW.table6

            i = 0
            sum = 0
            total = 0
            while i < len(tempTable):
                t = tempTable[i][1] + "\t" + str(tempTable[i][2]) + "\t" + str(tempTable[i][3]) +"\tบาท\n"
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
            f = open(path + "Log\\" + nameFile + ".txt", "a", encoding="utf-8")
            i = 0
            while i < len(tempTable):
                t = tempTable[i][1] + "\t" + str(tempTable[i][2]) + "\t" + str(tempTable[i][3]) + "\n"
                sum += int(tempTable[i][2])
                total += int(tempTable[i][3])
                i += 1
                f.write(t)
            f.close()

            tableName = self.mainW.tabelNumber.cget("text")
            if tableName == "โต๊ะ1":
                self.mainW.table1.clear()
            elif tableName == "โต๊ะ2":
                self.mainW.table2.clear()
            elif tableName == "โต๊ะ3":
                self.mainW.table3.clear()
            elif tableName == "โต๊ะ4":
                self.mainW.table4.clear()
            elif tableName == "โต๊ะ5":
                self.mainW.table5.clear()
            elif tableName == "โต๊ะ6":
                self.mainW.table6.clear()

            n = 0
            for i in self.mainW.labelOder:
                i.config(text=str(n + 1))
                n += 1

            for i in self.mainW.labelList:
                i.config(text="")

            n = 0
            for i in self.mainW.labelAmount:
                i.config(text="")

                if n == 9:
                    i.config(text="0")
                n += 1

            n = 0
            for i in self.mainW.labelPrice:
                i.config(text="")

                if n == 9:
                    i.config(text="0")
                n += 1
        elif self.header == "2":
            #สรุปยอดขายประจำวัน
            #export excel
            x = datetime.datetime.now()
            nameFile = str(x.year) + str(x.month) + str(x.day)
            path = "C:\Program Files\\BillRamen\\"

            df = pd.read_csv(path + "Log\\" + nameFile + "billramen.txt", sep='\t', header=None, names=['เมนู', 'จำนวน', 'ราคา'])
            df.to_excel(path + nameFile + 'output.xlsx', index=False)
            #print(str(df.values[0,2]))
            i = 0
            total = 0 #จำนวนเงินที่ได้ทั้งวัน
            temp = []
            while i < len(df):
                if len(temp) == 0:
                    t = [df.values[i,0],df.values[i,1],df.values[i,2]]
                    temp.append(t)
                else:
                    j = 0
                    while j < len(temp):
                        if str(temp[j][0]) == df.values[i,0]:
                            temp[j][1] += df.values[i, 1]
                            temp[j][2] += df.values[i, 2]
                            break
                        j += 1

                        if j == len(temp):
                            t = [df.values[i, 0], df.values[i, 1], df.values[i, 2]]
                            temp.append(t)
                            break

                total += int(df.values[i,2])
                i += 1

            f = open(path + "Log\\" + nameFile + "billramen.txt", "w", encoding="utf-8")
            i = 0
            while i < len(temp):
                t = str(temp[i][0]) + "\t" + str(temp[i][1]) + "\t" + str(temp[i][2]) + "\n"
                i += 1
                f.write(t)
            f.write("รวม\t\t" + str(total))
            f.close()

            #export textfile for print
            f = open(path + "Report\\"+ nameFile + " Report.txt", "w", encoding="utf-8")
            f.write("---------------------------\n")
            f.write("รายงานประจำวัน\n")
            f.write("	ร้าน ราแมะราแมะ\n")
            f.write("วันที่:\t" + str(x) + "\n")
            f.write("---------------------------\n")
            f.write("รายการ	จำนวน	ราคา\n")
            s = open(path + "Log\\" + nameFile + "billramen.txt", "r", encoding="utf-8")
            f.write(s.read())
            s.close()

            f.close()


        self.button_confirm.after(1, self.master.destroy)