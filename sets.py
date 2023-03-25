# Sets
# sets can not have duplicate values and are unordered

set_1 = {9, 8, 8, 8, 7, 6}
set_2 = set({"a", "b", "c", "d", "e"})
print(set_1)
print(set_2)

empty_set = set()

print(empty_set)

set_3 = set(range(1, 12, 2))
print(set_3)

set_4 = {"a", 3.14, 18, True}

for num in set_3:
    print(num)


# Set methods
#.add()
scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi)

#.remove() and .discard()
fruits ={"apple", "orange", "banana", "tomato", "eggplant"}
fruits.remove("tomato")
print(fruits)
fruits.discard("pear")
fruits.discard("eggplant")
print(fruits)

#.clear()
fruits.clear()
print(fruits)

#.copy()
scifi_copy = scifi.copy()
print(scifi_copy)
print(scifi_copy is scifi)

#.union()
set_5 = {1, 2, 3, 4, 5}
set_6 = {6, 7, 8, 9, 10}
set_7 = set_5.union(set_6)
set_8 = set_5 | set_6
print(set_5)
print(set_6)
print(set_7)
print(set_8)

#.intersection()

set_9 = {4, 5, 6, 7, 8}
set_10 = {6, 7, 8, 9, 10}
set_11 = set_9.intersection(set_10)
set_12 = set_9 & set_10
print(set_11)
print(set_12)

set_13 = set_9 - set_10
set_14 = set_10 - set_9
set_15 = set_9.difference(set_10)
print(set_13)
print(set_14)
print(set_15)


# set comprehensions
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)