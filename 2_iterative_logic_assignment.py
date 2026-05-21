"""1. Factorial Engineering: Write a program to find the factorial of a large integer using a for
loop. Ensure you handle the case for 0! and negative inputs."""

num = int(input("Enter a number :"))
factorial = 1

if num == 0:
    print("Factorial of", num, "is", factorial)
elif num > 0:
    for i in range(1, num+1):
        factorial *= i
    print('Factorial of', num, 'is', factorial)
else:
    print("Invalid input")
    


# =====================================================



"""
2. Divisor Discovery: Find all the factors (divisors) of a given number n and print them in
ascending order.
"""

num = int(input("Enter a number :"))

for divisor in range(1, num+1):
    if num % divisor == 0:
        print(divisor, end=',')

# ===============================================================


"""
3. Primality Test: Check if a number is prime using a loop that iterates up to the square root
of n for efficiency."""

num = int(input("Enter a number :"))

sqroot = int(num ** 0.5) +1

if num <=1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, sqroot):
        if num % i == 0:
            is_prime = False
            break

        else:
            is_prime = True
if is_prime:
    print("Prime")
else:
    print("Not Prime")

# ================================================================


"""
4. Fibonacci Sequence Generator: Generate the first n terms of the Fibonacci sequence
where n is provided by the user."""
# num = int(input("Enter the number :"))

# # logic =  # i = 4  ,     first  = 5 ,     second = 8 ,   third = 

first = 0
second = 1
print(first, second)
for i in range(num+1):  
    third = first + second
    print(third, end=', ')
    first = second
    second = third

# ======================================================================

"""5. Perfect Number Checker: A number is "perfect" if the sum of its proper divisors equals the
number. Check if n is perfect."""

num = int(input("Enter the number :"))
result = 0

for i in range(1, num):
    if num % i == 0:
        result += i
if result == num:
    print("Perfect number")
else:
    print("Not a perfect number")


# =============================================================


"""6. Strong Number: A Strong number is one where the sum of factorials of its digits equals the
number itself. Determine if n is Strong."""

num = int(input("Enter the number :"))
original = num
total = 0

while num>0:
    digit = num % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial = factorial * i
    total = total + factorial

    num = num // 10

if original == total:
    print("strong number")
else:
    print("not a strong number")


# ========================================================


"""
7. Harmonic Series Sum: Calculate the sum of the series: 1 + 1/2 + 1/3 + ... + 1/n up to n
terms."""

num = int(input("Enter the number :"))

total = 0

for i in range(num+1):
    if i > 0:
        total += (1/i)
print(total)


# =======================================================


"""
8. String Vowel Counter: Given a string, count the occurrences of each vowel using a loop
and branching logic."""

name = input("Enter the string :")
a=e=i=o=u=0

for ch in name.lower():
    if ch == 'a':
        a+=1
        
    if ch == 'e':
        e+=1
        
    if ch == 'i':
        i+=1
        
    if ch == 'o':
        o+=1
        
    if ch == 'u':
        u+=1

print(f"""
         a = {a},
         e = {e},
         i = {i},
         o = {o},
         u = {u}
        """)


# ==============================================================================





