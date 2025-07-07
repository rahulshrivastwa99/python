# Function to find the nth Fibonacci number using recursion
def fibonacci(n):
    # Base case 1: The 0th Fibonacci number is 0
    # Base case 2: The 1st Fibonacci number is 1
    if (n<2):
        return n
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# -------- Main Program --------

# Take input from user
n = int(input("Enter a number to get its nth Fibonacci value: "))

# Call the recursive function and print the result
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
