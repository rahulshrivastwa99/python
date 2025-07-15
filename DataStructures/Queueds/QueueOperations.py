class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def enqueue(self):
        item = int(input("Enter item to enqueue: "))
        self.queue.append(item)
        print(f"Enqueued item: {item}")
        print("Queue after enqueue:", self.queue)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            removed = self.queue.pop(0)
            print(f"Popped item: {removed}")
            print("Queue after popping:", self.queue)

    def show_rear(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Rear element:", self.queue[-1])

    def show_front(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("front element:", self.queue[0])

    def size_queue(self):
        return len(self.queue)

    def display(self):
        if len(self.queue) == 0:
            print("Queue cant be displayed")
        else:
            print(self.queue)


q = Queue()

# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.display()
# q.dequeue()
# q.display()

# q.enqueue(4)
# q.enqueue(5)
# q.dequeue()

# q.is_empty()
# q.display()
# q.show_front()
# q.show_rear()

# print("Queue size:", q.size_queue())

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Check if empty")
    print("5. Show front")
    print("6. Show rear")
    print("7. Size")
    print("8. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        q.enqueue()
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        q.is_empty()
    elif choice == 5:
        q.show_front()
    elif choice == 6:
        q.show_rear()
    elif choice == 7:
        print("Queue size:", q.size_queue())
    elif choice == 8:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
