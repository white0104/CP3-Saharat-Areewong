menuList = []
priceList = []
def showBill():
    print('-----MY Food-----')
    for x in range(len(menuList)):
        print(menuList[x],priceList[x])
def Total():
    sum = 0
    for i in range(len(priceList)):
        sum += priceList[i]
    print(sum)
while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = (int(input("Price:")))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
Total()