
### Presents a form to collect user information (name, email, age)

# Accepts the form submission as JSON data

# Processes the JSON data (validate, store, or manipulate it)

# Returns a JSON response with the processed data plus a status message


from flask import Flask,render_template,redirect,url_for,request,jsonify
import datetime

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('user_form.html')

@app.route('/process_user',methods=["POST"])
def process_user():
    response={
    "status": "error",
    "message": "",
    "original_data":None,
    "Processed_data":None
    }

    data=request.get_json()
    
    # Checking is data is Null
    if not data:
        response["message"]="No data provided"
        return jsonify(response)
    
    #Extracting individall data
    name=data.get("name")
    email=data.get("email")
    age=data.get("age")

    #Checking required fields
    req_fields=["name",'email','age']
    for field in req_fields:
        if field not in data:
            response["message"]="Missing fields"
            return jsonify(response)
        
    #Checking the data type
    # Name
    if not isinstance(name, str) or len(name.strip())==0:
        response["message"]="Name must be none empty string"
        return jsonify(response)
    #Email
    if isinstance(email,str) and "@" not in email:
        response["message"]="Email is not valid"
        return jsonify(response)
    #Age
    if isinstance(age,int) and age<0:
        response["message"]="AGe must be integer and greater than 0"
        return jsonify(response)


    try:
        Processed_data={
            "name":name.upper(),
            "email":email,
            "age":age,
            "received_at":datetime.datetime.now(),
            "is_adult": age>=18
        }
        response["Processed_data"]=Processed_data
        response['message']='User data processed successfully'
        response["status"]="success"
        response["original_data"]=data

        return jsonify(response)



    except:
        response['message'] = 'An error occurred'
        return jsonify(response)





if __name__=='__main__':
    app.run(debug=True)