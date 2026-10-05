# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0

billing = True


# ---------- PART 2: the OUTER while loop ----------
while billing:

    customer_name = input("Customer name: ")
    item_count = int(input("How many items are they buying? "))

    # ---------- PART 3: continue on a bad item count ----------
    if item_count <= 0:
        print("Item count must be greater than 0.\n")
        continue

    # ---------- PART 4: the INNER while loop ----------
    customer_total = 0
    item_number = 1

    while item_number <= item_count:

        item_name = input("Item name: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))

        # ---------- PART 5: item total and price band ----------
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than 0.")
            continue

        item_total = price * quantity

        print(item_name + ": " + str(quantity) + " x " + str(price) + " = " + str(item_total))

        customer_total = customer_total + item_total

        if item_total < 50:
            low_price_items = low_price_items + 1
        elif item_total <= 100:
            medium_price_items = medium_price_items + 1
        else:
            high_price_items = high_price_items + 1

        item_number = item_number + 1

    # ---------- PART 6: finish the customer ----------
    customers_served = customers_served + 1
    total_sales = total_sales + customer_total

    print(customer_name + "'s total: " + str(customer_total))

    next_customer = input("Next customer? (yes/no): ")

    if next_customer != "yes":
        billing = False


# ---------- PART 7: the NESTED for report ----------
print("\n=== Daily Report ===")

bands = [
    ("Low price items", low_price_items),
    ("Medium price items", medium_price_items),
    ("High price items", high_price_items)
]

for band_name, count in bands:
    print(band_name + ": ", end="")

    for i in range(count):
        print("*", end="")

    print()

print("Customers served:", customers_served)
print("Total sales:", total_sales)