# Strings
ex_1 = 'This is a string'
ex_2 = "This is also a string"
ex_3 = "0123456"

#string access by index
print(ex_3[1])
print("apple"[4])

#string slicing
print(ex_1[:3])
print(ex_1[2:5])
print(ex_1[5:])

#concatenation
ex_4 = "pecan" + " " + "pie"
print(ex_4)

#type() and str()
ex_5 = False
ex_6 = 34
ex_7 = 2.456
ex_8 = "string"
print(type(ex_5))
print(type(ex_6))
print(type(ex_7))
print(type(ex_8))

ex_9 = str(ex_5)
print(type(ex_9))

#Escape sequences
print("This\tis\ta\tlot\tof\tspace.") #\t adds idents
print("line one\nline two") #\n adds a new line
print('"When I said \'immdiately,\' I meant today!" said King Saul.') #\' to add single quotes in the middle of a string delimited by single quotes
print("\"Do or do not. There is no try.\"") #\" to add double quates in the middle of a string delimited by double quotes
print("All escape sequences contain a \\.") #\\ add a backslash to the string

# input()
name = input("Enter name.") #value entered is always a string
print("Your name is " + name + ".")
print(type(name))

# int() and float()
user_int = input("Enter integer.")
user_int2 = int(user_int)
user_float = float(user_int2)
print(user_int)
print(type(user_int))
print(user_int2)
print(type(user_int2))
print(user_float)
print(type(user_float))
