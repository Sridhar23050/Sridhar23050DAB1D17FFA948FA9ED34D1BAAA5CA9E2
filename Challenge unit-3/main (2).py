
def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i].lower() == target_product.lower():
            indices.append(i)
    return indices

# Test case:
# Creating a list of products
products = ["apple", "orange", "banana", "Apple", "mango", "grapes", "apple"]

# Search for the product "apple" in the list
indices = linear_search_product(products, "apple")

# Print the indices of all occurrences of the product "apple"
if indices:
    print(f"The product 'apple' is found at indices: {indices}")
else:
    print("The product 'apple' is not found in the list")