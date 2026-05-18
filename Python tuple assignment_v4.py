"""LOGIC OVERFLOW
Python & DSA Training | Assignment: Tuples & Interview Prep
PROGRAMMING ASSIGNMENT: TUPLE"""




"""
1. Coordinate Immutability
A GPS system stores location as (latitude, longitude). Write a function that takes a list of coordinate tuples
and returns only those that are within the 'Northern Hemisphere' (Latitude > 0)."""

standards_locations = [(18.5, 73.8), (-33.8, 151.2)]
northen_hemisphere = []

for i in standards_locations:
    if i[0] > 0:
        northen_hemisphere.append(i)
    else:
        northen_hemisphere
print(northen_hemisphere) 

print('*' * 100)
# ==========================================================================




"""
2. Employee Records Search
An HR database stores employee data as (ID, Name, Dept). Given a tuple of these records, find the index
of the employee with ID 105. If not found, return -1."""

employee_data =  ((101, 'Ram', 'IT'), (105, 'Neha', 'HR'))
indx = 0

for i in employee_data:
    if i[0] == 105:
        indx = employee_data.index(i)

    else:
       indx = -1

print(indx)

print('*' * 100)
# ==========================================================================




"""3. Stock Price Change
Stock prices for a week are stored in a tuple. Calculate the price difference between the first and the last
day of the week using indexing"""

stock_price =  (200,900)

if len(stock_price) > 1:
    price_difference = stock_price[-1] - stock_price[0]
else:
    price_difference = 0

print(price_difference)

print('*' * 100)

# ===================================================================





"""4. Config Integrity Check
System configurations are stored in a tuple to prevent accidental changes. Write a script to count how
many times the value 'Enabled' appears in the config tuple."""

configurations =  ('Disabled',)#('Enabled', 'Disabled', 'Enabled')
count = 0

if 'Enabled' in configurations:
    count = configurations.count('Enabled')
else:
    count

print(count)

print('*' * 100)
# =================================================================




"""5. Database Row Unpacking
A database query returns a row as (User_ID, Username, Email, City). Unpack this tuple into variables and
return a formatted string: 'User [Username] lives in [City]'."""

db = (1, 'prof_ram', 'ram@logic.com', 'Pune')

user_id, user_name, user_email, user_place = db

print(f"User {user_name} lives in {user_place}")

print('*' * 100)
# ========================================================================




"""6. Historical Records Slicing
A tuple contains logs for the last 10 years. Use slicing to extract the records for the 'mid-range' years
(index 4 to 7 inclusive)."""

records = (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019)

mid_range_record = tuple(records[4 :7+1 ])
print(mid_range_record)

print('*' * 100)

# ======================================================================================


"""7. Product Dimension Validator
A shipping company accepts packages if the sum of dimensions (Length, Width, Height) is less than 100.
Given a tuple of 3 integers, return 'Accept' or 'Reject'."""

packages = (30, 30, 30)

if sum(packages) < 100:
    print("accepted")
else:
    print("rejected")

print('*' * 100)

# ===============================================================================




"""8. Concatenating Auth Keys
To form a secure key, you need to merge two tuples of characters. Create a new tuple by joining Tuple A
and Tuple B."""

secure_key_T1, secure_key_T2 = ('A', 'B'), ('C', 'D')

mostSecuredKey = secure_key_T1 + secure_key_T2

print(mostSecuredKey)

print('*' * 100)

# ====================================================================

"""9. The 'Singleton' Error
You are given an input. Your task is to ensure it is returned as a tuple. If it's a single integer `n`, return
`(n,)`."""

input = (2, 2)


if type(input) == int:
    result = (input,)
else:
    result = tuple(input)

print(result)

print('*' * 100)

# ===========================================================================





""""10. Sorting Nested Tuples
Given a list of tuples representing (Student_Name, Marks), sort the list based on Marks in descending
order."""


marks = [('A', 80), ('B', 95), ('C', 85)]

result = []

while marks:

    max_tuple = marks[0]

    for i in marks:

        if i[1] > max_tuple[1]:
            max_tuple = i

    result.append(max_tuple)

    marks.remove(max_tuple)

print(result)





