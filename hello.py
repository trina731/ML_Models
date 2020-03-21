# this is a comment

#vars are not typecat
a = 2 
b = 3
c = a * b

#vars can change type after declaration
c = "Five"

#if else condition 
if c < "Six":
    print("C is less than 6")
else:
    print("C is greater than 6")

#lists (can contain different data types)
my_list = ["Trina", 1, 2, 3]
print(my_list)

#empty list
emptyL = []

#2d list
twoD_list = [['hello', 'world'], ['world']]

print(my_list[0])
print(twoD_list)

#adds to end of list
my_list.append(6)
print(my_list[len(my_list) - 1])

#negative indexing, starting from the end
print(my_list[-1])

#insert to middle of list
my_list.insert(1, "inserting")

#remove an element from list
my_list.remove("Trina")
print(my_list)

#deletes from end of list
print(my_list.pop())

#for loop
for item in my_list:
    #print item if greater than 4
    print(item)

#python is object oriented, so almost everything in python is an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is: " + self.name)

p1 = Person("Trina", 18)
p1.myfunc()

#vars created outside a function are global
#to create a global variable inside a function, you can use global keyword

#strings are arrays
a = "Hello World"
print(a[0])

#array slicing
print(a[2:5])

#negative indices to start from end
print(a[-5:-2])

#how to combine strings and numbers: use format() method
age = 36
txt = "My name is Trina, and I am {}"
print(txt.format(age))

#almost any value that has content is evaluated to true
print(bool("Hello"))

#lambda function: small anonymous function that can take  any # args, but only have one expression
x = lambda a, b: a * b
print(x(5, 6))

#use lambda function inside other functions:

