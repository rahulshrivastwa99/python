# ------------------------
# 1. Arithmetic Operators
# ------------------------
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)           # 13
print("Subtraction:", a - b)        # 7
print("Multiplication:", a * b)     # 30
print("Division:", a / b)           # 3.333...
print("Floor Division:", a // b)    # 3
print("Modulus:", a % b)            # 1
print("Exponentiation:", a ** b)    # 1000
print()

# ------------------------
# 2. Comparison Operators
# ------------------------
x = 5
y = 10

print("Comparison Operators:")
print("Equal:", x == y)             # False
print("Not equal:", x != y)         # True
print("Greater than:", x > y)       # False
print("Less than:", x < y)          # True
print("Greater or equal:", x >= y) # False
print("Less or equal:", x <= y)     # True
print()

# ------------------------
# 3. Logical Operators
# ------------------------
p = True
q = False

print("Logical Operators:")
print("AND:", p and q)              # False
print("OR:", p or q)                # True
print("NOT:", not p)                # False
print()

# ------------------------
# 4. Bitwise Operators
# ------------------------
m = 5   # 0b0101
n = 3   # 0b0011

print("Bitwise Operators:")
print("AND:", m & n)                # 1 (0101 & 0011 = 0001)
print("OR:", m | n)                 # 7 (0101 | 0011 = 0111)
print("XOR:", m ^ n)                # 6 (0101 ^ 0011 = 0110)
print("NOT:", ~m)                   # -6
print("Left Shift:", m << 1)        # 10 (0101 << 1 = 1010)
print("Right Shift:", m >> 1)       # 2 (0101 >> 1 = 0010)
print()

# ------------------------
# 5. Assignment Operators
# ------------------------
z = 5

print("Assignment Operators:")
z += 2
print("+= :", z)                    # 7
z -= 1
print("-= :", z)                    # 6
z *= 3
print("*= :", z)                    # 18
z /= 2
print("/= :", z)                    # 9.0
z //= 2
print("//= :", z)                   # 4.0
z %= 3
print("%= :", z)                    # 1.0
z **= 2
print("**= :", z)                   # 1.0
print()

# ------------------------
# 6. Identity Operators
# ------------------------
a = [1, 2]
b = a
c = [1, 2]

print("Identity Operators:")
print("a is b:", a is b)            # True
print("a is c:", a is c)            # False
print("a is not c:", a is not c)    # True
print()

# ------------------------
# 7. Membership Operators
# ------------------------
my_list = [1, 2, 3, 4]

print("Membership Operators:")
print("2 in my_list:", 2 in my_list)      # True
print("5 not in my_list:", 5 not in my_list)  # True
