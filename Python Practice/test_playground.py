store_inventory = {
    "apple": 1.50,
    "milk": 3.00,
    "bread": 2.50,
    "coffee": 5.00
}

# Notice the glitchy numbers mixed in!
customer_cart = ["apple", "bread", 404, "milk", "orange", 10] 

def process_checkout(cart, inventory):
    total_cost = 0
    for i in cart:
        try:
            cartElement = int(i)
        except ValueError:
            if i not in inventory:
                print("Invalid key not detected. Skipping...")
                continue
            total_cost += inventory[i]
            continue

        else:
            print("Invalid interger detected. Skipping...")
            continue

    print(f"The total cost of your orders is {total_cost}")

process_checkout(customer_cart, store_inventory)

