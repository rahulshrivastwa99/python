# Taking input as a string
name = input("Enter your name: ")
print("Hello,", name)

# Taking an integer input
age = int(input("Enter your age: "))  # input() gives string, so we convert to int
print("You will be", age + 1, "next year.")


# Taking a float input
price = float(input("Enter the price: "))
print("The price with 18% tax is:", price * 1.18)


# Taking two numbers in a single line separated by space
a, b = map(int, input("Enter two numbers separated by space: ").split())
print("Sum:", a + b)


# Input a list of integers
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("List entered:", nums)
