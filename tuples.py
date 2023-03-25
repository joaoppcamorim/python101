# Tuples
tuple_1 = ("a", "b", "c", "d")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)
tuple_4 = tuple([3.14, 2.2015, 10])
tuple_5 = tuple("edcba")
print(tuple_4)
print(tuple_5)
tuple_6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_6[2])
print(tuple_6[:8])
print(tuple_6[2:7])
print(tuple_6[3:])

# tuples are immutable data types and does not support item reassignment

# tuples take less memory space than lists
tuple_7 = (1, 3, 5)
list_1 = [1, 3, 5]

print(tuple_7.__sizeof__())
print(list_1.__sizeof__())

# tuples can be used as keys in dictionaries

# tuple looping - same as lists

cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

for city in cities:
    print(city)

count = 0

while count < len(cities):
    print(cities[count])
    count += 1


# tuple slicing with step
print(tuple_6[::3])
print(tuple_6[1::2])
print(tuple_6[7::-1])
print(tuple_6[8::-2])

#tuple methods

nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))


print(nested[2])
print(nested[0][1])

# .count()
repeat = (7, 3, 3, 8, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

# .index()
print(repeat.index(8))
print(repeat.index(7))
