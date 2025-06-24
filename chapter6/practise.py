#program to find the greatest of 4 no.. entered by user 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
#find the greatest of 4 no.. entered by user
if (num1 > num2 and num1 > num3 and num1 > num4):
    print("The greatest number is", num1)
    
elif (num2 > num1 and num2 > num3 and num2 > num4):
    print("The greatest number is", num2)
    
elif (num3 > num1 and num3 > num2 and num4 > num4):
    print("The greatest number is", num3)
    
else:
    print("The greatest number is", num4)
