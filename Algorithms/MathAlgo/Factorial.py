# Function to compute factorial of a number
def factorial(n):
    # Edge case: factorial of 0 is 1
    if n == 0:
        return 1

    # Initialize result variable to 1
    result = 1

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Multiply result by current number i
        result *= i

    # Return the final factorial value
    return result


# -------- Main Program --------

# Take input from the user and convert it to an integer
n = int(input("Enter a number to find its factorial: "))

# Call the function and print the result
print(f"The factorial of {n} is: {factorial(n)}")
