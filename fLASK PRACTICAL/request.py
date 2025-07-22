# import requests

# # Get current data
# response = requests.get("http://127.0.0.1:5000/products/1")
# print("Before Update:", response.json())
# print()
# # Update data
# update_data = {"name": "Super PC", "price": 70000}
# response = requests.put("http://127.0.0.1:5000/products/1", json=update_data)
# print("Update Response:", response.json())
# print()
# # Verify update
# response = requests.get("http://127.0.0.1:5000/products/1")
# print("After Update:", response.json())




import requests

# Step 1: Check if product exists (GET)
print("\n=== Checking product before deletion ===")
response = requests.get("http://127.0.0.1:5000/products/1")
print("Product 1:", response.json())

# Step 2: Get all products before deletion
response = requests.get("http://127.0.0.1:5000/products")
print("\nAll products before deletion:")
print(response.json())

# Step 3: Delete the product (DELETE)
print("\n=== Deleting product ===")
response = requests.delete("http://127.0.0.1:5000/products/1")
print("Delete Response:", response.json())

# Step 4: Verify deletion (GET again)
print("\n=== Verifying deletion ===")
response = requests.get("http://127.0.0.1:5000/products/1")
print("Product 1 after deletion:", response.json())

# Step 5: Get all products after deletion
response = requests.get("http://127.0.0.1:5000/products")
print("\nAll products after deletion:")
print(response.json())