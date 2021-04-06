# Modules - dividing large files of code into smaller pieces (modules)
# modules must first be imported
# Syntax: import[module_name]
# Syntax for using code from a module [module_name].[code]

import math
print math.pow(2, 4)

import random
print random.randint(0,100000000)
# Random Number Generator

# Statistics module calculates mean, median, mode of an iterable of numbers
import statistics
nums = [1, 3, 4, 5, 6, 7, 8, 9, 99, 78, 55, 4, 3223, 567, 7, 5, 5, 6, 7, 8, 2, 5, 66, 11, 77, 88, 99]
print statistics.mean(nums)
print statistics.median(nums)
print statistics.mode(nums)

# Keyword module is used to check if a string is a Python keyword
import keyword
print keyword.iskeyword("for")
print keyword.iskeyword("football")

# Creating a module
# Create a .py file and call it in the existing .py file
# hello.py used in this example
import hello
hello.print_hello()
hello.try_this()

# 1. Call a different function from the statistics module
numbers1 = [2, 3, 5, 6, 7, 8, 9, 1, 0, 0, 0, 3, 4, 5, 6, 7, 8, 9, 9, 9]
print ("Mean: ", statistics.mean(numbers1))
print ("Median: ", statistics.median(numbers1))
print ('Median Low: ', statistics.median_low(numbers1))
print ('Median High: ', statistics.median_high(numbers1))
print ('Median Grouped: ', statistics.median_grouped(numbers1))
print ("Mode: ", statistics.mode(numbers1))

# 2. Create a module named "cubed" witha function that nakes a number as a parameter and returns the number cubed.  Import and call the function from another module.
import cubed
print cubed.cube()





