my_list = [1,2,3,4,5, "rocketseat", True, False]

if my_list[1] and my_list[7]:
    print(my_list[1:7])
else:
    print(my_list)

my_list.append(6) #add at end of list
my_list.index(6) #result 8.
my_list.insert(2, 10) #index a new element
my_list.pop(3) #remove at index -1
my_list.remove(True) #remove
my_list = [1,3,2,6,4]
my_list.sort() #reorganize ascending order


my_tuple = [1, 2, 2, 3, 4] # immutable, hashable

my_tuple.count(2)
my_tuple.index(3)


person = {"name": "Ryo", "age": "32", "city": "Nara"} #object
person["surname"] = "Yamada"  #add key-value
del person["age"]
person.keys() #dict_keys(['name', city, surname])
keys = list(person.keys()) # can use keys[0] 
values = list(person.values()) # can acess values[0] 
items = list(person.items()) # can use items[0][1]
print("First key-value: %s = %s" % (items[0][0], items[0][1]))


#if, elif, else
age = 18
if age >= 18:
    print("Legal age")

if age == 15:
    print("Debutante ball")

if age != 0:
    print("Not a baby anymore")


age = int(input(("age?"))) #input