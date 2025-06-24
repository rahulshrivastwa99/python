#program to store 7 fruits in list
fruits = []
f1 = input("Enter Fruit name:") 
fruits.append(f1)
f2 = input("Enter Fruit name:")
fruits.append(f2)
f3 = input("Enter Fruit name:")
fruits.append(f3)
f4= input("Enter Fruit name:")
fruits.append(f4)
f5 = input("Enter Fruit name:")
fruits.append(f5)
f6 = input("Enter Fruit name:")
fruits.append(f6)
f7 = input("Enter Fruit name:")
fruits.append(f7) 
print(fruits)

#program to append marks of student

marks = []
f1 = int(input("Enter the student marks  name:")) 
marks.append(f1)
f2 = int(input("Enter the student marks  name:"))
marks.append(f2)
f3 = int(input("Enter the student marks  name:"))
marks.append(f3)
f4= int(input("Enter the student marks  name:"))
marks.append(f4)
f5 = int(input("Enter the student marks  name:"))
marks.append(f5)
f6 = int(input("Enter the student marks  name:"))
marks.append(f6)
f7 = int(input("Enter the student marks  name:"))
marks.append(f7) 
marks.sort() #sorting the marks in increasing order 
print(marks)


# tuple type cannot change in py

a = (32, 34.5, "Rahul")

a[2] = "SHRI"
print(sum(a))

# SUM OF LIST in py

list = [2, 4, 7, 9, 8]
print(sum(list))  #sum of all elements in listS

# no. of zeros in tuple 

a= (7,0,9,0,0,0,0,9,7,6)
print(a.count(0)) #count of zeros in tuple
