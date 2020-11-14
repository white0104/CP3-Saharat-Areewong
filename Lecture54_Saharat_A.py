def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelected()
def menuSelected() :
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vatCalculate(price)
    elif userSelected == 2:
        priceCalculate()
    return userSelected
def vatCalculate (price):
    vat = 7
    result = price + (price * vat / 100)
    return print(result)
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)
login()