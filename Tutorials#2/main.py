# Lists ;

myList = ["Ege", "Erhan", "Mustafa"];
myList.append("NewName")
myList.pop()
myList.remove("Ege")
# print(myList)

# print("Length of My list : " + str(len(myList)))

# Do you think Can we store different data types in one single Lists ?
list2 = ["Ege", "Barışan", 123, True];


# print(list2)
# Why not
# list2[2] = False;
# print(list2)

def printList(list):
    for x in range(len(list)):
        if (x == len(list) - 1):
            print(str(list[x]), end=" ")
        else:
            print(str(list[x]), end=",")


printList(list2)
print()
print(type(list2))

furnitures = ["Mug", "Laptop", "bottle", "thermos", "toilet paper"];


def findInLists(list):
    if "thermos" in list:
        print("Yes , there is a word like that in this list");
    else:
        print("Unfortunately...")


findInLists(furnitures);

# Dictionaries

myDictPc = {
    # "key": "value",
    # ...

    "model": "ASUS",
    "screenCard": "Nvdia",
    "cpu": "Intel i7",
    "isThereSsd": True
}
print(myDictPc)
if (myDictPc["isThereSsd"]):
    print("Yeah SSd is available inside of it.")
    print(len(myDictPc))
else:
    print("There is no Ssd ... Put it please")

# We can get value of any keys we want
processor = myDictPc["cpu"];
print(processor)
# We can get all names of keys

allItemsKeys = myDictPc.keys();
print(allItemsKeys)

# also We can update values

print(myDictPc);
myDictPc["model"] = "Monster";
print(myDictPc)
# There is another way to update

myDictPc.update({"screenCard": "Amd"});
print("********----------------********")
# We can get all values

allValues = myDictPc.values();
print(allValues)

# Adding new key
print(myDictPc);

myDictPc["ram"] = "16GB";
print(myDictPc);

# Let's check if the key is available in it

if "ram" in myDictPc:
    print("Yeah ram is one of the key of myDictPc")
else:
    print("There is no key like that");

# Remove items in Dict

print("*********************************************************")
print(myDictPc)
# myDictPc.popitem();#it deletes last item.
# myDictPc.pop("cpu")
# del keyword
# it deletes all things about myDictPc
# del myDictPc["isThereSsd"]
# del myDictPc


# Clear method important!

# myDictPc.clear();#it creats empty dictionary.


# Let's surfing through a Dictionary
print("------------------------------------------------------------------")
for element in myDictPc.keys():
    if (element == "ram"):
        print(myDictPc[element], end="")
    else:
        print(myDictPc[element], end=",")
print()
print("------------------------------------------------------------------")

for x in myDictPc.values():
    print(x, end=" ")
print()
for x, y in myDictPc.items():
    print(x, y)

# How to copy a dict to another dict

copyDict = myDictPc.copy();
# or you can also do this with dict() method
copy2Dict = dict(myDictPc);
print(copyDict)
print(copy2Dict)

print("--------------------------------------------------------------------------")


# Classes and Objects
# Note __init()__ function in Python is equal to Constructor in Java.
# Note2 self keyword in Python is same with this keyword in Java.
# ... it doesn't have to be self but it hast to be first parameter of any function


# Let's creat a class named Person

# Ctrl+Alt+L == Reformatting code.

class Person:
    name = "Ramazan"
    surname = ""
    age = ""
    courses = []

    def __init__(self, name, surname, age):
        self.name = name;
        self.surname = surname;
        self.age = age

    def sayHiWithName(self):
        print("Hello " + self.name + " " + self.surname)

    def addCourse(self, course):
        self.courses.append(course);


person1 = Person("Ege", "Barışan", 21);

person1.sayHiWithName()
print(len(person1.courses))
person1.addCourse("Computer Networking")
person1.addCourse("Image Processing")
person1.addCourse("Enterprising")
person1.addCourse("Operating Systems")
person1.addCourse("Mobile Programming")
person1.addCourse("Database Management Systems")

print(len(person1.courses))
"""""
if "Image Processig" in person1.courses:
    print("You can not take Trends in Computer science")
elif "Mobile Programmng" in person1.courses:
    print("Your computer will not burn God willing")
else:
    print("You are not student.")
"""

for x in person1.courses:
    print(x)

""""
class emptyClass:
    pass
sometimes you need to create empty class.
"""


class Student(Person):
    year = "";

    def __init__(self, name, surname, age, year):
        super().__init__(name, surname, age)

        self.year = year;
    def sayYear(self):
        print("your graduate year is " + str(self.year));

student1 = Student("Mustafa", "Zaimoğlu", 21, 2023);
# print(student1.name, student1.surname);
student1.sayYear()
student1.sayHiWithName()
print("***********************************")
import numpy as np
import cv2 as cv
#zeors_array = np.zeros( (5, 3) )
#print(zeors_array)

#for x in range(5):
#   for y in range(3):
#       zeors_array[x][y] = 255;



#print(zeors_array)


#Python Matrix

A = [{1,2,3} ,{4,5,6},{7,8,9}]
print('A =',A)
print('A[1] = ',A[1] )











