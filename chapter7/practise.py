# # #program to print multiplication atable of even numbers

# # n = int(input("Enter a Number: "))
# # for i in range (1, 11):
# #     print(f"{n} X {i} = {n * i}")
    
# # #print all the name strt with r
# # l = ["Rahul", "Rohan", "Sourav", "Suraj"]
 
# # for name in l:
# #     if name.startswith('R'):
# #         print(f"Hello {name}")
        
# # #table with using while loop

# # n = int(input("Enter a Number: "))
# # i = 1
# # while(i<11):
# #     print(f"{n} X {i} = {n * i}")
# #     i += 1
    
# # # given no is prime or not

# n = int(input("Enter a Number: "))
# for i in range (1, n):
#     if(n%i) == 0:
#         print(f"{n} is not a prime number")
      
      
# program to do a factorial of a number  
# n = int(input("Enter the number: "))  # Take input from the user
# product = 1                           # Start with 1 (neutral for multiplication)

# for i in range(1, n+1):               # Loop from 1 to n (inclusive)
#     product *= i                      # Multiply product by i on each loop

# print(f"The factorial of {n} is {product}")  # Output the result

n  = int(input("Enter the Number: "))
for i in range(1, n+1):
    print(" "* (n-i), end= "")
    print("$"* (2*i-1), end= "")
    print("\n")
    
    
n  = int(input("Enter the Number: "))
for i in range(1, n+1):
    print("#"* i, end= "")
    print("")
    
    