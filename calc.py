def menu():
    print("**********CALCULATOR***********")
    a=int(input("Enter 1st no:"))
    b=int(input("Enter 2nd no:"))
    print('-------------------------------')
    print("Enter + for addition")
    print("Enter - for subtraction")
    print("Enter * for multiplication")
    print("Enter / for division")
    print('--------------------------------')
    ch=input("Enter symbol:")
    
    if ch=='+':
        print("Result is :",a+b)
    elif ch=="-":
        print("Result is :",a-b)
    elif ch=="*":
        print("Result is :",a*b)
    elif ch=="/":
        print("Result is :",a/b)

    else:
        print("invalid symbol !")

while True:
    menu()


