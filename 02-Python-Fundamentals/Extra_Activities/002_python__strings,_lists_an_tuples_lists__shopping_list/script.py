# # # SHOPPING LISTS # # #

shopping_list = ["milk", "oranges", "coffee", "sugar", "butter"]
print("Step 1.0: shopping list: ", shopping_list)

shopping_list.append("honey")
print("Step 1.1: ", shopping_list)

shopping_list.remove("milk")
print("Step 1.2: ", shopping_list)

shopping_list.insert(2, "soy_sauce")
print("Step 1.3: ", shopping_list)

shopping_list.pop()
print("Step 1.4: ", shopping_list)

last_minute_items = ["blueberries", "potatoes", "chicken"]
print("Step 1.5: ", last_minute_items)

shopping_list.extend(last_minute_items)
print("Step 1.6: Final shopping_list: ", shopping_list)

shopping_list.clear()
last_minute_items.clear()
print("Step 1.7: Empty lists: ", shopping_list, last_minute_items)