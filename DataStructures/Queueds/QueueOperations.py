class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def enqueue(self, item):
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
        print(self.queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.dequeue()
q.display()

q.enqueue(4)
q.enqueue(5)
q.dequeue()

q.is_empty()
q.display()
q.show_front()
q.show_rear()

print("Queue size:", q.size_queue())
