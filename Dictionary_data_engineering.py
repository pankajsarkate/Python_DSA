# Advanced Data Engineering
# Mastering Dictionaries & Nested Structures | Professor's Practice Set


"""Welcome, Data Engineer! Now that you have grasped the mechanics of Python dictionaries, it is
time to put your skills to the test. In the real world, dictionaries are the backbone of data
pipelines—handling JSON payloads, API responses, and NoSQL document structures.
Below are three LeetCode-style case studies designed to challenge your understanding of
nested dictionaries, key lookups, and edge-case handling. Good luck!"""




# =============================================================================
# Case Study 1: The API Log Aggregator
# Difficulty: Medium
# Nested Dicts | Frequency Maps
# =============================================================================


"""Problem Statement :
Frequency Maps
You are analyzing raw logs from an API gateway. The logs are provided as a list of
dictionaries, where each dictionary represents a single API request. Your task is to
build a nested dictionary that aggregates the count of HTTP status codes returned
for each endpoint.
Write a function that takes this list and returns a dictionary where the keys are the 
endpoint strings, and the values are dictionaries mapping the status_code to its
occurrence count."""



# =============================================================================
# =============================================================================

"""
- empty list
- missing keys
- None values
- incomplete records
"""

# =============================================================================
# Sample Input
# =============================================================================

logs = [
    {"endpoint": "/Api/users", "status": 200},
    {"endpoint": "/api/users", "status": 200},
    {"endpoint": "/api/payments", "status": 500},
    {"endpoint": "/api/Users", "status": 404},
    {"endpoint": "/api/payments", "status": 200},
    {"endpoint": "/api/payments"},
    {"endpoint": None, "status": 500},
    {"status": 404},
    {}
]


# =============================================================================
# Output Dictionary
# =============================================================================

output = {}


# Check if logs list is empty
if logs:

    # Iterate through each log dictionary
    for log in logs:

        # Safely fetch values dynamically
        endpoint = log.get("endpoint")
        status = log.get("status")

        print(f"Endpoint : {endpoint}")
        print(f"Status   : {status}")
        print("-" * 40)

        # Skip invalid or incomplete records
        if endpoint is None or status is None:
            continue

        # handle the case sensitvity for endpoint
        if endpoint is not None:
            endpoint = endpoint.lower()


        # Create endpoint key if not present
        if endpoint not in output:
            output[endpoint] = {}

        # Increment status count dynamically
        output[endpoint][status] = output[endpoint].get(status, 0) + 1

else:
    print("Logs list is empty")

# =============================================================================
# Final Output
# =============================================================================

print("\nFinal Aggregated Output:\n")
print(output)

print("*" * 100)

# =============================================================================
# Expected Output
# =============================================================================

"""{'/api/users': {200: 2, 404: 1}, 
    '/api/payments': {500: 1, 200: 1}}"""
# =============================================================================




# -----------------------------------------------------------------------------




# =============================================================================
# Case Study 2: E-Commerce Inventory Merger
# Difficulty: Hard
# Dictionary Merging | Conflict Resolution
# =============================================================================


# Problem Statement
"""You are building an integration pipeline that merges inventory data from two
different warehouse APIs. Both APIs return a nested dictionary mapping a 
product_id to its details (which includes stock and price).
Your goal is to merge warehouse_a and warehouse_b. The rules for merging are:

1. If a product exists in only one warehouse, add it directly to the merged result.
2. If a product exists in BOTH warehouses, the merged stock should be the sum of
both stocks.
3. If a product exists in BOTH warehouses, the merged price should be the 
minimum of the two prices.

 ---------------------------------------------------------------------

Edge Cases to Consider

-> Missing detail keys: A product might have a "stock" key but be missing
the "price" key. Handle this gracefully.
-> Negative Stock: Handle data corruption where stock might be negative
(treat as 0 before summing).
-> Empty Dictionaries: Either warehouse could return an empty dictionary."""





# input:
warehouse_a = {
    "p101": {"stock": 50, "price": 19.99},
    "p102": {"stock": 10, "price": 45.00},
    "p104": {"stock": -5},
    "p105": {"price": 100},
}

# warehouse_a = {}


warehouse_b = {
    "p102": {"stock": 15, "price": 40.00},
    "p103": {"stock": 100, "price": 5.99},
    "p104": {"stock": 20, "price": 10},
    "p106": {"stock": -50, "price": 25}
}

# warehouse_b = {}

# =============================================================================
# Final Merged Dictionary
# =============================================================================

merged_inventory = {}

# =============================================================================

# =============================================================================
# Get all unique product IDs dynamically using or "|" it means union of both the sets
# =============================================================================

all_product_ids = set(warehouse_a.keys()) | set( warehouse_b.keys())
# all_product_ids =  set(warehouse_a.keys()).union(set(warehouse_b.keys()))
print(all_product_ids)


# Iterate all the elements in all_product_ids:
for product_id in all_product_ids:

    # store the unique product ids for a and b
    product_a = warehouse_a.get(product_id, {})
    product_b = warehouse_b.get(product_id, {})
    print(product_a)
    print(product_b)
    print('-' * 40)
    
    # fetch stock safely
    stock_a = product_a.get("stock", 0)
    stock_b = product_b.get('stock', 0)
    # print(stock_a)
    # print(stock_b)

    # handle the negative value for stocks
    if stock_a< 0:
        stock_a = 0
    if stock_b < 0:
        stock_b = 0

    # merged stock a and b
    merged_stock = stock_a + stock_b
    print(merged_stock)
    print('-' * 20,"merged_stock",'-' * 20)

    # -----------------------------------------

    prices = []
    # fetch price safely
    price_a = product_a.get('price')
    price_b = product_b.get('price')
    print(price_a)
    print(price_b)
    print('-' * 40)

    # handling  missing values in price
    if type(price_a) == int or type(price_a) == float:
        prices.append(price_a)
    if type(price_b)== int or type(price_b) == float:
        prices.append(price_b)

    # minimum price from a and b
    if prices:
        merged_price = min(prices)
    else:
        merged_price = None

    # Create final merged structure
    merged_inventory[product_id] = {
                                        "stock": merged_stock,
                                        "price": merged_price
                                    }
    

# =============================================================================
# Final Output
# =============================================================================

print("\nMerged Inventory\n")

for product, detail in merged_inventory.items():
    print(product,' : ',detail)

print("*" * 100)

# =============================================================================
# Expected Output
# =============================================================================


"""{
    p104  :  {'stock': 20, 'price': 10}
    p103  :  {'stock': 100, 'price': 5.99}
    p101  :  {'stock': 50, 'price': 19.99}
    p105  :  {'stock': 0, 'price': 100}
    p106  :  {'stock': 0, 'price': 25}
    p102  :  {'stock': 25, 'price': 40.0}
}"""
# =============================================================================






















    








