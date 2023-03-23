#Flow Control
# Comparison operators
print(4 > 2)
print(1 > 3)
print(5.79 < 6)
print(3 < 3)
print(9 >= 9)
print(1 <= 2)
print(10 != 100)
print(10 != 10)
print(10 == 100)
print(10 == 10)
print("hello" == "hello")
print("hello" == "Hello")
print("hello" != "hello")

#boolean operators
# and operator
print(4 > 1 and "word" == "word") # true true
print(8.76 == 8.7600 and 2 != 2) # true false
print("earth" == "EARTH" and 6 <= 3) # false false
print(10 == 5 and 10 != 5) # false true

# or operator
print(4 > 1 or "word" == "word") # true true
print(8.76 == 8.7600 or 2 != 2) # true false
print("earth" == "EARTH" or 6 <= 3) # false false
print(10 == 5 or 10 != 5) # false true

# not operator
print(not 6482 > 0)
print(not "Python" != "Python")

# if statements
veg = input("Enter a vegetable.")

if veg == "corn":
    print("the vegetable is corn.")


# else statements
veg2 = input("Enter a vegetable.")

if veg2 == "corn":
    print("the vegetable is corn.")
else:
    print("the vegetable is not corn.")


# nested if and else

gpa = float(input("GPA?"))
inst_app = input("Approved?")

if gpa >= 3.7:
    if inst_app == "yes":
        print("qualified")
    else:
        print("not approved")
else:
    print("low GPA")


# elif statements
user_num = int(input("number."))

if user_num < 0:
    print("less than zero")
elif user_num == 0:
    print("zero")
elif user_num > 0:
    print("more than 0")

# truthy and falsey values
# empty strings are falsey - evaluate to false; non-empty strings are truthy - evaluate to true
# integer 0 is falsey
# float 0.0 is falsey
# bool() evaluates the value to true or false

