# State - value of a programs variables while running
# Procedural Programmiong - writing a sequence of stems moving toward a solution
    # Each step changes a program's state.
    # Store data in global variables and manipulate it with functions
    # Procedural Example #``
x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)

    # Store data in global variables and manipulate it with functions
    # Procedural Example #2
rock = []
country = []
def collect_songs():
    song = "Enter a Song."
    ask = "Type r or c. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)
        
        elif genre == "c":
            cy = input(song)
            country.append(cy)
        
        else:
            print ("Invalid.")

    print(rock)
    print(country)

collect_songs()

# Procedural Drawbacks
    # Global variables in large programs can be hard to track
    # Easy to get errors with large programs and multiple variable modifications

############################################################################################

# Functional Programming - Originates from the lambda calculus
    # Smallest universal programming language in the world
    # Eliminates global state
    # relies on functions that do not use or change clobal state

# Function with Side Effects
    # Relies on data outside itself
a = 0

def increment():
    global a
    a += 1

# Function w/ no side effects
def increment(b):
    return b + 1

############################################################################################
# Object Oriented Programming - state is stored in objects, not functions as in functional programming
    # Also eliminates global state
    # Classes define a set of objects that can interact with eachother.
    # In Python, class is a compound statement with a HEADER and SUITES
        # Syntax - class [className]: [suites]
class Orange:
    def __init__(self, w, c): #double under score on either side of "init"
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

# Creating a new object - instantiating a class
or1 = Orange(10, "dark orange")
print(or1)
    # prints "Created!"
    #        "<__main__.Orange object at 0x7faa4ae61970>
    # Tells you an Orange object has been created and where in computers memory that it has been stored

# Get value of instance variables with syntax [object_name].[variable.name]
print(or1.color)

or2 = Orange(4, "light orange")
or3 = Orange(8, "dark orange")
or4 = Orange(4, "yellow")
print(or1)
print(or2)
print(or3)
print(or4)

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10,98)
print(orange.mold)

# Defining multiple methods in a class
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle) # Just prints that an object has been created an the memory location of said object
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

# Challenge 1: Define a class called "Apple" with four instance variables that represent four attributes of an apple
class Apple():
    def __init__(self, w, c, v, d):
        self.weight = w
        self.color = c
        self.variety = v
        self.diameter = d

apple1 = Apple(300, 'Red', 'Gala', 6)
print(apple1)
print(apple1.weight)
print(apple1.color)
print(apple1.variety)
print(apple1.diameter)

# Challenge 2: Create a Circle class with a method called area that calculates and returns its area. Then create a Circle object, call area on it, and print the result. Use Python's pi function in the built-in math module. 
from math import pi
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * (self.radius * self.radius)
circ1 = Circle(5)
print(circ1)
print(circ1.area())

# Challege 3: Create a "Triangle" class with a method called "area" that calculates and returns its area.  Then create a "Triangle" objecty, call "Area" on it, and print the result.
class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
    
    def area(self):
        return (self.base * self.height) / 2

triangle1 = Triangle(5, 10)
print(triangle1)
print(triangle1.area())

# Challenge 4: Make a 'Hexagon' class with a method called "calculate_perimeter" that calulates and returns its perimeter.  Then create a 'Hexagon' object, call 'calculate_perimeter' on it, and print the result
class Hexagon():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side * 6)

hexagon1 = Hexagon(10)
print(hexagon1)
print(hexagon1.calculate_perimeter())

import math

class Displacement():
    def __init__(self, a, d):
        self.angle = a 
        self.distance = d
    
    def hDist(self):
        return(self.distance * math.tan(self.angle * math.pi/180))
      

hDist1 = Displacement(45, 10)
print(hDist1.angle)
print(hDist1.distance)
print(hDist1.hDist())
