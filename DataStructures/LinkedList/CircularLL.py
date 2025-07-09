""" 🔁 1. What is a Circular Linked List?
A Circular Linked List is a variation of the linked list where:
The last node points back to the first node (instead of None).
Forms a circle of nodes — no null at the end.

📌 2. Types of Circular Linked Lists
Singly Circular Linked List
    Each node has one pointer (next)
    Last node’s next points to head

Doubly Circular Linked List
    Each node has next and prev
    Last node’s next → head
    Head node’s prev → last node

🔧 3. Key Operations in CLL
a. Traversal
Start from head and keep moving until you return to head again.

b. Insertion
At beginning: Insert new node and adjust the last node’s pointer to point to the new head.

At end: Traverse to the last node and make it point to the new node, and new node → head.

After a given node: Insert after the given node, adjust pointers accordingly.

c. Deletion
Handle carefully to maintain circular nature:

If deleting head, update last node’s pointer

If deleting middle or end, skip the node

If only one node, set head to None

"""



# ==========================
# 🌐 SINGLY CIRCULAR LINKED LIST
# ==========================

# Node class for Singly Circular Linked List
class SCLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to manage operations on SCLL
class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    # 🔁 Traversal of SCLL (loops until we return to head)
    def traverse(self):
        if not self.head:
            print("Singly Circular Linked List is empty")
            return
        n = self.head
        while True:
            print(n.data, end=" ---> ")
            n = n.next
            if n == self.head:
                break
        print()

    # ➕ Insert at the end of SCLL
    def insert_end(self, data):
        new_node = SCLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Circular reference
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head

    # ➕ Insert at beginning of SCLL
    def insert_beginning(self, data):
        new_node = SCLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            new_node.next = self.head
            self.head = new_node
            n.next = self.head

    # ❌ Delete a node by value
    def delete_by_value(self, value):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == value:
            if self.head.next == self.head:  # Only one node
                self.head = None
                return
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print("Value not found in list")

# ==========================
# 🔁 DOUBLY CIRCULAR LINKED LIST
# ==========================

# Node class for Doubly Circular Linked List
class DCLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # Forward reference
        self.prev = None  # Backward reference

# Class to manage operations on DCLL
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # 🔁 Traverse forward
    def traverse_forward(self):
        if not self.head:
            print("Doubly Circular Linked List is empty")
            return
        n = self.head
        while True:
            print(n.data, end=" <---> ")
            n = n.next
            if n == self.head:
                break
        print()

    # 🔁 Traverse backward
    def traverse_backward(self):
        if not self.head:
            print("List is empty")
            return
        n = self.head
        # Move to last node
        while n.next != self.head:
            n = n.next
        # Now traverse back
        while True:
            print(n.data, end=" <---> ")
            n = n.prev
            if n.next == self.head:
                print(n.data, end=" <---> ")
                break
        print()

    # ➕ Insert at end
    def insert_end(self, data):
        new_node = DCLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    # ➕ Insert at beginning
    def insert_beginning(self, data):
        new_node = DCLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    # ❌ Delete a node by value
    def delete_by_value(self, value):
        if not self.head:
            print("List is empty")
            return

        n = self.head
        found = False
        while True:
            if n.data == value:
                found = True
                break
            n = n.next
            if n == self.head:
                break

        if not found:
            print("Value not found")
            return

        if n.next == n:  # Only one node
            self.head = None
            return

        if n == self.head:
            self.head = n.next

        n.prev.next = n.next
        n.next.prev = n.prev

# ==========================
# ✅ DEMO
# ==========================

print("🔁 Singly Circular Linked List:")
scll = SinglyCircularLinkedList()
scll.insert_end(10)
scll.insert_end(20)
scll.insert_beginning(5)
scll.traverse()
scll.delete_by_value(20)
scll.traverse()

print("\n🔁 Doubly Circular Linked List:")
dcll = DoublyCircularLinkedList()
dcll.insert_end(100)
dcll.insert_end(200)
dcll.insert_beginning(50)
print("Traverse forward:")
dcll.traverse_forward()
print("Traverse backward:")
dcll.traverse_backward()
dcll.delete_by_value(100)
print("Traverse forward:")
dcll.traverse_forward()
