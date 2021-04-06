# Encapsulation
#   1. Objects group variables (state) and methods (for altering or doing calculations that use the state) in a single unit

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = 1

    def area(self):
        return self.width * self.len
# Variables - len, width
# Method - area
#   2. hiude a class's internal data to prevent the client (code ourside the class that uses the object) from directly accessing it.
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

# nums - instance variable
    # Can be changed in 2 ways:
    #   1. use the change_data method
data_one = Data()
print(data_one.nums)
data_one.nums[0] = 100
print(data_one.nums)
    #   2. directly accessing the nums instance variable using the Data object
data_two = Data()
print(data_two.nums)
data_two.change_data(0, 52)
print(data_two.nums)

#-----------------------------------------------------------------------------------------------------------------------------------------

# Abstraction
#   Taking away or removing characteristics from somthing in order to reduce it to a set of essential characteristics 

# Polymorphism - Ability to present the same interface for differing underlying forms (data typs)
#   Use "print" interface for varying data types
print("Hello Fuckers!") #String
print(200) #Integer
print(200.5252) #Float

print(type("Hello Fuckers!")) 
print(type(200)) 
print(type(200.5252))

#-------------------------------------------------------------------------------------------------------------------------------------

#   Inheritance - when you create a class, you can inherit methods and variables from another class.
#   Class inherited FROM - Parent
#   Class that inherets the method or variable - child

#   Class that models a shape
class Shape(): # - Parent Class
    def __init__(self, w, l):
        self.width = w
        self.lenth = l

    def print_size(self):
        print("""{} by {}""".format(self.width, self.lenth))

my_shape = Shape(20, 25)
print(my_shape.print_size())

class Square(Shape): # - Child Class (Parent class is a parameter to child class) 
   # pass - Keyword that tells python not to do anything.  Use it if you're not defining any new variables or methods in child class
   def area(self):
       return self.width * self.lenth # Applies new method to parent variables

   def print_size(self): # method overriding - overrides method previously defined in parent class
        print("""I am {} by {} inches.""".format(self.width, self.lenth))

a_square = Square(20, 20)
print(a_square.print_size())
print(a_square.area())

#----------------------------------------------------------------------------------------------------------------------------------------
# Composition - models the "has a" relationship by storing an object as a variable in another object.
class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name
# when you create a "DOG" object, you pass in a "Person" object as the owner parameter
mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)        

########## VOCABULARY #################
# 4 Pillars of object oriented programming - inheritance, polymorphism, abstraction, encapsulation
# Inheritance - when you create a class, it can inherit methods and variables from another class
# Parent class: that class that is inherited from
# Child class - the class that inherits
# Method overriding - child class' ability to change the implimentation of a method inherited from its parent class
# Polymorphism - the ability to present the same interface for differing underlying forms (data types)
# Abtraction - process of taking away / removing characteristics from something in order to reduce it to a set of essential characteristics
# Client - code outside the class that uses it
# Encapsulation - object oriented programming groups variables (state) and methods (for altering state) in a single unit (object)
#   - hiding a class' internal data to prevent the client from accessing it
# Composition - stores ab object as a variable in another object
        
########## CHALLENGES #################
#   1. Create Rectacngle and Square classes with a method called calculate_perimeter.  Create Rectangle and Square onjects and call the method on both of them.
class Shape():
    def name(self):
        print("I am a shape!")



class Square(Shape):
    def __init__(self, s1):
        self.side = s1
    
    def calculate_perimeter(self):
        return (4 * self.side)
    
    def change_size(self, new_size):
        self.side += new_size

    
b_square = Square(5)
print(b_square.calculate_perimeter())
b_square.change_size(8)
print(b_square.calculate_perimeter())
    
class Rectangle(Shape):

    def __init__(self, w, l):
        self.width = w
        self.lenth = l
    
    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.lenth)

a_rectangle = Rectangle(10, 5)
print(a_rectangle.calculate_perimeter())
print(b_square.name())
print(a_rectangle.name())

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rider = Rider("Rochelle Pate")
poly = Horse("Poly", rider)
print("The name of the horse is {}".format(poly.name))
print("The name of the rider is {}".format(rider.name))

