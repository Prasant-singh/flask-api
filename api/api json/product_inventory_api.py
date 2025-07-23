### Create a Flask application that manages a product inventory with JSON data
# json data
# {
#   "id": 1,
#   "name": "Wireless Mouse",
#   "price": 24.99,
#   "quantity": 50,
#   "category": "Electronics"
# }


# Required API Endpoints:

# GET /products - List all products

# GET /products/<id> -  

# POST /products - Add new product (accepts JSON)

# PUT /products/<id> - Update product (accepts JSON)

# DELETE /products/<id> - Remove product

from flask import Flask,redirect,render_template,request,url_for,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("products.html",initial_products=products)


products = [
    {"id": 1, "name": "PC", "price": 40000, "quantity": 22, "category": "Electronics"},
    {"id": 2, "name": "Earphone", "price": 100, "quantity": 1, "category": "Electronics"},
    {"id": 3, "name": "Book", "price": 400, "quantity": 4, "category": "Study"}
]

@app.route("/products",methods=["GET","POST"])
def handle_products():
    if request.method=="GET":
        return jsonify(products)
    if request.method=="POST":
        new_product=request.get_json()
        new_id=max([ids['id'] for ids in products])+1 if products else 1
        new_product['id'] = new_id
        products.append(new_product)
        
        print(products)
        return jsonify({"status": "success", "product": new_product})

@app.route("/products/<int:product_id>",methods=['GET', 'PUT', 'DELETE'])

def handle_product(product_id):
    product=[product for product in products if product['id']==product_id]
    if not product:
        return jsonify({"status":"Failed","Message":"Id not present"})
    
    if request.method == "GET":
        return jsonify(product)
    
    elif request.method == "PUT":
        update_data = request.get_json()
        if not update_data:
            return jsonify({"status": "failed", "message": "No update data provided"}), 400
        
        
        for key, value in update_data.items():
            if key in product[0] and key != 'id': 
                product[0][key] = value
        
        return jsonify({"status": "success", "product": product[0]})
        
    elif request.method == "DELETE":
        product_index = None
        for i, p in enumerate(products):
            if p['id'] == product_id:
                product_index = i
                break
        
        deleted_product = products.pop(product_index)
        return jsonify({"status": "success", "deleted_product": deleted_product})


if __name__=="__main__":
    app.run(debug=True)