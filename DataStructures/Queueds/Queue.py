# ----------------------------------------------------------
# QUEUE DATA STRUCTURE – FULL CONCEPTUAL NOTES IN COMMENTS
# ----------------------------------------------------------

# ✅ WHAT IS A QUEUE?
# A Queue is a **linear data structure** that follows the
# **FIFO (First In, First Out)** principle.
# That means the element that is inserted first will be removed first.

# ✅ REAL-LIFE EXAMPLES:
# - People standing in a line (first person is served first)
# - Print queue
# - CPU scheduling in Operating Systems
# - Call center systems (first call answered first)

# ✅ KEY QUEUE OPERATIONS:
# 1. Enqueue  -> Add element at the rear (end)
# 2. Dequeue  -> Remove element from the front (beginning)
# 3. Peek     -> Get front element without removing it
# 4. isEmpty  -> Check if queue is empty
# 5. Size     -> Number of elements in the queue
# 6. Display  -> Print all elements from front to rear

# ✅ TYPES OF QUEUES:
# - Simple Queue (FIFO)
# - Circular Queue
# - Double Ended Queue (Deque)
# - Priority Queue

# ----------------------------------------------------------
# ✅ SIMPLE QUEUE IMPLEMENTATION USING PYTHON LIST
# ----------------------------------------------------------

Queue = []  # This list will act as our Queue

# Check if the queue is empty


def is_empty():
    # Return True if the queue has no elements
    return len(Queue) == 0

# Enqueue operation: add an element at the end of the queue


def enqueue():
    item = input("Enter the item to enqueue: ")
    Queue.append(item)
    print(f"✅ {item} has been added to the queue.")

# Dequeue operation: remove an element from the front of the queue


def dequeue():
    if is_empty():
        print("❌ Queue Underflow! Cannot dequeue from empty queue.")
    else:
        item = Queue.pop(0)
        print(f"🗑️  {item} has been removed from the queue.")

# Peek operation: view the front element without removing it


def peek():
    if is_empty():
        print("⚠️ Queue is empty.")
    else:
        print(f"🔍 Front element is: {Queue[0]}")

# Size operation: check how many elements are in the queue


def size():
    print(f"📦 Size of the queue is: {len(Queue)}")

# Display operation: print all elements from front to rear


def display():
    if is_empty():
        print("📭 Queue is empty.")
    else:
        print("📃 Queue from front to rear:", Queue)

# ----------------------------------------------------------
# ✅ APPLICATIONS OF QUEUE IN COMPUTER SCIENCE
# ----------------------------------------------------------

# 🔹 CPU & Disk Scheduling (Round Robin)
# 🔹 Breadth First Search (BFS) in Graphs
# 🔹 Handling of real-time data (IoT data processing)
# 🔹 Messaging systems, Chat servers
# 🔹 I/O Buffers (input/output management)
# 🔹 Printer Queue in Operating Systems

# ----------------------------------------------------------
# ✅ MENU DRIVEN INTERFACE TO TEST QUEUE
# ----------------------------------------------------------


if __name__ == "__main__":
    while True:
        print("\n📋 Queue Operations Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            enqueue()
        elif choice == "2":
            dequeue()
        elif choice == "3":
            peek()
        elif choice == "4":
            size()
        elif choice == "5":
            display()
        elif choice == "6":
            print("👋 Exiting Queue Program. Bye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")
