from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load dataset
df = pd.read_csv("coffee_roast_data.csv")

# Convert dataset into a dictionary for quick lookup
roast_data = df.set_index("Roast Type").to_dict(orient="index")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_roast = request.form.get('roast_type')
        if selected_roast in roast_data:
            details = roast_data[selected_roast]

            # Ensure the image exists before passing it
            image_path = os.path.join("static/images", details["Image Path"])
            if not os.path.exists(image_path):
                details["Image Path"] = "default.jpg"  # Fallback image

            return render_template('index.html', roast=selected_roast, details=details)

    return render_template('index.html', roast=None, details=None)

# Creating a new route for simply extracting the details
@app.route('/getdetails', methods=['GET'])
def get_details():
    roast_type = request.args.get('roast_type')  
    if roast_type in roast_data:
        details = roast_data[roast_type]
        return jsonify({"roast_type": roast_type, "details": details}) 
    return jsonify({"error": "Roast type not found"}), 404  


if __name__ == '__main__':
    app.run(debug=True)
