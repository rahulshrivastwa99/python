# #program to create a dictionary of hindi words with values as the english transalation,
#    #usr can input the hindi word and get the english translation

# words = {
#     "madad": "Help",
#     "kursi": "Chair",
#     "billi": "Cat"
# }

# word = input("Enter the word you want meaning of: ")
# print(words[word])

# #write a program to input eight nos on the user and display all uniques no's in once
# # Program to input 8 numbers from the user and display unique numbers
# s = set()

# for i in range(8):
#     n = int(input(f"Enter number {i + 1}: "))
#     s.add(n)  # Only unique values will be stored

# print("Unique numbers entered:", s)

# Program to create a dictionary of 4 friends and their favorite languages

# d = {}

# for i in range(4):
#     name = input(f"Enter friend {i + 1}'s name: ")
#     lang = input(f"Enter {name}'s favorite language: ")
#     d[name] = lang  # OR d.update({name: lang})

# print("\nFriend -> Language:")
# print(d)

# or inchance the name is same of two friends

entries = []

for i in range(4):
    name = input(f"Enter friend {i + 1}'s name: ")
    lang = input(f"Enter {name}'s favorite language: ")
    entries.append((name, lang))

print("\nAll entries (with possible duplicate names):")
for name, lang in entries:
    print(f"{name} => {lang}")


