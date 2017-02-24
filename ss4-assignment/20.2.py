def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit]=quantity
    return inventory[fruit]

new_inventory = {}
add_fruit(new_inventory, "apples", 15)
print(new_inventory)
print(new_inventory["apples"]==15)
add_fruit(new_inventory, "apples", 25)
print(new_inventory)
print(new_inventory["apples"]==35)
