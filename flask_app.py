# ✅ Flask module import (keyword)     
from flask import Flask, request  # 'Flask' is a class provided by the Flask library 

# ✅ Creating a Flask app instance (required pattern)
app = Flask(__name__)    # 'app' is a variable you can rename, '__name__' is standard

# ✅ Route definition (Flask decorator - keyword)
@app.route('/')          
def home():       
    if request.content_type == 'application/json':  # Check if Content-Type is application/json
        data = request.get_json()  # Reads the input as a dictionary
        if data:  # Check if JSON data is provided
            print(data)  
            return {"status": "received"}  
        else:  # Handle cases where no JSON data is sent
            return {"error": "No JSON data provided"}, 400  
    else:  # Handle unsupported Content-Type
        return {"error": "Unsupported Media Type. Content-Type must be 'application/json'."}, 415  

# ✅ Run the app if this file is executed directly
if __name__ == '__main__':  # Python standard boilerplate
    app.run(debug=True)     # 'debug=True' enables live reload (can be True/False)
