#importing modules - contain sets of functions
# generic import
import random

print(random.randint(1,10))

# function import - import specific function from a module
from random import randint

print(randint(10,20))

# Universal import
from random import *

print(random())

# variable scope
example = "hello world" # global scope

def loc_ex():
    example = "this is a string" # local scope - only relevant in the context of the function
    return example


print(example)
print(loc_ex())