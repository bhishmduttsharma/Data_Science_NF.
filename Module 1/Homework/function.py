# 1 Create a Function to Check Whether Two Strings are Anagrams 
# Problem 
# Write a function that accepts two strings and returns True if both are anagrams, otherwise False. 

def are_anagrams(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True
    else:
        return False

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(are_anagrams(s1, s2))


# 2. Create a Function to Find Second Largest Number in a List 
# Problem 
# Write a function that accepts a list and returns the second largest number.

def second_largest(num):
    num.sort()
    return num[-2]

nums = [10, 20, 30, 40, 50]

print(second_largest(nums))


# 3. Create a Function to Count Vowels in a Sentence 
# Problem 
# Write a function that accepts a sentence and returns the count of each vowel.

def count_vowels(sentence):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  
    for char in sentence.lower():
        if char in vowels:
            vowels[char] += 1  
    return vowels
text = input("Enter a sentence: ")

print(count_vowels(text))


# 4. Create a Function to Check Whether a Number is an Armstrong Number 
# Problem 
# Write a function that returns True if a number is an Armstrong number. 

def armstrong(num):
    total = 0
    power = len(str(num))

    for digit in str(num):
        total += int(digit) ** power
    return total == num

n = int(input("Enter a number: "))
print(armstrong(n))


# 5. Create a Function to Find Common Elements Between Multiple Lists 
# Problem 
# Write a function that accepts three lists and returns common elements.

def common_elements(list1, list2, list3):
    return set(list1) & set(list2) & set(list3)
a = [1, 2, 3, 4]
b = [2, 3, 5, 6]
c = [3, 2, 7, 8]

print(common_elements(a, b, c))