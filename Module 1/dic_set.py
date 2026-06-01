# Write a program to create a dictionary from two lists: one of keys and one of values. 

keys = ["name", "age", "address","gender"]
values = ["Bhishm", 20, "Mathura","Male"]

my_dict = dict(zip(keys, values))
print(my_dict)


# Merge two dictionaries into one 

dic1 = {1,2,3,4,5}
dic2 = {5,6,7,8,9}
dic1.update(dic2)

print(dic1)


# Write a program to sort a dictionary by its values. 

d = {
    'a' : 2,
    'b' : 1,
    'c' : 9,
    'd' : 5
}
values = sorted(d.values())
print(values)


#Given two sets, check if one set is a subset of another.

set = {1,2,3,}
set1 = {1,2,3,4,5}

if set.issubset(set1):
    print("set is a subset of set1")
else:
    print("set is not a subset of set1")


#Write a program to check whether two lists have at least one common element using sets.

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

if set(list1) & set(list2):
    print("Yes")
else:
    print("No")