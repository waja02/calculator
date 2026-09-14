num1=float(input("Enter first num :"))
operator=input("enter any sign(+, -, *, /) :")
num2=float(input("Enter second num :"))
if operator=="+":
    print("Result", num1+num2)
elif operator=="-":
    print("Result", num1-num2)
elif operator=="*":
    print("Result", num1*num2)
elif operator=="/":
    if num2 !=0:
        print("Result", num1/num2)
    else:
        print("numer is not disvalid")
else:
    print("invalid character")