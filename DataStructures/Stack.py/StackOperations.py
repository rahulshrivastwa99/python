Stack = []


def stack_empty():
    return len(Stack) == 0


def push_Stack():
    element = int(input("Enter the element to push: "))
    Stack.append(element)
    print(f"{element} pushed to stack..")


def pop_Stack():
    if not len(Stack) == 0:
        print(f"{Stack.pop()} popped from stack..")
        print(Stack)
    else:
        print("Stack is empty..")


def peek_Stack():
    if len(Stack) != 0:
        print(f"Top element of stack is {Stack[-1]}")
    else:
        print("Stack is Empty")


def size_Stack():
    print(f"Size of stack is {len(Stack)}")


def display_Stack():
    print(f"Stack elements are {Stack}")


while True:
    print("\n📋 Stack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        push_Stack()
    elif choice == 2:
        pop_Stack()
    elif choice == 3:
        peek_Stack()
    elif choice == 4:
        size_Stack()
    elif choice == 5:
        display_Stack()
    elif choice == 6:
        print("👋 Exiting the program. Goodbye!")
        break  # 🔁 This will stop the loop and exit the program
    else:
        print("❗ Invalid choice. Please enter a number from 1 to 6.")
