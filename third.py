a=int(input("Enter a number:"))
# if(num%5==0):
#     print("it is divisible by 5")
# else:
#    print("It is not dividsible by 5")
if(a>=0 and a<=9):
    print("single digit")

elif(a>=10 and a<=99):
    print("double digit")

elif(a>=100 and a<=999):
    print("triple digit")

else:
    print("multiple digit")
