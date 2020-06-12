#YASHODEEP PAWAR USERID:2470
from collections import Counter

classes = {}

x = int(input("enter no class and students in class:  "))

for i in range(x):
    a = input("enter class name: ")

    b = input("enter students: ")

    classes[a] = b

students = Counter(classes)

print(students)


