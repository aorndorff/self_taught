class Square:
    pass
print(Square)
#   the class "Square" is an object
#   Classes have 2 types of variables
#   1. class variables - belong to the object Python creates for each class definition and the objects they create.
#       - Must be defined within a class
#       - Access them with class objects and/or with an object created within a class object
#       - allow you to share data between all of the instances of a class without relying on global vaiables
#   2. instance variables - most variables studied so far
#   self.[variable_name] = [variable_value]
#   instance variables belong to objects

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
print(my_rectangle.print_size())

#   Example above - "width" and "len" are instance variables

class Square ():
    recs = []

    def __init__(self, s1, s2):
        self.width = s1
        self.len = s2
        self.recs.append((self.width, self.len))
    
    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

sq1 = Square(5, 5)
sq2 = Square(10, 10)
sq3 = Square(40, 50)
sq4 = Square(5, 2)

print(Square.recs)
#   "recs" is a class variable under the Square class.
#       - defined outside of the __init__ method bc Python only calls the __init__ method when you create an object
#       - you want to be able to access the class variable using the class object, which doesn't call the __init__ method
#       - Each time a rectangle object is created, the code in the __init__ method appends a tuple containing the attributes of the newly created object.
#   Class variables allow us to share data between different objects created by a class without writing a global variable.

#   Every class in Python inherits from a parent class called "Object"
#   Python uses methods inherited from Object in various situations

class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)
#   When you print an object, Python calls a "magic" method called __repr__ inherited from Object
#   What prints is whatever __repr__ returns.
#   __repr__ can be overridden to change what prints

class Possum:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

possumM = Possum("Grogu")
possumF = Possum("Marla")

print(possumM)
print(possumF)

#   Operands in an expression must have a magic method the operator can use to evaluate the expression
print(2 + 2)
#   Each integer object has a magic method called __add__ that python calls when it evaluates this expression
# if you define an __add__ method in a class, you can use the objects it creates as operands in and expression with the additon operator

class PositivityPyramid:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = PositivityPyramid(-20)
y = PositivityPyramid(10)

print(x.n)
print(y.n)
print(x + y)
print(-20 + 10) # __add__ is only modified if called using variables created in the class that changes it

# "Is" - the keyword "is" returns TRUE if two objects are in the same object, and False if not.

class Person:
    def __init__(self):
        self.name = "Bob"

Bob = Person()
same_bob = Bob
print(Bob is same_bob) # "is" is the expression, "Bob" and "same_bob" are oberators / objects

another_bob = Person()
print(Bob is another_bob)

#   Use the "is" keyword to check if a variable is "None"
x = 10
if x is None:
     print("X is None :(")
else:
    print("X is not None!")

x = None
if x is None:
    print("X is None")
else:
    print("X is not None :(")

# Vocabulary
#   Class Variable - variable that belongs to a class object an the objects it creates
#   Instance Variable - belongs to an object
#   Private Variables - A method an object CAN access, but the client CANNOT
#   Public Variable - A variable a client can acccess

# Challenges
#   1. Add a square_list class variable to a class called Square so that every time you create a new Square object, the new object gets added to the list.
#   2. Change the Square class so that when you print a Square object, a message prints telling you the length of each of the 4 sides of the shape
class Square2:
    square2 = []
    def __init__(self, s1):
        self.side = s1
        self.square2.append(self.side)
    def print_size(self):
        print("""{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side))
sq2_1 = Square2(29)
print(Square2.square2)
print(sq2_1.print_size())
sq2_2 = Square2(52)
print(Square2.square2)

#   3. Write a function that takes two objects and parameters and returns True if they are in the same object and False if not.
class Song:
    def __init__(self):
        self.song = "Same Song"

DI = Song()
Same_Song = DI
print(DI is Same_Song)

warm_it_up = Song()
print(DI is warm_it_up)
