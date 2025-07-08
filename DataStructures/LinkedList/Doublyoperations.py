#Creation of a Node o dobly linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.prev = None


#Creation of DLL
class DoublyLL:
     def __init__(self):
         self.head = None
         self.n = 0 #stores the number of nodes in the linked list

#Traversal in Foward Direction
     def f_Traverse(self):
         if self.head == None:
             print("Linked list is empty")
         else:
            n = self.head
            while n is not None:
                print(n.data, "-->",end = " " )
                n = n.nref
            print()  # newline after traversal

     #  Traversal in reverse direction:       
     def r_Traverse(self):
         if self.head == None:
             print("Linked list is empty")
         else:
             n = self.head
             while n.nref is not None:
                n = n.nref
             while n is not None:
                print(n.data, "-->", end = " ")
                n = n.prev
             print()  # newline after traversal

     #Insertion When LinkedList is completely empty:
     def insert_empty(self, data):
         if self.head == None:
             new_node = Node(data)
             self.head = new_node
             self.n += 1
         else:
             print("Linked List is not empty")

     #Insertion at the beginning of the Doubly LL:
     def insert_at_beginning(self, data):
         new_node = Node(data)
         if self.head is None:
             self.head = new_node
         else:
            new_node.nref = self.head
            self.head.prev = new_node
            self.head = new_node
            self.n += 1

     # Insertion at the end of the Doubly LL:
     def insert_at_end(self, data):
         new_node = Node(data)
         if self.head is None:
            self.head = new_node
         else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.prev = n
         self.n += 1


     # Insertion after a  specific position in the LL:
     def insert_after(self, data, prev_node):
         if self.head is None:
             print("LL is empty")
         else:
             n = self.head
             while n is not None:
                 if prev_node == n.data:
                      break
                 n = n.nref
             if n is None:
                 print("Node is not present in LinkedList ")
             else:
                 new_node = Node(data)
                 new_node.nref = n.nref
                 new_node.prev = n
                 if n.nref is not None:
                    n.nref.prev = new_node
                 n.nref = new_node
                 self.n += 1
              
     # Insertion at before the given node     
     def insert_before(self, data, next_node):
         if self.head is None:
             print("LL is empty")
         else:
             n = self.head
             while n is not None:
                 if next_node == n.data:
                      break
                 n = n.nref
             if n is None:
                 print("Node is not present in LinkedList ")
             else:
                new_node = Node(data)
                new_node.nref = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.nref = new_node
                else:
                    self.head = new_node
                n.prev = new_node
                self.n += 1
 #Deletion at the starting from the LinkedList:
     def delete_first(self):
         if self.head == None:
             print("Linked List is empty ")
             return 
         if self.head.nref is None:
             self.head = None
             print("DLL is empty after deleting the node!")
             self.n -= 1
         else:
             self.head = self.head.nref
             self.head.prev = None
             self.n -= 1
     
 #Deletion of last node in the linkedlist:
     def delete_last(self):
         if self.head is None:
             print("LinkedList is Empty")
             return
         elif self.head.nref is None:
             self.head = None
             print("DLL is empty after deleting the node!")
             self.n -= 1
         else:
             n = self.head
             while n.nref != None:
                 n = n.nref
             n.prev.nref = None    
             self.n -=  1
             
             
             
             
     # Deletion by the value in LinkedList:                
     def  delete_by_value(self, value):
         if self.head is None:
             print("LinkedList is empty")   
             return 
         if self.head.nref is None:       
            if value == self.head.data:
                self.head = None
                self.n -= 1
            else:
                print("value is not present in DLL")
            return
         if self.head.data == value:
             self.head = self.head.nref
             self.head.prev = None
             self.n -= 1
             return
         n = self.head
         while n.nref is not None:
             if value == n.data:
                 break
             n = n.nref
         if n.nref is not None:
             n.nref.prev = n.prev
             n.prev.nref = n.nref
             self.n -= 1
         else:
             if n.data == value:
                 n.prev.nref = None
                 self.n -= 1
             else: 
                print("value is not present in DoublyLinkedList")    
             
        
    
DLL = DoublyLL()
print("start")
DLL.insert_empty(10)
# DLL.insert_at_beginning(12)
DLL.insert_at_beginning(14)
DLL.insert_at_beginning(16)
DLL.insert_at_end(67)
# DLL.insert_at_beginning(18)
# DLL.delete_first()
# DLL.delete_last()
# DLL.insert_empty(20)
DLL.delete_by_value(7)
# DLL.insert_at_beginning(56)
# DLL.insert_at_beginning(76)
# DLL.insert_after(13, 56)
# DLL.insert_before(999, 67)
# DLL.insert_before(998, 999)
DLL.f_Traverse()
DLL.r_Traverse()
print("Number of Nodes:", DLL.n)
print("end")
