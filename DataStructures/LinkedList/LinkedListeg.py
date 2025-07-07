#Creation of a Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None



#Creation of a Linked list:
class LinkedList:
     def __init__(self):
         self.head = None
         self.n = 0 #stores the number of nodes in the linked list

     #Traversal operation in linked list
     def traverse(self):
         if self.head == None:
             print("Linked list is empty")
         else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end = " ")
                n = n.ref
            print()  # newline after traversal

     #Insertion at the beginning of the LL:
     def insert_at_beginning(self, data):
         new_node = Node(data)
         new_node.ref = self.head
         self.head = new_node
         self.n += 1
         
     # Insertion at the end of the LL:
     def insert_at_end(self, data):
         new_node = Node(data)
         if self.head is None:
            self.head = new_node
         else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
         self.n += 1
         
     # Insertion after a  specific position in the LL:
     def insert_after(self, data, prev_node):
         n = self.head
         while n is not None:
             if prev_node == n.data:
                 break
             n = n.ref
         if n is None:
             print("Node is not present in LinkedList ")
         else:
             new_node = Node(data)
             new_node.ref = n.ref
             n.ref = new_node
     
         
         
         
LL1 = LinkedList()
LL1.insert_at_beginning(30)
LL1.insert_at_beginning(50)
LL1.insert_at_end(55)
LL1.insert_at_end(65)
LL1.insert_after(60, 55 )
LL1.traverse()
