import random
 
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
 
# prints a random item from the string
string = "striver"
print(random.choice(string))

# print a random item by using randrange
print(random.randrange(0,9))

# set
print(set("abcdefghijklmnopqrstuvwxyz"))