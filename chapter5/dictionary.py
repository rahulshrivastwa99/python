# ---------------------------------------------------
# ✅ COMPLETE DICTIONARY NOTES IN PYTHON (with CODE)
# ---------------------------------------------------

# ▶ What is a dictionary?
# A dictionary is an ordered*, mutable, and indexed collection of key-value pairs.
# Keys must be unique and immutable (str, int, tuple); values can be any type.

# ✅ Dictionary Properties:
# --------------------------
# 1. Ordered (from Python 3.7+)
# 2. Mutable (can change after creation)
# 3. Unique keys (duplicates get overwritten)
# 4. Keys must be immutable (e.g., str, int, tuple)
# 5. Values can be any data type
# 6. Supports nesting (dict inside dict)

# -----------------------------------------
# 1. Creating Dictionaries
# -----------------------------------------
print("1️⃣ Creating Dictionaries")

empty = {}  # Empty dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "branch": "CSE"
}
print("Student Dictionary:", student)
print()

# -----------------------------------------
# 2. Accessing Values
# -----------------------------------------
print("2️⃣ Accessing Values")

print("Name:", student["name"])         # Using key
print("Age (safe):", student.get("age"))  # Using .get()
print("Unknown key:", student.get("marks"))  # Returns None
print()

# -----------------------------------------
# 3. Updating / Adding Items
# -----------------------------------------
print("3️⃣ Updating and Adding")

student["age"] = 22                     # Update value
student["college"] = "BPIT"            # Add new key
print("Updated Dictionary:", student)
print()

# -----------------------------------------
# 4. Deleting Items
# -----------------------------------------
print("4️⃣ Deleting Items")

student.pop("branch")                  # Remove specific key
del student["college"]                 # Another way to remove key
print("After deletion:", student)

student.clear()                        # Removes all items
print("After clear():", student)
print()

# -----------------------------------------
# 5. Dictionary Methods
# -----------------------------------------
print("5️⃣ Dictionary Methods")

info = {
    "name": "Rahul",
    "age": 21,
    "branch": "CSE"
}

print("Keys:", info.keys())           # Returns dict_keys object
print("Values:", info.values())       # Returns dict_values object
print("Items:", info.items())         # Returns (key, value) pairs

# update() method
info.update({"age": 22, "college": "BPIT"})
print("After update:", info)
print()

# -----------------------------------------
# 6. Looping Through Dictionary
# -----------------------------------------
print("6️⃣ Looping through Dictionary")

for key in info:
    print(f"{key} => {info[key]}")

print("\nUsing items():")
for k, v in info.items():
    print(f"{k} => {v}")
print()

# -----------------------------------------
# 7. Nested Dictionary
# -----------------------------------------
print("7️⃣ Nested Dictionaries")

students = {
    "rahul": {"age": 21, "branch": "CSE"},
    "ankit": {"age": 22, "branch": "ECE"}
}

print("Rahul's Branch:", students["rahul"]["branch"])
print()

# -----------------------------------------
# 8. Valid and Invalid Keys
# -----------------------------------------
print("8️⃣ Valid/Invalid Keys")

valid = {
    "str": "okay",
    100: "int key",
    (1, 2): "tuple key"
}
print("Valid keys:", valid)

# ❌ Invalid key example (would raise error)
# invalid = {[1, 2]: "list key"}  # ❌ Lists can't be keys
print()

# -----------------------------------------
# 9. Real-Life Use Case: Word Counter
# -----------------------------------------
print("9️⃣ Real-life Use: Word Frequency Counter")

text = "apple banana apple mango banana apple"
words = text.split()
counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

print("Word Count:", counter)
print()

# -----------------------------------------
# 🔟 Summary Table (in comments only)
# -----------------------------------------

# ✅ Common Dictionary Methods:
# - get(key)        → Returns value or None
# - pop(key)        → Removes and returns value
# - clear()         → Removes all items
# - keys()          → Returns all keys
# - values()        → Returns all values
# - items()         → Returns all (key, value) pairs
# - update(dict2)   → Merges another dictionary

# ✅ Common Use Cases:
# - Word frequency
# - Student records
# - Contact books
# - JSON-like nested data
