# 📘 What is a Stack? (In Detail)
# A stack is a linear data structure that follows the LIFO principle — Last In, First Out.
# -------------------------
# 🔁 LIFO Explained:
# The last element inserted (pushed) into the stack is the first one to be removed (popped).
# Think of a stack of plates — you add plates on top, and you also remove from the top.
# ----------------------------------------
# 📚 Characteristics of Stack
# Linear: Elements are ordered in a sequence.

# Dynamic size (in Python list implementation).

# Allows access to only the top element.
# --------------------------------------------
# Operations are performed only on one end — the top of the stack.

# 🔧 Basic Stack Operations
# Operation	Description
# push()	Adds an element to the top
# pop()	Removes the top element
# peek()	Views the top element without removing
# is_empty()	Checks if the stack is empty
# size()	Returns total number of elements
# display()	Prints elements from bottom to top


# STACK IMPLEMENTATION USING PYTHON LIST {Array}

class Stack:
    def __init__(self):
        # Initialize an empty list for the stack
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self):
        # Add an item to the top of the stack using user input
        item = input("Enter the item to push: ")
        self.stack.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        # Remove and return the top item of the stack
        if self.is_empty():
            print("❌ Stack Underflow! Cannot pop from an empty stack.")
            return None
        popped_item = self.stack.pop()
        print(f"✅ Popped item: {popped_item}")
        return popped_item

    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            print("⚠️ Stack is empty. Nothing to peek.")
            return None
        print(f"🔝 Top element: {self.stack[-1]}")
        return self.stack[-1]

    def size(self):
        # Return the number of elements in the stack
        print(f"📦 Current stack size: {len(self.stack)}")
        return len(self.stack)

    def display(self):
        # Display the current elements of the stack
        if self.is_empty():
            print("📭 Stack is empty.")
        else:
            print("📦 Stack from bottom to top:", self.stack)


# ----------------------------
# TESTING THE STACK OPERATIONS
# ----------------------------
if __name__ == "__main__":
    s = Stack()

    while True:
        print("\n📋 Choose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            s.push()
        elif choice == "2":
            s.pop()
        elif choice == "3":
            s.peek()
        elif choice == "4":
            s.display()
        elif choice == "5":
            s.size()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❗ Invalid choice. Please try again.")

  # Creating an object of Stack

#     # Display initial state
#     s.display()

#     # Push elements to the stack
#     s.push(10)
#     s.push(20)
#     s.push(30)

#     # Display the stack
#     s.display()

#     # Peek at the top element
#     print("Top element is:", s.peek())

#     # Pop elements from the stack
#     s.pop()
#     s.pop()

#     # Display after pops
#     s.display()

#     # Check the size
#     print("Current size of stack:", s.size())

#     # Final pop and one extra to check underflow
#     s.pop()
#     s.pop()  # This should show underflow message

#     # Final state
#     s.display()

# STACK IMPLEMENTATION USING PYTHON Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class StackLinkedList:
#     def __init__(self):
#         self.top = None

#     def push(self, item):
#         new_node = Node(item)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if not self.is_empty():
#             popped_node = self.top
#             self.top = self.top.next
#             return popped_node.data
#         return None

#     def peek(self):
#         if not self.is_empty():
#             return self.top.data
#         return None

#     def is_empty(self):
#         return self.top is None

#     def size(self):
#         count = 0
#         current = self.top
#         while current:
#             count += 1
#             current = current.next
#         return count

#       # Create a stack instance
# s = StackLinkedList()

# # Call push to add elements
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(45)
# s.push(55)
# s.push(65)

# # Call peek to see the top element
# print("Stack top element:", s.peek())


# # Call pop to remove the top element
# print("Popped Elements:")
# print(s.pop())   # Output: 30
# print(s.pop())   # Output: 30

# # Check if stack is empty
# print("Stack is empty : True or False?")
# print(s.is_empty())  # Output: False
# print("Size of current stack is:", s.size())  # Output: False
