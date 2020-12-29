from tkinter import *
from tkinter import ttk
from datetime import datetime
from forex_python.converter import CurrencyRates
def average_forex(event):
    c = CurrencyRates()
    year  = int(year_start.get())
    month = int(month_start.get())
    day = int(day_start.get())
    date_obj = datetime(int(year), int(month), int(day))
    #result = c.convert('USD', 'THB', 1, date_obj)
    sum = 0
    totalday = 0
    while date_obj != datetime(int(year_end.get()), int(month_end.get()), int(day_end.get())):

        try:
            date_obj = datetime(int(year), int(month), int(day))
            result = c.convert(forex1.get(), forex2.get(), 1, date_obj)
            totalday += 1
            sum += result
            print(date_obj, " , ", result)
            day += 1

        except:
            day = 1
            month += 1
            if (month > 12):
                month = 1
                year += 1

    print(sum)
    print(totalday)
    sum = sum / totalday

    labelResult.configure(text=sum)

main = Tk()
forexvar1 = StringVar()
forex1 = ttk.Combobox(main, textvariable=forexvar1)
forex1['values'] = ("CNY", "EUR", "USD","THB","JPY","GBP")
textForex1 = Label(text="ค่าเงินที่ต้องการจะเปรียบเทียบ" ).grid(column=0,row=1)
forex1.grid(column = 1, row = 1)
forex1.current()
forexvar2 = StringVar()
forex2 = ttk.Combobox(main, textvariable=forexvar2)
forex2['values'] = ("CNY", "EUR", "USD","THB","JPY","GBP")
textForex2 = Label(text="ค่าเงินที่ต้องการจะเปรียบเทียบ" ).grid(column=0,row=2)
forex2.grid(column = 1, row = 2)
forex2.current()
yearvar_start = StringVar()
year_start = ttk.Combobox(main, textvariable=yearvar_start)
year_start['values'] = (2015,2016, 2017,2018,2019,2020)
year_start.grid(column = 1, row = 3)
year_start.current()
monthvar_start = StringVar()
month_start = ttk.Combobox(main, textvariable=monthvar_start)
month_start['values'] = (1, 2, 3,4,5,6,7,8,9,10,11,12)
month_start.grid(column = 2, row = 3)
month_start.current()
dayvar_start = StringVar()
day_start = ttk.Combobox(main, textvariable=dayvar_start)
day_start['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
day_start.grid(column = 3, row = 3)
day_start.current()
textdate_start = Label(text="ปี/เดือน/วัน" ).grid(column=0,row=3)
yearvar_end = StringVar()
year_end = ttk.Combobox(main, textvariable=yearvar_end)
year_end['values'] = (2015,2016, 2017,2018,2019,2020)
year_end.grid(column = 1, row = 4)
year_end.current()
monthvar_end = StringVar()
month_end = ttk.Combobox(main, textvariable=monthvar_end)
month_end['values'] = (1, 2, 3,4,5,6,7,8,9,10,11,12)
month_end.grid(column = 2, row = 4)
month_end.current()
dayvar_end = StringVar()
day_end = ttk.Combobox(main, textvariable=dayvar_end)
day_end['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
day_end.grid(column = 3, row = 4)
day_end.current()
textdate_end = Label(text="ปี/เดือน/วัน" ).grid(column=0,row=4)
labelResult =Label(main,text="ค่าเฉลี่ย")
labelResult.grid(row=5,column=1)
calculateButton=Button(main,text="คำนวน",)
calculateButton.bind('<Button-1>',average_forex)
calculateButton.grid(row=5,column=0)

main.mainloop()