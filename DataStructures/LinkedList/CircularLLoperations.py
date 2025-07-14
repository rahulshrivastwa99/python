#Creation of a Circular singly Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
#Creation of circular singly liked list:
class CircularSingly:
     def __init__(self):
        self.head = None
        self.n = 0  # stores the no. of total nodes in linked list present
        
    #Traversal operation in linked list
     def traverse(self):
         if self.head == None:
             print("Linked list is empty")
         else:
            n = self.head
            while True:
                print(n.data, "-->", end = " ")
                n = n.ref
                if n == self.head:
                    return
            print()  # newline after traversal
            
     #Insertion When LinkedList is completely empty:
     def insert_empty(self, data):
         if self.head == None:
             new_node = Node(data) # Create the new node
             new_node.ref = new_node   # For a circular linked list, point next to itself
             self.head = new_node
             self.n += 1
         else:
             print("\nLinked List is not empty")

     #Insertion at the beginning of the LL:
     def insert_at_beginning(self, data):
         new_node = Node(data)
         if not self.head:
            self.head = new_node
            new_node.ref = self.head
            self.n += 1
         else:   
             n = self.head
             while n.ref != self.head:
                n = n.ref
             new_node.ref = self.head
             self.head = new_node
             n.ref = self.head
             self.n += 1
         
      # Insertion at the end of the LL:
     def insert_at_end(self, data):
         new_node = Node(data)
         if not self.head:
            self.head = new_node
            new_node.ref = self.head
            self.n += 1
         else:
            n = self.head
            while n.ref is not self.head:
                n = n.ref
            n.ref = new_node
            new_node.ref = self.head
            self.n += 1    


      # Insertion after a  specific position in the LL:
     def insert_after(self, data, prev_node):
         n = self.head
         while True:
             if prev_node == n.data:
                 new_node = Node(data)
                 new_node.ref = n.ref
                 n.ref = new_node
                 self.n += 1
                 return
             n = n.ref
             if n == self.head:
                 break
             print(f"Node with data {prev_node} not found")


     # Insertion before a given node in Singly Circular Linked List
     def insert_before(self, data, next_node):
        # Case 0: Empty list
         if self.head is None:
            print("List is empty")
            return

         n = self.head

    # Case 1: Insert before head node
         if n.data == next_node:
            new_node = Node(data)
         # Traverse to the last node
            while n.ref != self.head:
                n = n.ref
            new_node.ref = self.head
            n.ref = new_node
            self.head = new_node
            self.n += 1
            return

    # Case 2: Insert before a middle node
         prev = self.head
         curr = self.head.ref
         while curr != self.head:
            if curr.data == next_node:
                new_node = Node(data)
                new_node.ref = curr
                prev.ref = new_node
                self.n += 1
                return
            prev = curr
            curr = curr.ref

    # Case 3: Node not found
         print("Node is not present in LinkedList")

             
             
                    
            

SCLL = CircularSingly()

# SCLL.insert_empty(12)
# # SCLL.insert_empty(14)
SCLL.insert_at_beginning(13)
SCLL.insert_at_beginning(17)
SCLL.insert_at_beginning(19)
# SCLL.insert_at_end(11)
# SCLL.insert_after(18, 19)
SCLL.insert_before(12, 19)
print("Number of total nodes:", SCLL.n)
SCLL.traverse()

