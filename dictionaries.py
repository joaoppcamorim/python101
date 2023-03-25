# Dictionaries
console = {"nintendo": "switch", "sony": "PS5", "microsoft": "xbox"}
print(console["microsoft"])
# dictionaries are unordered unlike lists

print([2, 4, 6] == [2, 4, 6])
print([2, 4, 6] == [6, 4, 2])

first = {1: 234, 2: 345, 3: 456}
second = {2: 345, 3: 456, 1: 234}
print(first == second)

print( 4 in first)
print( 5 not in first)

# Dictionary methods
# .keys()
print(first.keys())

for key in first.keys():
    print(key)

# .values()

print(first.values())

for value in first.values():
    print(value)

# .items()

print(first.items())

for key, value in first.items():
    print(key, value)


# .get()

print(first.get(4, "not a key"))

# dictionaries are mutable as such they are stored as references like lists

#.fromkeys()
ex_1 = {}.fromkeys(["address"], "58 kingston street")
ex_2 = {}.fromkeys("address", "58 kingston street")
ex_3 = {}.fromkeys(["address"])
print(ex_1)
print(ex_2)
print(ex_3)

#.pop()
ex_4 = {"make": "Honda", "model": "civic", "year": 2016}
popped = ex_4.pop("model")
print(ex_4)
print(popped)

#.popitem()
ex_5 = {"name": "Bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
ex_5.popitem() #removes last item from a dictionary - random before 3.7
print(ex_5)

# .clear()
print(ex_4.clear())

# .copy()
ex_6 = ex_5.copy()
ex_6["name"] = "Robert"
print(ex_5)
print(ex_6)

# .update()

city_info = {"contry": "Canada", "province": "Ontario", "city": "Toronto"}
population = {"population": 29300000}
city_info.update(population)

print(city_info)

# .setdefault()
computers = {"Google": "Chromebook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
computers.setdefault("Lenovo", "ThinkPad")
print(computers)
computers.setdefault("Apple", "MacBook Pro")
print(computers)

# .dict()
empty = dict()
print(empty)
with_values = dict(a=1,  b=2, c=3)
print(with_values)