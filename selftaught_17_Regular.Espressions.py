import re
l = "Beautiful is better than ugly. beautiful doesn't have to be Capitalized"
matches = re.findall("Beautiful", l, re.IGNORECASE) # findall is a method
print(matches)

zen = """Although never is 
often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one fucking great idea -- let's do more of those! """
m = re.findall("If", zen, re.IGNORECASE) 
n = re.findall("idea.", zen, re.IGNORECASE)
print(m)
print(n)

string = "Two too."
r = re.findall("t[ow]o", string, re.IGNORECASE)
print(r)

line = "123?345634 hello FUCKERS?!"
q = re.findall("\d", line, re.IGNORECASE)
print(q)

line = "I love $"
t = re.findall("\\$", line, re.IGNORECASE)
print(t)

madlibs = """Giraffes have aroused the curiosity 
of __PLURAL_NOUN__ since earliest times. 
The giraffe is the tallest of all living __PLURAL_NOUN__, 
but scientists are unable to explain how it got its 
long __PART_OF_THE_BODY__. The giraffe's tremendous height, 
which might reach __NUMBER__ __PLURAL_NOUN__, comes from its 
legs and __BODYPART__. """ 

def mad_libs(mls):
    """ :param mls: String with parts the user should fill out 
    surrounded by double underscores. Underscores cannot be inside 
    hint e.g., no __hint_hint__ only __hint__. """ 

    hints = re.findall("_.*?_", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}"\
                .format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("Invalid MLS")

mad_libs(madlibs)



