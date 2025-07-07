def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, n + 1):
        total = a + b
        a, b = b, total

    return b

# -------- Main Program --------
n = int(input("Enter how many stairs you want to climb: "))

ways = climbStairs(n)
print(f"There are {ways} distinct ways to climb {n} stairs.")
