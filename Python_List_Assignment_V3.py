"""Assignment: Python Lists, Traversals & Slicing
Instructions: Solve the following 20 situational problems. Focus on writing clean, Pythonic
code. For each problem, ensure you handle the edge cases provided in the tables."""


"""1. Email Domain Filter
A company wants to separate internal emails from external ones. Given a list of email strings, 
return a new list containing only those that belong to the 'logic-overflow.com' domain"""

emails = ['ram@gmail.com', 'neha@logic-overflow.com', 'hr@logic-overflow.com']
domain = "logic-overflow.com"

filtered_emails = []

for i in emails:
    temp = i.split("@")[1]
    if temp == domain:
        filtered_emails.append(i)

print(filtered_emails)


# ====================================================================================


"""2. E-commerce Price Inflation Due to a global tax change, increase every item's 
price in a list by exactly 5%. Round the result to 2 decimal places."""

prices = [0, 10.5, 100, 200, 300]
inflation = 5/100
new_prices = []

for i in prices:
    if i >0:
        increarsed_rate = i + (i * inflation)
        new_prices.append(round(increarsed_rate, 2))
    else:
       new_prices.append(i)
       print(i, "This item is FREE") 


print(new_prices)
 

# =================================================================================


"""3. Task Prioritization (Queue)
Simulate a simple FIFO (First In First Out) queue. Given an initial queue and a list of new tasks,
 add the new tasks and then remove the first two tasks from the front."""

queue = ['T1']
new =  ['T2', 'T3', 'T4']
queue.extend(new)

if len(queue) >0:
   for i in range(2):
      if queue:
         queue.pop(0)
else:
   queue = []

print(queue)


# ==================================================================




"""4. The Unique ID Generator
A database export has duplicates. Extract unique IDs from the list while preserving
 the original order of their first appearance"""

db_ids = [10, 20, 10, 30, 20]
unique_ids = []

for i in db_ids:
    if i not in unique_ids:
        unique_ids.append(i)
print(unique_ids)

# ==========================================================




"""5. LIFO Stack Reversal
A warehouse stacker needs to process packages in the reverse order of how they were received. 
Reverse the list in place without using `[::-1]`"""

ls =  [1, 2, 3, 4]
rev = []
for i in ls:
    rev.insert(0, i)
print(rev)


# ==============================================================================




"""6. Top 3 Performance Review
Given a list of employee performance scores, find the top 3 highest scores. 
If there are fewer than 3 scores, return all of them sorted descending."""

# type 1:
prfm_score = [88, 92, 78, 99, 100]
top_k = []

prfm_score.sort(reverse=True)
top_k.append(prfm_score[:3:])

print(top_k)


# type 2:
desc = []

for _ in range(len(prfm_score)):  # range(3)
    largest = prfm_score[0]
    for i in prfm_score:
        if i > largest:
            largest = i
    prfm_score.remove(largest)
    desc.append(largest)
print(desc[ : 3])

# ===========================================================================




"""7. Inventory Audit Search
Check if 'Router' exists in a list of network hardware. If found, return its index. If not, add it to the end of the list and
return the new list."""

inventory = ['Switch', 'Hub']


if 'Router' in inventory:
    print('Router Index is :', inventory.index('Router'))
        
else:
    inventory.append("Router")
    print("router is added")

print("inventory :", inventory)


#===========================================================================




""""8. Log File Slicing
From a list of 100 log entries, extract the first 5 (Recent) and last 5 (Oldest)
 using list slicing in a single program."""

logs = list(range(1, 101))

first5 = logs[:5]
last5 =  logs[-5 : ]

print("first five logs :", first5, "\nlast five logs :", last5)


# ==========================================================================





"""9. Chronological Merge
Combine two lists of timestamps and ensure the final list is sorted in ascending order"""

# Method 1:
L1 = [10, 5] 
L2 = [8, 12]
result = L1+L2
result.sort(reverse=False)
print(result)
timestamps = L1+L2
sorted_stimestamps = []



# Method 2:
for _ in range(len(timestamps)):
    smallest = timestamps[0]

    for i in timestamps:
        if i < smallest:
            smallest = i

    sorted_stimestamps.append(smallest)
    timestamps.remove(smallest)
print(sorted_stimestamps)




# ================================================================





"""10. The Median Index Finder
In a sorted list of IDs, find the middle element. For even-length lists, 
return a list containing the two middle elements"""

ls = (1, 2, 3, 4)


if len(ls) % 2 != 0:
    result = (len(ls) // 2)
    print(ls[result :result+1])
else:
    result = (len(ls) // 2)
    print(ls[result-1 :result+1])



# ==============================================================




"""11. Tag Counter (Case-Insensitive)
Count how many times the word 'Python' appears in a list of tags. Ensure the search is 
case-insensitive."""

mixed_case = ['python', 'PYTHON', 'java']
match = ['python', 'PYTHON']
count = 0

for i in mixed_case:
    if i in match:
        count += 1

    else:
        count

print('Python count',count)

# ===================================================================


"""12. Olympic Scoring
Remove the single highest and single lowest score from a list of judges' marks to find the 
filtered list."""

scores = [9.5, 8.0, 10.0, 7.5]

scores.remove(min(scores))
scores.remove(max(scores))

print(scores)


# ======================================================




"""13. Palindrome String List
Check if a list of characters forms a palindrome (reads the same forward and backward)."""

ls =  ['n', 'i', 't', 'i', 'n']
reverse = []

for i in ls:
    reverse.insert(0, i)

if ls == reverse:
    print("palindrome")
else:
    print("not palindrome")


# =========================================================================



"""14. Batch Processor
Given a list of 20 customer IDs, split them into exactly 4 batches of 5 IDs each using slicing."""

ids = list(range(1,21))
batch = []

for i in range(0, len(ids), 5) :
    batch.append(ids[i:i+5])

print(batch)





# ==============================================================




"""15. VIP Sorting
Sort a list of guest names alphabetically, but ensure any name starting with 'Z' 
is moved to the very front"""

guests =  ['Adam', 'Bill'] #['Alice', 'Zayn', 'Bob', 'Zara']
VIP_sorted = []
z_vip = []

for i in guests:
    if i[0] == 'Z' or i[0] == 'z':
        z_vip.append(i)
    else:
        VIP_sorted.append(i)

vip_names = sorted(z_vip) + sorted(VIP_sorted)
print(vip_names)


# =============================================================================





"""16. Negative Expense Alert
From a list of transactions, extract all negative values (expenses) into a new list named 'Alerts'"""

transactions =  [500, -20, 100, -5]
negative_trans =  []

for i in transactions:
    if i < 0:
        negative_trans.append(i)
    else:
        negative_trans

print(negative_trans)


# ==================================================================





"""17. Next Available Slot
In a theater seating list where 'None' represents an empty seat, find the index of the first 'None'.
Return -1 if full"""

Available_seats = ['Occupied', 'Occupied', None]

for i in Available_seats:
    if None == i:
        print(Available_seats.index(i))


if None not in Available_seats:
    print(-1)

        
# ==================================================================





"""18. Headline Swapper
Given a list of words from a news headline, swap the first and the last word using indexing."""

headline = ['Python', 'is', 'Great']

if len(headline) > 1:
    first = [headline[0]]
    headline.pop(0)
    second = [headline[-1]]
    headline.pop(-1)
    headline = second + headline + first
else:
    headline

print(headline)


# =============================================================================



"""
19. Subscription Upgrade
A list contains 'Free' and 'Paid'. Use a loop to find every 'Free' instance and replace it with 
'Trial'"""


subcription = ['Paid', 'Paid', "Free"]

for i in range(len(subcription)):
    if subcription[i] == "Free":
        subcription[i] = "Trial"
    else:
        subcription
print(subcription)


# =============================================================================




"""
20. The Flat List
Convert a matrix (list of lists) like [[1,2], [3,4]] into a single dimension list [1,2,3,4]"""

matrix =  [[1, 2], [3, 4]]
flat_list  = []

for i in matrix:
    flat_list.extend(i)

print(flat_list)



# ===========================================================================
