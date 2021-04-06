# Containers - like filing cabinets for objects
# Container types - lists, tuples, dictionaries 

# Methods - functions closely associated w/ a given type of data

# Call methods "Upper" and "Replace"

"Hello".upper()

"Hello".replace("o", "@")

# List - container that stores objects in order

# 01234
# HELLO

# 2 Syntaxes
    # 1. create empty list w/ "list" function --> fruit = list()
    # 2. name a list w/ brackets --> fruit = []

fruit = ["Apple", "Orange", "Banana"]
print(fruit)

fruit.append("Elderberry")

fruit.append("basket")

print(fruit)

# Lists can store any data type

random = []

print(random)

random.append(True)
random.append(100)
random.append(1.12343)
random.append("Hello Fuckers!")

print(random)

# Iterable - when you can acces each item using a loop.

# Each item in an iterable has an index --> a number representing the item's position in the iterable

# In "Random" list above, True is index 0, "Hello Fuckers!" is index 3

# Retrieve item with its index using syntax [list_name][[index #]]
print(random[0])
print(random[1])
print(random[2])
print(random[3])
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])

# Mutable - when you can add or remove objects from the container
     # change an item by assigning its index to a new object
colors = ["Cardinal", "Gold", "UCLA"]
print(colors)
colors[2] = "Just kidding, UCLA can eat a bag of dicks!"
print(colors)

# remove last item from a list using method "pop"
print(random)
item = random.pop()
print(item)
print(random)

# Combine 2 list with the "+" operator
print(random + colors)

# check if an item is in a list with keyword "in"
print("blue" in colors)
print("Cardinal" in colors)

# check if an item is NOT IN a list with keyword "not in"
print("blue" not in colors)
print("Cardinal" not in colors)

# get size of list with "len" function
print(len(colors))
print(len(random))
print(len(colors + random))

# Practical Application

guess = input("Guess a color: ")

if guess in colors:
	print("Fight On!!!!")
else:
	print("Try Again!")
if guess == "blue":
	print("Fuck you, you UCLA FUCK!!!")

# Tuple = container that stores objects in a specific order
# Tuples are immutable - their contents cannot change
# 2 syntaxes
    # 1. my_tuple = tuple()
    # 2. my_tuple = ()
tuple = ("A. Orndorff", 1981, True, "Machine", 52.5252)
print(tuple)
# Even if tuple has (1) item, a "," is still required after it
# example("I'm sorry Ms. Jackson",)
# Index numbering still applles to Tuples
# Keywords "in", "not in" still apply
# Use tuples when data will not change (i.e. coordinates, etc)

# Dictionary - container for storing objects, and link one object (key) to another object (value)
# Linking one object to another - mqpping --> Resulting pair is called "key-value pair"
# you can use a key to look up a value, but you cannot use a value to look up a key
# 2 Syntaxes
    # 1. blahblah = dict()
    # 2. blahblah = {}
blahblah = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(blahblah)
# adding items to dicionary
blahblah["key5"] = "value5"
blahblah["key6"] = "value6"
print(blahblah)
# look up item in dictionary
print(blahblah["key1"])
# use "in" to check for a key in a dictionary
# you cannot check for a value in a dictionary
# delete a key-value pair w/ keyword "del: "
print(blahblah)
del blahblah["key3"]
print(blahblah)

# Example program using a dictionary
# If dictionary keys are integers, they dont need to be in ""
rhymes={1: "fun", 2: "blue", 3:"me", 4: "whore", 5: "Live", 6: "dicks"}
n = input("Type a Number: ")
if n in rhymes:
	rhyme = rhymes[n]
	print(rhyme)
else:
	print("Not Found, Dumbass!")

# Containers within Containers
	# List within a list
lists = []
rap = ["Snoop", "Dr. Dre", "Easy E"]
country = ["Chris Ledoux", "George Strait", "Cross Canadian Ragweed", "Hank Williams"]
rock = ["ACDC", "Metallica", "Megadeth", "Motley Crue"]
classical = ["Mozart", "Beetoven", "Brahms"]
lists.append(rap)
lists.append(country)
lists.append(rock)
lists.append(classical)
print(lists)
print(classical)

# tuples can be stored in lists, as can dictionaries
	# tuple inside of a list
city_coordinates = []
la = {32, 188}
chicago = {41, 87}
sheboygan = {"Hell if", "I know"}
city_coordinates.append(la)
city_coordinates.append(chicago)
city_coordinates.append(sheboygan)
print(city_coordinates)

# 5 challenges

# 1. Create a List of your favorite musicians
musicians = ["Chris Ledoux", "George Strait", "Beetoven", "Mozart", "ACDC", "Motley Crue"]
print(musicians)

# 2. Create a list of Tuples, each touple containing the lat/long of womewhere you've lived 
coordinates = []
houston = (42, 81)
pontiac = (36, 80)
bakersfield = (35, 48)
coordinates.append(houston)
coordinates.append(pontiac)
coordinates.append(bakersfield)
print(coordinates)

# 3. Create a Dictionary that contains attributes about you
attributes = {"height": "6-2", "weight": "220", "eyes": "hazel", "hips": "metal", "sport": "football"}

# 4. Write program that lets user ask an attribute, then returns result
n = input("Ask an attribute about Aaron: ")
if n in attributes:
	attribute=attributes[n]
	print(attribute)
else:
	print("I'm not telling!")

# 5. Create a dictionary mapping fav. music artists to fav songs by them
artists = {"Chris Ledoux": ["Bareback Jack", "Gold Buckle Dreams", "Re-Ride", "Tougher Than The Rest"], "ACDC": ["Long Way To the Top", "Back in Black", "Thunderstruck", "Dirty Deeds"], "George Strait": ["Amarillo by Morning", "Texas", "Much Too Young"], "Metallica": ["Enter Sandman", "ONE", "Sad But True"]}
print(artists)
