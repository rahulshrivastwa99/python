# Define a function named fibonacci that takes one parameter `n`
# `n` represents how many numbers of the Fibonacci sequence we want
def fibonacci(n):
    # Initialize an empty list to store the Fibonacci sequence
    fib_seq = []
    
    # Start with the first two Fibonacci numbers: 0 and 1
    a, b = 0, 1
    
    # Run a loop n times to generate the first n Fibonacci numbers
    for _ in range(n):
        # Append the current value of `a` to the sequence
        fib_seq.append(a)
        
        # Update `a` and `b` to the next two numbers in the sequence
        # `a` becomes current `b`, and `b` becomes current `a + b`
        a, b = b, a + b

    # After the loop ends, return the complete sequence
    return fib_seq


# -------- Main Program --------

# Ask the user to enter a number and convert the input from string to integer
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the fibonacci() function with input `n` and print the returned list
print(f"The first {n} Fibonacci numbers are: {fibonacci(n)}")
