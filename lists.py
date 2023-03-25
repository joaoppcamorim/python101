# lists
example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = [2.12, 3.4, 5.6, 7.8, 9.123]
example_list_3 = ["blue", "green", "red", "yellow", "purple"]
example_list_4 = [True, False, False, True, True]
example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
example_list_6 = [10, 4.2, "tree", False, [1, 2, 3]]

#list()
print(list("blah"))

# in and not in
checked_list = [1, 2, 3, 4, 5]
print(1 in checked_list)
print(8 in checked_list)
not_in_example = 8 not in checked_list
print(not_in_example)

# indexes and list slicing
indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])
indexes_example_2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]
print(indexes_example_2[2][1])
print(indexes_example[0][1])
print(indexes_example[-1])

mixed = [False, 365, 4.24, "this is a string"]
print(mixed[1] + mixed[2])
print("concat " + mixed[-1])

sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

# reassign a list's items
example = [2, 4, 6, 8, 0]
print(example)
example[3] = 7
print(example)
example[1:4] = [3, 2, 1]
print(example)
example[4:7] = [7, 6, 5]
print(example)

# del and list methods
# del deletes based on index
planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)

# .remove()
planets.remove("earth")
print(planets)
# .remove() only removes the first item with the specified value
colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)

# .append()
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)

# .insert()
pets.insert(1, "turtle")
print(pets)

# .sort()
pets.sort()
print(pets)
pets.sort(reverse=True)
print(pets)

ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort()
print(ASCIIbetical)
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)

# .index()
print(ASCIIbetical.index("kiwi"))
print(colors.index("blue"))

# .pop()
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", 'Radiohead']
end = bands.pop()
print(bands)
print(end)
muse = bands.pop(3)
print(muse)

# Lists vs Strings
# lists are mutable while strings are immutable