# Function to check if n is a power of 2 and return its power if true
def power_of_two(n):
    # Power of 2 must be positive
    if n <= 0:
        return False

    power = 0  # To keep track of the exponent

    # Keep dividing n by 2 while it is divisible
    while n % 2 == 0:
        n = n // 2
        power += 1  # Increase the power count

    # If the final result is 1, it was a power of 2
    if n == 1:
        return True, power
    else:
        return False

# -------- Main Program --------

# Take input from user
n = int(input("Enter a positive integer: "))

# Call the function
is_pow2, power = power_of_two(n)

# Print the result
if is_pow2:
    print(f"{n} is a power of 2 (2^{power}).")
else:
    print(f"{n} is NOT a power of 2.")
