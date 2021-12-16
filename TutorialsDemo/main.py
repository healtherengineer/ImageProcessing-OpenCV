from email.message import EmailMessage
from typing import Match

import cv2 as cv
import numpy as nump

import main

print(cv.__version__)
print(nump.__version__)
""""
#Python Basics
print("*************************************");
c = True;
print(c);

print("Hello Guessing game");
#guess = input("Enter your score for tomorrow's match (1 = Frankfurt || 2 = Fenerbahçe || O = Draw): ");

if guess == "1":
    print("Aren't you from German ? aren't you ? :) ")
elif guess == "2":
    print("You are a part of the champion . :)")
elif guess == "0":
    print("You are not from German or Turkey ,either.")
else:
    print("Invalid Choice...")
print(guess);

y = "Football Club";
x ="";
for ch in "Fenerbahce":
    x+=ch;
x+=" ";
x +=y;
print(x);

print("******************************************************")
#Arrays
countries = ["Hungary" , "Ukraine" , "Poland"];
countries.append("Italy"); #Inserting function . array.append(newObject);
lenOftheArray = len(countries);#Finding length of the anyobject . len(object);
countries.pop(2); #it removes second index of the array .
countries.remove("Ukraine");#it looks for Ukraine finds and removes .if it couldnt's find it gives an error.

for country in countries:
    print(country);

print(lenOftheArray);
print(*********************************************************)
"""
#Function

#How to Declare a function in Python
def myFirstFunction():
    print("Hello, This is my first python function or method which one you like")

myFirstFunction()

#Arbitrary Arguments
def printSecondChild(*kids):
    print("Second Child's name is " + kids[1]);

printSecondChild("Asya" , "Melek" ,"Asena")

#We can set parameters as default own ourselves
def giveMyFavoriteFood(food = "Yaprak Sarması"):
    print("My favorite food is "+ food);

giveMyFavoriteFood();
giveMyFavoriteFood("Patlıcan Tava")

def printArray(array):
    for arr in array:
        print(arr)

arr1 = [1,2,312,543,123];
printArray(arr1)