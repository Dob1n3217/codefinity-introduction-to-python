# 1. Initial inventory
vegetables = ["tomatoes", "potatoes", "onions"]

# 2. Remove "onions"
vegetables.remove("onions")

# 3. Add "carrots" only if missing
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# 4. Add "cucumbers" only if missing
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# 5. Sort and output
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)