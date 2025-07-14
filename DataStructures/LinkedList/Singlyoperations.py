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

     #Insertion When LinkedList is completely empty:
     def insert_empty(self, data):
         if self.head == None:
             new_node = Node(data)
             self.head = new_node
             self.n += 1
         else:
             print("Linked List is not empty")
             
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
             self.n += 1
             
       #Insertion at before the given node     
     def insert_before(self, data, next_node):
         n = self.head
         if n is None:
            print("Linked List is empty ")
            return

     # Special case: inserting before head
         if n.data == next_node:
            new_node = Node(data)
            new_node.ref = n
            self.head = new_node
            self.n += 1
            return

     # Traverse to find node before the target
         while n.ref is not None:
            if n.ref.data == next_node:
            # Target found, insert here
                 new_node = Node(data)
                 new_node.ref = n.ref
                 n.ref = new_node
                 self.n += 1
                 return
            n = n.ref
     # After loop: target not found
         else:
            print("Node is not present in LinkedList ")

     # Deletion of the 1st node in linkedlist:
     def delete_first(self):
         if self.head == None:
             print("Linked List is empty ")
             return 
         self.head = self.head.ref
         self.n -= 1
    
     #Deletion of last node in the linkedlist:
     def delete_last(self):
         if self.head is None:
             print("LinkedList is Empty")
         elif self.head.ref is None:
             self.head = None
             self.n -= 1
         else:
             n = self.head
             while n.ref.ref != None:
                 n = n.ref
             n.ref = None    
             self.n -=  1
     # Deletion by the value in LinkedList:                
     def  delete_by_value(self, value):
         if self.head is None:
             print("LinkedList is empty")   
             return        
         if value == self.head.data:
             self.head = self.head.ref
             self.n -= 1
             return
         n = self.head
         while n.ref is not None:
             if value == n.ref.data:
                 break
             n = n.ref
         if n.ref is None:
             print("Node is not present in LinkedList")  
         else:
             n.ref = n.ref.ref    
             self.n -= 1
        
        
                    
              

LL1 = LinkedList()
print("start")
LL1.insert_empty(10)
LL1.insert_at_beginning(30)
LL1.insert_at_end(55)
print("beggining operations ")
LL1.insert_after(60, 55 )
LL1.insert_before(10, 55)
LL1.delete_last()
LL1.delete_first()
LL1.delete_by_value(25)
LL1.delete_by_value(30)
LL1.delete_by_value(10)
LL1.traverse()
print("Number of nodes:", LL1.n)
print ("end")

# LL1.insert_at_end(65)
# LL1.insert_after(990, 30 )
# LL1.insert_before(90, 60)
# LL1.insert_before(2000, 50)
# LL1.insert_before(1000, 70)

