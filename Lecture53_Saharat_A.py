def Vat7(pirce):
    result = pirce+(pirce*7/100)
    return result
print(Vat7(int(input("Totalpirce:"))))