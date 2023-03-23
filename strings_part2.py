#String methods
#.upper() and .lower()
all_low = "assgyusdgiodhufopgjgpj"
print(all_low.upper())
all_upper = "YGDSIUGHOIFDKJH"
print(all_upper.lower())

#.isupper() and .islower()

print("DFYUDFUYGF".isupper())
print("fgdsufsdgd".islower())

#Multiple string methods
print("SHOUT".lower().isupper())

#Other methods
#.isalpha() - only letters
#.isalnum() - only letters and numbers
#.isdecimal() - only numbers
#.isspace() - only spaces
#.istitle() - only title
#.title() - turns string into title case

#.startswith() and .endswith()

print("this is a string".startswith("this"))
print("To infinity and beyond!".endswith("beyond!"))

#.join()

print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print("....".join(["one", "two", "three"]))

#.split
print("Eggs, Milk, Waffles, Bacon".split())
print("Eggs, Milk, Waffles, Bacon".split(","))
print("Eggs, Milk, Waffles, Bacon".split(", "))

#.rjust() and .ljust() and .center
print("hello world".rjust(15, "."))
print("hello world".ljust(15, "£") + "four spaces later.")
print("hello world".center(15,"*"))

#.strip(), .rstrip(), .lstrip()
print("hello world".strip())
print("I had an exciting trip!!!!1111".rstrip("1"))
print("juice, bread, milk".lstrip(", eiucej"))
print("blueblueyellowblue".strip("eulb"))

#.replace()
print("good morning".replace("morning", "afternoon"))

#len()
print(len("tree"))

#.format()
name = input("name.")
degree = input("degree.")
job = input("job.")
experience = input("experience.")

print(name + " majored in " + degree + ", works as a " + job + ", and has " + experience + " years of experience.")
print("{} majored in {}, works has a {}, and has {} years of experience".format(name, degree, job, experience))