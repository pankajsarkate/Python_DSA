# # Topic
# # Arithmetic
# # Logical 
# # Bitwise 
# # Comparison

# """1. Leap Year Algorithm: Write a script to check if a year provided by the user is a leap year.
# Ensure century years are only leap years if divisible by 400"""

year = int(input("Enter the year :")) 

if year % 400:
    print("Not a Leap Year")
else:
    print("Leap Year") 

# #________________________________________________________________________________
# #________________________________________________________________________________




# """2. Binary Power Check: Use Bitwise Operators to determine if an integer is a power of 2. You
# are restricted from using any loops or external libraries"""

# # 2**0, 2**1, 2**2, 2**3, 2**4
# # 1      2     4     16    32

num = int(input("Enter the number :"))

if num > 0 and (num & (num - 1) == 0):
    print(num, "Number is a power of 2")

else:
    print(num, "Number is not a power of 2")

# #________________________________________________________________________________
# #________________________________________________________________________________




# """3. Coordinate Geometry: Given x and y coordinates, find the quadrant. Handle cases where
# the point lies on the X-axis, Y-axis, or Origin"""

x, y = map(int, input("Enter X , Y :").split(","))

x, y = int(input("Enter X :")),  int(input("Enter Y :"))

if x > 0 and y > 0:
    print("First quadrant")

elif x < 0 and y > 0:
    print("Second quadrant")

elif x <0 and y < 0:
    print("Third quadrant")

elif x == 0 and y == 0:
    print("Origin")

elif x == 0 and (y < 0 or y > 0):
    print("on Y axis")
else:
    print("on X axis")


# #________________________________________________________________________________
# #________________________________________________________________________________




# """4. Logical Overlap: Given two intervals [a, b] and [c, d], write a single logical expression
# using comparison operators to detect if they overlap."""
# [a, b] = [1, 10]
# [c, d] = [5, 15]

a, b = map(int, input("Enter the numbers :").split())
c, d = map(int, input("Enter the numbers :").split())

if a < d and c < b:
    print("Overlap Detected")
else:
    print("Overlap not Detected")
# #________________________________________________________________________________
# #________________________________________________________________________________



# """5. Bitwise Odd-Even: Identify if a number is even or odd without using the modulo (%)
# operator. Use bitwise AND."""

num = int(input("Enter the number :"))

if num & 1:
    print("Odd")
else:
    print("Even")

# #________________________________________________
# #________________________________________________



# """6. Triangle Validity & Classification: Input three sides. Check if the triangle is valid. If valid,
# classify it as Equilateral, Isosceles, or Scalene."""
logic = """
        Equilateral=All sides are equal,
        Isosceles = Two sides are equal,
        Scalene  = All sides are different
        """
a, b, c = int(input("Enter the number 1st side :")), int(input("Enter the number 2nd side :")), int(input("Enter the number 3rd side:"))

if a == b == c:
    print("Eqauilateral Triangle")
elif a == b != c:
    print("Isoscalene Triangle")
else:
    print("Scalene Triangle")

# #__________________________________________________
# #__________________________________________________




# """7. Zero-Safe Division: Perform a division a/b. If b is zero, display a custom error message.
# Otherwise, display the floor quotient and remainder"""

a, b = int(input("Enter the number 1st side :")), int(input("Enter the number 2nd side :"))

if b==0:
    print("ZeroDivisionError")
else:
    print(f"Q: {a/b}, R: {a%b}")

# #______________________________________________________
# #______________________________________________________



# """8. Max of Three: Find the maximum among three numbers using nested if-else statements
# (Strictly no max() function)."""

a, b, c = int(input("Enter the number 1st side :")), int(input("Enter the number 2nd side :")), int(input("Enter the number 3rd side:"))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b>a:
        if b > c:
            print(b)
        else:
            print(c)

# #___________________________________________________________
# #___________________________________________________________



# """9. Bitwise Swap: Swap the values of two integer variables using the XOR (^) operator without
# using a temporary variable."""

# using arithmatic operator

a, b = 7, 3
b, a = a, b
print(a,b)

#using bitwise operator xor ^
a, b = 7, 3
a = a ^ b
b = a ^ b
a = a ^ b


# """11. Salary Breakdown: Calculate Net Salary. If Basic > 50k: HRA=20%, DA=90%. If Basic <=
# 50k: HRA=15%, DA=85%."""

basic = int(input("Enter Basic Salry :"))
hra = float(input("Enter HRA in % :"))
da = float(input("Enter DA Salry :"))

if basic > 50000:
    hra_sal = basic * (hra/100)
    da_sal  = basic * (da/100) # type: ignore
    net_sal = basic + hra_sal + da_sal
    print(net_sal)
else:
    hra_sal = basic * (hra/100)
    da_sal  = basic * (da/100) # type: ignore
    net_sal = basic + hra_sal + da_sal
    print(net_sal)

# #_____________________________________________________________
# #_____________________________________________________________



# """12. ASCII Character Analysis: Input a character and determine if it is Uppercase, Lowercase,
# Digit, or Special Symbol using ordinal comparisons."""

ch = input("Enter a letter :")

if 'a' <= ch <= "z":
    print("LowerCase")
elif "A" <= ch <= "Z":
    print("UpperCase")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special Character")

# #________________________________________________________________
# #_________________________________________________________________




# """13. Dual Divisibility: Check if a number is divisible by 5 AND 11. If not, check if it's divisible
# by either one and print accordingly."""
num = int(input("Enter a number :"))

if num & 5 and num % 11:
    print(f"divisible by either")
else:
    print("divisible by Both")


# #____________________________________________________
# #____________________________________________________



# """14. 3-Digit Palindrome: Input a 3-digit number. Reverse it using arithmetic operators and
# check if the number is a palindrome."""
num = 123

hundreds = 123 // 10
tens = (123 // 10) % 10
unit = 123 % 10

reverse = (unit * 100) + (tens *10) + hundreds
if num == reverse:
    print("Palindrome")
else:
    print("Not palindrome")


# dynamic logic
num = int(input("Enter the number to check palindrome :")) 
origin = num
# reverse = 0           digit = 1     reverse = 321    num = 0

while num>0:
    digit = num%10                                     
    reverse = (reverse * 10) + digit
    num //= 10              

if origin == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")





# #________________________________________________
# #________________________________________________



# """15. Progressive Electricity Billing: 1-50 units: 0.50/u; 51-150: 0.75/u; 151-250: 1.20/u; Above
# 250: 1.50/u. Add 20% surcharge to total."""

units = """
        1-50 = 0.50/u,
        51-150 = 0.7/u,
        151-250 = 1.20/u
        unit >251 = 1.50/u
        20%.surcharge to total
        """

unit = int(input("Enter the total units :"))

if unit <=50 and unit !=0:
    total = unit * 0.50

elif unit <=150:
    total = (50 * 0.5) + ((units-50) * 0.75)

elif unit <=250:
    total = (50 * 0.5) + (100 * 0.75) + ((units - 150)*1.20)
else:
    total = (50 * 0.5) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = total * 0.20
bill = total + surcharge
print("Elelctric bill is :", bill)


# #________________________________________________
# #________________________________________________



# """16. Bitwise Sign Detection: Write a program that checks if two input integers have opposite
# signs using the bitwise XOR operator"""

num1 = int(input("Enter the first num :"))
num2 = int(input("Enter the second num :"))

if ( num1 ^ num2) < 0:
    print("Opposite sign")
else:
    print("Same sign")

# #________________________________________________
# #________________________________________________



# """17. Arithmetic Menu: Build a calculator that takes two numbers and an operator (+, -, *, /) and
# outputs the result using if-elif."""

num1 = float(input("Enter a number 1 :"))
num2 = float(input("Enter a number 2 :"))
opr = input("Enter Arithmatic operator+,(-,*,+,/) :")

if opr == '/':
    print(f"{num1} {opr} {num2} = {num1/num2}")
elif opr == '*':
    print(f"{num1} {opr} {num2} = {num1*num2}")
elif opr == '-':
    print(f"{num1} {opr} {num2} = {num1-num2}")
else:
    print(f"{num1} {opr} {num2} = {num1+num2}")

# #______________________________________________________
# #______________________________________________________

# """18. Vowel/Consonant Switch: Determine if a character is a Vowel or Consonant. Ensure it
# works for both lowercase and uppercase inputs."""

char = input("Enter a charater :")
vowels = "aeiouAEIOU"

if char in vowels:
    print("Vowel")
else:
    print("Consonent")


# #_________________________________________________________
# #_________________________________________________________




# """19. Quadratic Roots: Calculate roots of ax² + bx + c. Use comparison to handle Real, Equal,
# and Imaginary roots based on Discriminant"""

a = 1
b = -3
c = 2

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)

    print("Roots:", root1, ",", root2)

elif discriminant == 0:
    root = -b / (2 * a)

    print("Equal Roots:", root)

else:
    print("Imaginary Roots")



# #_________________________________________________________
# #_________________________________________________________



"""
20. Bitwise Multiplication: Multiply an input number by 16 using only Bitwise Shift operators
(Strictly no * operator)."""

num = int(input("Enter the number :"))

result = num << 4
print(result)




