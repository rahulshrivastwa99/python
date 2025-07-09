# ------------------------------------------------------------
# 📘 Linked List in Python – Notes Included in Comments
# ------------------------------------------------------------

# 🔹 A Linked List is a linear data structure where each element (node)
#    points to the next node using a pointer (reference).
# 🔹 It's made up of nodes, where each node contains:
#    - data: the actual value
#    - next: a pointer to the next node

# ✅ Node Class: Represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # stores data (value of node)
        self.next = None      # stores reference to the next node


# ✅ LinkedList Class: Contains operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None      # head points to the first node in the list

    # --------------------------------------------------------
    # 🔹 Insert a node at the beginning (O(1) time)
    # --------------------------------------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node points to current head
        self.head = new_node        # head is now the new node

    # --------------------------------------------------------
    # 🔹 Insert a node at the end (O(n) time)
    # --------------------------------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:       # if list is empty, make new node head
            self.head = new_node
            return
        last = self.head
        while last.next:            # traverse to the last node
            last = last.next
        last.next = new_node        # point last node to new node

    # --------------------------------------------------------
    # 🔹 Insert a node at a specific position (0-based index)
    # --------------------------------------------------------
    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):  # move to (pos-1)th node
            if current is None:
                raise Exception("Position out of bounds")
            current = current.next
        new_node.next = current.next   # link new node to next
        current.next = new_node        # link previous node to new node

    # --------------------------------------------------------
    # 🔹 Delete a node by value
    # --------------------------------------------------------
    def delete_by_value(self, value):
        current = self.head
        if current is not None and current.data == value:
            self.head = current.next   # move head to next node
            return
        prev = None
        while current is not None and current.data != value:
            prev = current
            current = current.next
        if current is None:
            return  # value not found
        prev.next = current.next  # unlink node to delete it

    # --------------------------------------------------------
    # 🔹 Search for an element in the list
    # --------------------------------------------------------
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True       # found
            current = current.next
        return False              # not found

    # --------------------------------------------------------
    # 🔹 Print the entire linked list
    # --------------------------------------------------------
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # --------------------------------------------------------
    # 🔹 Reverse the linked list (Iterative Method)
    #    Time Complexity: O(n), Space: O(1)
    # --------------------------------------------------------
    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next     # store next node
            current.next = prev          # reverse current node's pointer
            prev = current               # move prev one step forward
            current = next_node          # move current one step forward
        self.head = prev                 # update head to the new front

    # --------------------------------------------------------
    # 🔹 Reverse the linked list (Recursive Method)
    #    Time Complexity: O(n), Space: O(n) due to recursion stack
    # --------------------------------------------------------
    def reverse_recursive(self, node):
        if node is None or node.next is None:
            return node
        rest = self.reverse_recursive(node.next)  # reverse the rest
        node.next.next = node     # point next node back to current
        node.next = None          # current node becomes last
        return rest

    def reverse(self):
        self.head = self.reverse_recursive(self.head)

    # --------------------------------------------------------
    # 🔹 Get the length of the linked list
    # --------------------------------------------------------
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
