# Case Study 1: Server Log Visitor Analysis

"""Scenario: You are working as a backend developer for a startup. Your web server
generates logs containing the IP addresses of users who visit your website. You
have been given two lists of IP addresses: one for visitors on Saturday and one for
visitors on Sunday. The marketing team wants to analyze user retention and reach
over the weekend. """

# Problem Definition

# Write a Python script using sets to calculate and print the following:

saturday_ips = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2', '10.0.0.5']
sunday_ips = ['10.0.0.5', '172.16.0.2', '192.168.1.100', '10.0.0.10']


# 1. The total number of unique visitors over the entire weekend.

# Method 1: using set

ttl_uni_visitors = set(saturday_ips + sunday_ips)

print('Method 1:',ttl_uni_visitors)
print('*' * 100)
# ---------------------------------------------------------------------------
# Method 2: using traditional loop and conditional

unique_visitors = []

for i in saturday_ips+sunday_ips:
    if i not in unique_visitors:
        unique_visitors.append(i)

print('Method 2:',unique_visitors)

print('*' * 100)

# ===============================================================================




# 2. The IP addresses of users who visited on both Saturday and Sunday (Loyal visitors).
saturday_ips = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2', '10.0.0.5']
sunday_ips = ['10.0.0.5', '172.16.0.2', '192.168.1.100', '10.0.0.10']


# Method 1:
loyal_visitors = []

# using set and type casting
commn_visitors = list(set(saturday_ips).intersection(sunday_ips))
loyal_visitors.extend(commn_visitors)
print('Method 1:',loyal_visitors)

# -----------------------------------------------------------------------------
# Method 2: using traditional loop and conditional

saturday_ips = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2', '10.0.0.5']
sunday_ips = ['10.0.0.5', '172.16.0.2', '192.168.1.100', '10.0.0.10']

lyl_visitors = []

for ip in saturday_ips:
    if ip in sunday_ips and ip not in lyl_visitors:
        lyl_visitors.append(ip)

print('Method 2:',lyl_visitors)

print("*" * 100)
# ================================================================================




# 3. The IP addresses of users who visited on Saturday but not on Sunday (Dropped-off visitors).
saturday_ips = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.2', '10.0.0.5']
sunday_ips = ['10.0.0.5', '172.16.0.2', '192.168.1.100', '10.0.0.10']

# Method 1: using set 
all_time_visitors = set(saturday_ips).difference(sunday_ips)
print('Method 1:',all_time_visitors)

# ----------------------------------------------------------------------
# Method 2: using traditional loop and conditional 
both_visitors = []

for ip in saturday_ips:
    if ip not in sunday_ips and ip not in both_visitors:
        both_visitors.append(ip)
print('Method 2:',both_visitors)

print('*' * 100)
# ========================================================================
# ========================================================================



"""
Case Study 2: E-Commerce Inventory
Reconciliation"""

"""Scenario: An e-commerce company operates two regional warehouses (Warehouse
A and Warehouse B). During an audit, the inventory management system outputs
tuples of product IDs currently in stock at each warehouse. The operations team
needs to balance the stock. """

# Problem Definition

# Using sets, write a program to answer the following operational questions:

# 1. Which products are stocked in only one of the warehouses, but not both? 
# (Items that might need to be shared).

warehouse_a = ("P101", "P102", "P103", "P104", "P105")
warehouse_b = ("P103", "P104", "P109")

# Method 1: using set

each_warehouses_prdct = set(warehouse_a).symmetric_difference(warehouse_b)
print(each_warehouses_prdct)

print('*' * 100)
# ===========================================================================




# 2. Is Warehouse B's inventory entirely covered by Warehouse A? (Check if B is a subset of A).

warehouse_a = ("P101", "P102", "P103", "P104", "P105")
warehouse_b = ("P103", "P104", "P109")

# Method 1: using set

inventory = set(warehouse_b).issubset(warehouse_a)
print("If B is a subset of A:" , inventory)

print('*' * 100)

# ===================================================================================




# 3. Update Warehouse A's system so it includes all the items from Warehouse B.
warehouse_a = ("P101", "P102", "P103", "P104", "P105")
warehouse_b = ("P103", "P104", "P109")

# Method 1: using set union

updated_inventory = set(warehouse_a).union(warehouse_b)

print(updated_inventory)


