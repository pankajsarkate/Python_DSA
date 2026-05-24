questions = """Assignment: Master-Level Nested Loop Patterns
Objective: Develop structural debugging skills, spatial matrix mapping, and loop iteration logic. Solve all
20 problems below using optimized nested for loops. Avoid using built-in string multiplication tricks (like 
"*" * n) to maximize logic building."""
print(questions)


n = 4

print("1. Solid Square Grid")

sample = """
Expected Terminal Output
****
****
****
****
"""
print(sample)
print("Output")

for row in range(1, n+1):

    spaces = 1
    stars = n
    print('' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("2. Right-Angled Triangle")
sample = """
Expected Terminal Output
*
**
***
****
"""
print(sample)
print("Output")

for row in range(1, n+1):
    spaces = 1
    stars = row

    print('' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print('3. Inverted Right-Angled Triangle')

sample = """
Expected Terminal Output
****
***
**
*
"""
print(sample)
print("Output")

for row in range(n, 0, -1):

    spaces = 1
    stars = row
    print('' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("4. Mirrored Right-Angled Triangle")

sample = """
Expected Terminal Output
   *
  **
 ***
****
"""
print(sample)
print("Output")

for row in range(1,  n+1):

    spaces = n - row
    stars = row

    print(" " * spaces + '*' * stars)
print('-' * 40)

# --------------------------------------------------

print("5. Inverted Mirrored Right Triangle")
sample = """
Expected Terminal Output
****
 ***
  **
   *
"""
print(sample)
print("Output")

for row in range(0, n):

    spaces = row
    stars = n - row

    print(' ' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("9. The Full Classic Pyramid")
sample = """
Expected Terminal Output
   *
  ***
 *****
*******
"""

print(sample)
print("Output")

for row in range(1, n+1):

    spaces =  n - row
    stars = 2 * row -1

    print(" " * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("10. Inverted Classic Pyramid")
sample = """
Expected Terminal Output
*******
 *****
  ***
   *
"""
print(sample)
print("Output")

for row in range(n, 0, -1):

    spaces = n - row
    stars = 2 * row - 1

    print(' ' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("11. The Diamond Star Configuration")
sample = """
Expected Terminal Output
   *
  ***
 *****
*******
 *****
  ***
   *
"""
print(sample)
print("Output")

"upper pyramid"
for row in range(1, n+1):

    spaces = n - row 
    stars = 2 * row -1

    print(' ' * spaces + '*' * stars)

"Lower Pyramid"
for row in range(n, 0, -1):

    spaces = n - row
    stars = 2 * row -1

    print(' ' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("12. Hollow Square Frame")
sample = """
Expected Terminal Output
****
*  *
*  *
****
"""
print(sample)
print("Output")

for row in range(1, n+1):

    # first and last row 
    if row == 1 or row == n:
        print('*' * n)

    else:
        print('*' + ' ' * (n-2) + '*')

print('-' * 40)

# --------------------------------------------------

print("16. Horizontal Double Triangle (Arrow)")
sample = """
Expected Terminal Output
*
**
***
****
***
**
*
"""
print(sample)
print("Output")

# upper right triangle
for row in  range(1, n+1):

    spaces = 1
    stars = row

    print('' * spaces + '*' * stars )

# lower right triangle
for row in range(n, 0, -1):

    spaces = 1
    stars = row - spaces

    print('' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------

print("19. Hourglass Matrix Layout")
sample = """
Expected Terminal Output
*******
 *****
  ***
   *
  ***
 *****
*******
"""
print(sample)
print("Output")

# upper inverted pyramid
for row in range(n, 0, -1):

        spaces = n-row
        stars = 2 * row -1

        print(' ' * spaces + '*' * stars)

# Lower pyramid
for row in range(1, n+1):

    spaces = n - row
    stars = 2 * row -1

    print(' ' * spaces + '*' * stars)

print('-' * 40)

# --------------------------------------------------
