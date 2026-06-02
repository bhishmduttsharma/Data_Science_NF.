#Write a program to find the largest and smallest elements in a list. 

list = [2,4,6,8,10,12,14]
print(max(list))
print(min(list))



#Write a program to remove duplicate elements from a list. 

list = [3,4,5,6,5,4,7,8,9]
print(set(list))



#Write a program to reverse a list without using built-in reverse functions. 

list = [3,6,8,9,12,14,15]
print(list[:-1])



#Write a program to merge two lists and sort the final list

list1 = [2,4,6,8,10]
list2 = [11,12,13,14]

final_list = list1 + list2
final_list.sort()

print("final list is:",final_list)



#Write a program to find the second largest element in a list.

list = [3,4,5,6,7,5,8]
list.sort()
print("second largest numeber is:",list[-2])



#Write a program to check whether an element exists in a tuple. 

element = (2,4,5,6,8,9)
if 5 in element:
    print("element is exists")
else:
    print("no")



#Write a program to count the occurrence of an element in a tuple. 
#  
element = 4
tuple = (2,4,5,3,7,8,9,4,4,5)
count = tuple.count(element)
print("occurrence of element is:",count)



 #Write a program to sort a list of tuples based on tuple values.

tuple = (2,3,4,5,6,5,4,2)
a = list(tuple)
a.sort()
print("List is : ",a)



# Write a program to convert a tuple into a list and a list into a tuple.
t = (3,6,4,3)
a = list(t)
print("List is : ", a)

list = [5,6,3,2]
b = tuple(list)
print("Tuple is :",b)


