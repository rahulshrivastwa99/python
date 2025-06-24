# ------------------------------------
# STRING OPERATIONS IN PYTHON
# ------------------------------------

# Strings are sequences of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' / """ """)
s = "Hello, Python!"

# -----------------------------
# 1. Accessing Characters
# -----------------------------
print("1. Accessing Characters:")
print("First character:", s[0])       # Indexing starts at 0
print("Last character:", s[-1])       # Negative indexing from end
print()

# -----------------------------
# 2. Slicing Strings
# -----------------------------
print("2. Slicing Strings:")
print("s[0:5]:", s[0:5])              # Slice from index 0 to 4 (5 excluded)
print("s[:5]:", s[:5])                # Same as s[0:5]
print("s[7:]:", s[7:])                # From index 7 to end
print("s[-7:-1]:", s[-7:-1])          # Slicing with negative index
print()

# -----------------------------
# 3. String Length function 
# -----------------------------
print("3. String Length:")
print("Length of string:", len(s))    # Number of characters
print()

# -----------------------------
# 4. String Concatenation
# -----------------------------
print("4. String Concatenation:")
a = "Hello"
b = "World"
print("Concatenated:", a + " " + b)   # Combine strings using +
print()

# -----------------------------
# 5. String Repetition
# -----------------------------
print("5. String Repetition:")
print("Repeat 'Hi' 3 times:", "Hi" * 3)
print()

# -----------------------------
# 6. Membership Operators
# -----------------------------
print("6. Membership Check:")
print("'Python' in s:", "Python" in s)  # True
print("'Java' not in s:", "Java" not in s)  # True
print()

# -----------------------------
# 7. String Comparison
# -----------------------------
print("7. String Comparison:")
print("'apple' == 'Apple':", 'apple' == 'Apple')  # Case sensitive
print("'abc' < 'bcd':", 'abc' < 'bcd')            # Lexicographical comparison
print()

# -----------------------------
# 8. Looping through String
# -----------------------------
print("8. Loop through String:")
for char in a:
    print(char, end=' ')              # Print each character in 'a'
print("\n")

# -----------------------------
# 9. String Methods
# -----------------------------
sample = "  python programming  "

print("9. String Methods:")
print("Original:", sample)
print("Lowercase:", sample.lower())         # Convert to lowercase
print("Uppercase:", sample.upper())         # Convert to uppercase
print("Title Case:", sample.title())        # Capitalize first letters
print("Strip (remove spaces):", sample.strip())  # Remove leading/trailing spaces
# print("Replace 'python' with 'java':", samp


name = "Rahul"
age = 21

# f-string format
print(f"My name is {name} and I am {age} years old.")
