num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))



def greatest(num1, num2, num3):
    if(num1>num2 and num1>num3):
        print("num1 is greatest: ", num1)
    elif(num2>num1 and num2>num3):
        print("num2 is greatest: ", num2)
    else:
        print("num3 is greatest: ", num3)

greatest(num1, num2, num3)

#program to convert celsius to frehenhit

def tempchange(f):
    return (f-32) * 5/9

f = int(input("Enter the Temperature in F: "))
print(f"{tempchange(f)}°")
