from tkinter import *
import math
BMI=0
def leftClickButton(event):
    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)
    print(BMI)
    if BMI > 30 :
        labelResult.configure(text="อ้วนมาก")
    elif BMI >25:
        labelResult.configure(text="อ้วน")
    elif BMI > 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif BMI > 18.6:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif BMI <= 18.5:
        labelResult.configure(text="ผอมเกินไป")

main = Tk()
labelHight =Label(main,text="ส่วนสูง(cm.):")
labelHight.grid(row=0,column=0)
textBoxHight =Entry(main)
textBoxHight.grid(row=0,column=1)
labelWeight =Label(main,text="น้ำหนัก(Kg.):")
labelWeight.grid(row=1,column=0)
textBoxWeight =Entry(main)
textBoxWeight.grid(row=1,column=1)
calculateButton=Button(main,text="คำนวน",)
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult =Label(main,text="ผลลัพ")
labelResult.grid(row=2,column=1)
main.mainloop()