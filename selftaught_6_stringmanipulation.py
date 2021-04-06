# String Manipulation

# Triple Strings - must use triple quotes when a string is multiple lines

longstring = """
line one
line two
line three
line four
line five
line six 
"""
print(longstring)

# String index - each character in string is indexed starting w/ 0
index = "This is a string index example"
print(index[0])
print(index[3])
# Negative index counts from the end of the string backwards
print(index[-1])

# Characters in string can't change.  You must redefine the string if you want to change it
ff = "Edgar Hoover"
print(ff)
ff = "J. Edgar Hoover"
print(ff)

# Concatenation - adding strings using the "+" operator
print("cat " + "in " + "the " + "hat")
print("cat" + " " + "in" + " " + "the" + " " + "hat")

# Strings can be muyltiplied using "*" operator
print("Open"*3)

# Changing Case
print("I'VE HAD THE BLUES, THE REDS, AND THE PINKS".lower())
print("OnE ThInG's FoR SuRE...".capitalize())
print("LOVE STINKS...".lower())
print("love stinks!!!...".upper())
print("yeahyeahhhhh!".upper())

# Formet - create new string that looks for {} and replaces them with parameters you set
formatexample = "William {}".format("Shatner")
print(formatexample)

# Pass variable as parameter
last = "Faulkner"
print("William {}".format(last))

# {} can be used multiple times in strings
author = "Aaron Orndorff"
year_born = 1981
print("{} was born in {}.").format(author, year_born)

# Format method is useful in creatings strings from user input (MADLIB EXAMPLE)
#n1 = input("Enter a noun: ")
#v = input("Enter a verb: ")
#adj = input("Enter an adjective: ")
#n2 = input("Enter a noun: ")
#r = """The {} {} the {} {}.""".format(n1, v, adj, n2)
#print(r)

# Split - can separate one string into two or more
print("Hello.Yes!!").split(".")
print("Hello.Yes.Try.This.Again").split(".")

# Join - add new characters between every character in a string
first_three = "abcdefg"
result = "+".join(first_three)
print(result)

# Turn a list of strings into a single string by calling "join" method
words = ["The ", "Fox ", "jumped ", "over ", "the ", "fence", "."]
one = "".join(words)
print(one)

# Strip Space - removes leading and trailing white space (but not white space in the middle)
s = "        The    Bum      got      Euthanized                 "
print(s)
s = s.strip()
print(s)

# Replace - replaces every occurrence in a string with anothe string
eq = "All animals are equal"
print(eq)
eq = eq.replace("a", "@")
print(eq)

# find and index - finds first occurrence of a character within a string and prints corresponding index
print("ahoobalooballooobalooo").index("h")
try:
    print("ahoobalooballooobalooo").index("l")
except:
     print("Not Found")

# "in" keyword checks if a string is in another string and returns "True" of "False"
print("Cat" in "Cat in the Hat") #true
print("Negro" in "Cat in the Hat") #false

# "not in" keyword checks to see if a string is NOT IN another string
print("Cat" not in "Cat in the Hat") #false
print("Negro" not in "Cat in the Hat") #true

# Using quotes within a string
print("She said, She saaaiiiiddd 'I dont love you anymore'.")
# OR
print("She said, She saaaiiiiddd \"I dont love you anymore.\"")
# OR
print('She said, She saaaiiiiddd "I dont love you anymore."')

# "\n" within a string represents a new line
print("I'm sorry my friends\nI'm such a mess\nI'm doing the best I can\nshe says 'where ya going? where ya been'")

# Slicing - returns a new iterable from a subset of items in another iterable
# Slicing a list
nonfict = ["Holy Bible", "Mein Kampf", "The Art of War", "Coding for Dummies"]
print(nonfict[1:2])
print(nonfict[0:2])
# Slicing a string
quote = "Be Polite, Be Courteous, but have a plan to kill everyone you meet"
print(quote[0:25]) # if starting from the beginning, "0" is not necessary 
print(quote[25:]) #no number after means to go to the end of the string

# Challenges
# 1. Print every character in the string "Camus"
philosopher = "Camus"
print(philosopher[0])
print(philosopher[1])
print(philosopher[2])
print(philosopher[3])
print(philosopher[4])

# 2. Write program that collects 2 strings from user, inserts them into string "Yesterday I wrote a [response_one].  I sent it to [response_two]!"
#response_one = input("Insert a noun: ")
#response_two = input("Insert a name: ")
#q = """Yesterday I wrote a {}.  I sent it to {}.""".format(response_one, response_two)
#print(q)

#3. Use a method to make the string "aldous Huxley was born in 1894." grammatically correct by capitalizing the first letter in the sentence.
string3 = "aldous Huxley was born in 1894.".title()
print(string3)

#4. Take the String "Where now?  Who now?  When now?" and call a method that returns a list that looks like
    #["Where now?", "Who now?", "When now?"]
string4a = "Where now?"
string4b = "Who now?"
string4c = "When now?"
print(string4a, string4b, string4c)
#4 Solution:
lst = "Where now?  Who now?  When now?".split("?")
print(lst)

#5. Take the list ["The", "fod", "jumped", "over", "the", "fence", "."] and turn it into a grammatically correct string.  There should be a space between each word, but no space between the word fence and the period that follows it.
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)

#6. Replace every instance of "s" in "A screaming comes accross the sky." with a dollar sign
string6 = ("A screaming comes accross the sky.")
print(string6)
string6 = string6.replace("s","$")
print(string6)

#7. Use a method to find the first index of th character "m" in the string "Hemmingway"
string7 = ("Hemmingway")
print(string7).index("m")

#8. Find dialogue in your favorite book containing quotes and put it in a string.
string8 = ("""HARTMAN
 I am Gunnery Sergeant
Hartman, your Senior
 Drill Instructor. From now on, you will speak
only when spoken to, and the first and last
 words out of your filthy
sewers will be "Sir!"
 Do you maggots understand that?
RECRUITS
 (in unison)
 Sir, yes, sir!
HARTMAN
 Bullshit! I can't hear you. Sound off like you
 got a
pair.
 RECRUITS
 (louder)
 Sir, yes, sir!
HARTMAN
 If you ladies leave my island, if you survive
 recruit
training ... you will be a weapon, you
 will be a minister of death,
praying for war.
 But until that day you are pukes! You're the
lowest form of life on Earth. You are not even
 human fucking beings!
You are nothing but
 unorganized grabasstic pieces of amphibian
shit!
 Because I am hard, you will not like me. But
 the more
you hate me, the more you will
 learn. I am hard, but I am fair!
There is no
 racial bigotry here! I do not look down on
 niggers,
kikes, wops or greasers. Here you
 are all equally worthless! And my
orders are
 to weed out all non-hackers who do not pack
 the gear
to serve in my beloved Corps! Do
 you maggots understand that?""")
print(string8)

#9 Create the string "three three three" using concatenation, and then using multiplication 
string9 = ("three "+"three "+"three")
print(string9)
string9a = ("three "*3)
print(string9a)

#10. Slice the string "It was a bright cold day in April, and the clocks were striking thirteen."
string10 = ("It was a bright cold day in April, and the clocks were striking thirteen.")
print(string10[:34])
print(string10[34:])
#or
slice10 = string10[:34]
slice10a = string10[34:]
print(slice10)
print(slice10a)