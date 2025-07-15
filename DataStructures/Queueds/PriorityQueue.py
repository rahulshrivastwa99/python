# 🔰 PRIORITY QUEUE NOTES:

# 1. A priority queue is a special type of queue where elements are ordered based on priority.
# 2. Elements with higher priority are dequeued before elements with lower priority.
#    ➤ Lower numerical value means higher priority (e.g., 1 is higher than 3)
# 3. Implemented using `heapq` in Python which provides a min-heap by default.
# 4. Basic operations:
#    - Enqueue: Use `heapq.heappush(queue, (priority, item))`
#    - Dequeue: Use `heapq.heappop(queue)` to get the item with the lowest priority number
#    - Peek: Access `queue[0]` to look at the item with the highest priority
# 5. Time complexity:
#    - Enqueue and Dequeue: O(log n)
#    - Peek: O(1)


import heapq  # Python module for heap queue algorithm (priority queue)


class PriorityQueue:
    def __init__(self):
        # We use a list to store queue elements as a heap
        self.queue = []

    def is_empty(self):
        # A priority queue is empty if its list is empty
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        """
        ✅ Enqueue: Adds an element to the priority queue
        - Python's heapq uses a **min-heap**, so the element with the **lowest number** (highest priority)
          is served first.
        - We push a tuple: (priority, item)
        """
        heapq.heappush(self.queue, (priority, item))
        print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        """
        ✅ Dequeue: Removes and returns the element with the **highest priority**
        - That means the element with the **lowest priority number**
        """
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            priority, item = heapq.heappop(self.queue)
            print(f"Dequeued: {item} (Priority: {priority})")

    def peek(self):
        """
        ✅ Peek: Shows the element with the highest priority without removing it
        - Just looks at the top element of the min-heap
        """
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            priority, item = self.queue[0]
            print(f"Front of queue: {item} (Priority: {priority})")

    def display(self):
        """
        ✅ Display: Shows the entire queue as a list of (priority, item)
        - The internal order may not be sorted (because it's a heap structure), but the dequeue
          will always give the correct priority order
        """
        if self.is_empty():
            print("Priority Queue is empty")
        else:
            print("Priority Queue contents:")
            for priority, item in self.queue:
                print(f"Item: {item}, Priority: {priority}")


# 📌 Demo usage
pq = PriorityQueue()
pq.enqueue("Rahul", 2)
pq.enqueue("Shrivastwa", 1)
pq.enqueue("Student", 3)

pq.display()
pq.peek()
pq.dequeue()
pq.display()
