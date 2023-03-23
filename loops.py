#Introduction to Loops
#While loops
counter = 0

while counter < 3:
    print('something')
    counter += 1


#For loops
word = "house"

for letter in word:
    print(letter)

#range()
one_input = range(5)

for num in one_input:
    print(num)


two_input = range(5,10)

for num in two_input:
    print(num)


three_inputs = range(1, 20, 3)

for num in three_inputs:
    print(num)