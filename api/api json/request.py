
## VEIFYING PUT REQUEST

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


# all products before deletion
response = requests.get("http://127.0.0.1:5000/products")
print("\nAll products before deletion:")
print(response.json())

#Delete the product (DELETE)
print("\n=== Deleting product ===")
response = requests.delete("http://127.0.0.1:5000/products/2")
print("Delete Response:", response.json())


#Get all products after deletion
response = requests.get("http://127.0.0.1:5000/products")
print("\nAll products after deletion:")
print(response.json())