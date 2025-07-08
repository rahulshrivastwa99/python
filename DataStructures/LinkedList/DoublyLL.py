# ---------------------------------------------
# 📘 DOUBLY LINKED LIST — CODE WITH NOTES
# ---------------------------------------------

# 🔹 A Doubly Linked List (DLL) contains nodes where each node has:
#     - data
#     - pointer to the next node (next)
#     - pointer to the previous node (prev)
# 🔹 Allows bidirectional traversal (forward & backward)

# ---------------------------------------------
# 🔸 Node structure for DLL
# ---------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # Stores the data
        self.prev = None      # Points to the previous node
        self.next = None      # Points to the next node

# ---------------------------------------------
# 🔸 Doubly Linked List structure
# ---------------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Head of the list

    # ---------------------------------------------
    # 🔹 Traverse forward
    # ---------------------------------------------
    def display_forward(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <--> ")
                temp = temp.next
            print("None")

    # ---------------------------------------------
    # 🔹 Traverse backward
    # ---------------------------------------------
    def display_backward(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            # Go to the last node
            while temp.next:
                temp = temp.next
            # Traverse in reverse
            while temp:
                print(temp.data, end=" <--> ")
                temp = temp.prev
            print("None")

    # ---------------------------------------------
    # 🔹 Insert at the beginning
    # ---------------------------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # ---------------------------------------------
    # 🔹 Insert at the end
    # ---------------------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    # ---------------------------------------------
    # 🔹 Delete from beginning
    # ---------------------------------------------
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

    # ---------------------------------------------
    # 🔹 Delete from end
    # ---------------------------------------------
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.prev.next = None


DLL = DoublyLinkedList()

DLL.insert_at_beginning(24)
DLL.insert_at_beginning(64)
DLL.insert_at_beginning(34)

DLL.display_forward()
DLL.display_backward()