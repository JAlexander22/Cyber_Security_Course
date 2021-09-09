First_Num = ""
Second_Num = ""
Div = ""
while First_Num != 0:
    print("Enter first Number")
    First_Num = int(input())
    print ("Enter Second Number")
    Second_Num = int(input())
    print ("________________________")


    Sum = (First_Num+Second_Num)
    Mul = (First_Num*Second_Num)
    Sub = (First_Num-Second_Num)
    try:
        Div = (First_Num/Second_Num)
        pass
    except ZeroDivisionError:
        print ("Divide by 0 Error")
    break
    print(Sum)
    print(Mul)
    print(Sub)
    print(Div)


