from datetime import datetime
from tkinter import *
from tkcalendar import Calendar,DateEntry
import os

class ReportMenu(Frame):
    def __init__(self, reportMenu,main):
        """ Initialise the Frame. """
        self.master = reportMenu
        self.mainW = main

    def create_widgets(self):

        self.text = Label(self.master, text="ตั้งแต่ วันที่", anchor='w', justify='left', height=1, font=1)
        self.text.place(relx = 0.3,rely = 0.3,anchor = 'center')
        self.text1 = Label(self.master, text="ถึง วันที่", anchor='w', justify='left', height=1,font=1)
        self.text1.place(relx = 0.3,rely = 0.5,anchor = 'center')
        self.text2 = Entry(self.master,width=25)
        self.datestar = DateEntry(self.master, width=25, bg="darkblue", fg="white", year=2021)
        self.datestar.place(relx = 0.6,rely = 0.3,anchor = 'center')
        self.dateend = DateEntry(self.master, width=25, bg="darkblue", fg="white", year=2021)
        self.dateend.place(relx = 0.6,rely = 0.5,anchor = 'center')
        self.button_confirm = Button(self.master, text="ยืนยัน", width=10, height=1, command=self.exportFile)
        self.button_confirm.place(relx = 0.3,rely = 0.8,anchor = 'center')
        self.button_back = Button(self.master, text="ย้อนกลับ", width=10, height=1,
                                  command=self.master.destroy)
        self.button_back.place(relx=0.6, rely=0.8, anchor='center')

    def exportFile(self):
        #print(str(self.datestar.get_date().year))
        path = "C:\Program Files\\BillRamen\\"
        DayStart = str(self.datestar.get_date().year) + str(self.datestar.get_date().month) + str(self.datestar.get_date().day)
        DayEnd = str(self.dateend.get_date().year) + str(self.dateend.get_date().month) + str(self.dateend.get_date().day)


        f = open(path + DayStart + " - " + DayEnd + " Report.txt", "w", encoding="utf-8")
        f.write("---------------------------\n")
        f.write("รายงานประจำวัน\n")
        f.write("	ร้าน ราแมะราแมะ\n")
        f.write("วันเริ่มต้น:\t" + str(self.datestar.get_date()) + "\n")
        f.write("วันที่สิ้นสุด:\t" + str(self.dateend.get_date()) + "\n")
        f.write("---------------------------\n")
        #f.write("รายการ	จำนวน	ราคา\n")

        yS = int(self.datestar.get_date().year)
        mS = int(self.datestar.get_date().month)
        dS = int(self.datestar.get_date().day)
        yE = int(self.dateend.get_date().year)
        mE = int(self.dateend.get_date().month)
        dE = int(self.dateend.get_date().day)
        date_obj = datetime(int(yS), int(mS), int(dS))
        s = open(path + "Report\\" + str(yS) + str(mS) + str(dS) + " Report.txt", "r", encoding="utf-8")
        f.write(s.read())
        f.write("\n")
        s.close()
        dS += 1

        while date_obj != datetime(int(yE), int(mE), int(dE)):
            try:
                date_obj = datetime(int(yS), int(mS), int(dS))
                #print(path + str(yS) + str(mS) + str(dS) + " Report.txt")
                s = open(path + "Report\\" + str(yS) + str(mS) + str(dS) + " Report.txt", "r", encoding="utf-8")
                f.write(s.read())
                f.write("\n")
                s.close()
                dS += 1
            except:
                dS = 1
                mS += 1
                if (mS > 12):
                    mS = 1
                    yS += 1
        f.close()
        os.startfile(path + DayStart + " - " + DayEnd + " Report.txt")
