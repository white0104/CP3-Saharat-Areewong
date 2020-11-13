o = int(input())
for x in range(o+1) :
    a = " "
    a = a * (o-x)
    for i in range(x+1):
        y = ""
        y = "*"*(i+x-1)
    print(a,y)
