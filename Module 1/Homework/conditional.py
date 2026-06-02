#  Write a program to check whether a year is a leap year or not.

n = int(input("Enter the number:"))

if (n % 400 == 0) or (n % 4 == 0):
    print("Year is leap year")
else:
    print("Not leap year")



#  Write a program to find the largest among three numbers using nested conditional statements.

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

if a > b:
    if a > c:
        print("a is the largest number")
    else:
        print("c is the largest number")
else:
    if b > c:
        print("b is the largest number")
    else:
        print("c is the largest number")  
  



#  Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or special character. 

character = input("Enter a character: ")
if character.isupper():
    print("Uppercase Letter")

elif character.islower():
    print("Lowercase Letter")

elif character.isdigit():
    print("Digit")

else:
    print("Special Character")



#  Write a program to calculate electricity bill using different unit slabs.

unit = int(input("Enter electricity units:"))
if unit >= 0 and unit <= 100:
    bill = unit * 2

elif unit > 100 and unit <= 200:
    bill = unit * 4

elif unit > 200 and unit <= 300:
    bill = unit * 6

else:
    bill = unit * 8

print(" you Electricity Bill is =", bill)



# Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene. 

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a==b and b==c:
    print("Triangle is Equilateral")
elif a==b or b==c or c==a:
    print("Triangle is isosceles")
else:
    print("Triangle is Scalene")



# Write a program to calculate income tax according to salary ranges.

salary = int(input("Enter your salary: "))
if salary <= 25000:
    tax = salary * 0.03
    print("Income Tax =", tax)

elif salary <= 50000:
    tax = salary * 0.04
    print("Income Tax =", tax)

elif salary <= 75000:
    tax = salary * 0.05
    print("Income Tax =", tax)

else:
    tax = salary * 0.07
    print("Income Tax =", tax)


                 
# write a program to check login authentication using username and password conditions. 

username = input("Enter the username: ")
password = int(input("Enter the password: "))

if username == "saurav" and password == 12345:
    print("Login Successful")

elif username != "saurav":
    print("Wrong Username")

elif password != 12345:
    print("Wrong Password")

else:
    print("Login Failed")



#  Write a program to assign grades based on marks and display distinction for high scores.

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
    print("Distinction")

elif marks >= 75:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

elif marks >= 40:
    print("Grade: C")

else:
    print("Grade: Fail")
