# Iterable - an object that you can get an iterator from
# Iterator - an object with a "next" method
# Object - a collection of data (variables and methods (functions) that act on those data
# Method - a function that belongs to an object
    # - append, sort, remove, insert, etc

# for-loop to interate through the characters of a string
name = "Aaron"
for character in name:
    print(character)
# Each time through the loop, the variable "character" gets assigned to an item in the iterable "name"

# For loop to iterate through the items in a list:
shows = ["Aerial America", "World at War", "World War 2 In Color", "The Men Who Built America"]
for show in shows:
    print(show)

# Use for loop to iterate through items in a tuple
jackass = ("Full Metal Jacket", "Frequency", "Rudy", "A Beautiful Mind")
for movie in jackass:
    print(movie)

# Use for loop to iteratr though items in a dictionary
people = {"Animal Mother": "Full Metal Jacket", "Parcher": "A Beautiful Mind", "Hitler": "Mein Kampf"}
for character in people:
    print(character)

# Use for loop to change items in a mutable iterable like a list
duramax = ["LB7", "LLY", "LBZ", "LML"]
i = 0
for generation in duramax:
    new = duramax[i]
    new = new.lower()
    duramax[i] = new
    i += 1
print(duramax)
# Alternative syntax
duramax = ["LB7", "LLY", "LBZ", "LML"]
for j, generation in enumerate(duramax):
    new = duramax[j]
    new = new.lower()
    duramax[j] = new
print(duramax)

# Use For-loops to move data betwene mutable iterables.
    # Take all strings from 2 diff lists, capitalize each, and put them into a new list
duramax = ["LB7", "LLY", "LBZ", "LML"]
powerstroke = ["idi", "seven three", "six zero", "six four", "six seven"]
fake_diesels = []
for generation in duramax:
    generation = generation.lower()
    fake_diesels.append(generation)
for fGeneration in powerstroke:
    fGeneration = fGeneration.upper()
    fake_diesels.append(fGeneration)
print(fake_diesels)

# "Range" function creates a sequence of integers and can use a for-loop to iterate them.
    # Contains 2 Parameters - where sequence starts and where it stops
for i in range(1, 53):
    print(i)

# While loops - Executes a code as long as an expression evaluates to "True"
    # Syntax - while[expression]:
        # [code to execute]
x = 10
while x > 0:
    print(x)
    x -= 1
print("Happy New Year!!!")

# Infinite Loop - a loop that never ends
#while True:
    #print("Hello Fuckers!!!")  

# break statement - terminates a loop
for y in range(0, 100):
    print(y)
    y += 1
    if y > 10:
        break

# use for-loop to continue a program until user inputs "quit"
#qs = ["What is your name?", "What's your number?", "Can I hit it?"]
#n = 0
#while True:
#        print("Type 'q' to quit")
#        a = raw_input(qs[n]) # Raw Input means you dont have to use quotes
#        if a == "q":
#            break
#        n = (n + 1) % 3 # "%" gives the remainder of the expression (n+1) / 3

# Continue-statement - stops current iteration of loop and moves to the next iteration of it
# print every number in 1 - 10 except 5
for i in range(1, 11):
    if i == 5:
        continue    
    print(i)

# Nested loops - inner (nested) loop iterates through its iterable (sequence) for each time through the outer loop
for i in range(1, 10):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

# nested for loops to add numbers in a nested loop to each number in another list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

# Nest a for loop inside a while loop
while raw_input('y or n?') != 'n':
    for i in range(1, 6):
        print(i)

# 1. Print each item in the following list: ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
list7 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in list7:
    print(show)

# 2. Print all the numbers from 25 to 50
numbers = [25, 26, 27, 28, 29 , 30]
for number in numbers:
    print(number)
for i in range(25, 31):
    print(i)

# 3. Print each item in the list from challenge #1 and their indexes
list7 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(list7):
    print(index)
    print(show)

# 4. Write a program with an infinte loop (with the option to type q to quit) and a list of numbers.  Eac time through the loop, as the user to guess the number on the list and tell them whether or not they guessed correctly.kjhgkhjb
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    guess = raw_input("Guess a number between 1 - 10. (type 'q' to quit)")
    if guess == "q":
        break
    try: 
        guess = int(guess)
    except ValueError:
        print("Guess a number between 1 - 10. (type 'q' to quit)")
    if guess in list:
        print("CORRECT!!")
    else:
        print("Try again, FUCKER!!")

# 5. Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers in the list [9, 1, 33, 83], and append each result to a third list.
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)
print(list3)