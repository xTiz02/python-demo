import random as r

x = str(3)    # x will be '3'
y = int("3")    # y will be 3
z = float("3.3")  # z will be 3.0

print('valor de x: {}'.format(x))

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(f'x: {x}, y: {y}, z: {z}')
print(x,y)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print(r.randrange(1, 10))

y = int(2.8) # y will be 2
z = float("3")   # z will be 3.0
y = str(2)    # y will be '2'

# Strings
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5]) # llo
print(b[:5]) # Hello
print(b[2:]) # llo, World!
print(b[-5:-2]) # orl

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J")) # returns "Jello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#List

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1]) # cherry
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist.insert(1, "orange2")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
thislist.pop(1)
del thislist[0] # delete the first element
del thislist # delete the list
#thislist.clear()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits if "a" in x]

print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits

print(green)
print(yellow)
print(red)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.add("orange")

thisset.update(tropical)
thisset.remove("banana")
print(thisset)


# Dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
#x = car.values()
x = car.keys()

print(x) #before the change

car["color"] = "white"

#x = thisdict.values()
print(x) #after the change


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items() #List of tuples

print(x) #before the change

car["year"] = 2020

print(x) #after the change


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
thisdict.pop("model")

for x in thisdict:
  print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 33
b = 200

if b > a:
  pass

for x in range(6):
  print(x)
else:
  print("Finally finished!")


def my_function(*kids):
  print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

car1 = Car("Ford", "Mustang")

x = dir(r)
print(x)

#Date
import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime(2020, 5, 17)
print(x)


#Json
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }
y = json.dumps(x)
print(y)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
    print("No match")

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")