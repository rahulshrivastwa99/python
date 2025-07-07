# -------------------------------------------
# Function to check if a number is prime
# -------------------------------------------
def isPrime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False  # 0 and 1 are not prime numbers

    # Loop from 2 to square root of n (inclusive)
    # No need to check beyond √n, as factors repeat after that
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any i in this range, it's not a prime
        if n % i == 0:
            return False  # Found a divisor, so not prime

    # If no divisor found, number is prime
    return True

# -------------------------------------------
# Main Program
# -------------------------------------------

# Ask the user to enter a natural number
n = int(input("Enter a natural number to check for prime: "))

# Call the is_prime function and display result
if isPrime(n):
    print(f"{n} is a Prime number.")
else:
    print(f"{n} is NOT a Prime number.")
