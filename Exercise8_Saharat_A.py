usernameInput = input("UserName :")
passwordInput = input("Password :")
if usernameInput == "saharat" and passwordInput == "123" :
    print("----Welcome Saharat-----")
    Water = 12
    banana = 10
    sprite = 20
    print("1.Water")
    print("2.Banana")
    print(("3.Sprite"))
    userSelected = int(input(">>"))
    if userSelected == 1 :
        WaterVol = int(input("ใส่จำนวนทน้ำี่ต้องการ:"))
        print("total :", Water*WaterVol,"THB")
    elif userSelected == 2 :
        bananaVol = int(input("ใส่จำนวนกล้วยที่ต้องการ:"))
        print("total :", banana*bananaVol,"THB")
    elif userSelected == 3 :
        spriteVol = int(input("ใส่จำนวนสไปร์ทที่ต้องการ:"))
        print("total :", sprite*spriteVol,"THB")
print("-----Thank You------")
