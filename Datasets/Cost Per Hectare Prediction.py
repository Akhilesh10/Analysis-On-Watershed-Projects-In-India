from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load dataset
data = pd.read_csv("dataset.csv")

# Feature Engineering
data["Cost_Per_Hectare"] = data["Total Cost"] / data["Area Sanctioned"]
data["Central_Funding_Ratio"] = data["Central Share"] / data["Total Cost"]
data["State_Funding_Ratio"] = data["State Share"] / data["Total Cost"]
data["State_Avg_Area"] = data.groupby("State Name")["Area Sanctioned"].transform("mean")
data["District_Avg_Cost"] = data.groupby("District Name")["Total Cost"].transform("mean")

# Encode categorical data
le_state = LabelEncoder()
le_district = LabelEncoder()
data["State_Name_Encoded"] = le_state.fit_transform(data["State Name"])
data["District_Name_Encoded"] = le_district.fit_transform(data["District Name"])

# Prepare features & target
features = ["Central Share", "State Share", "Central_Funding_Ratio", "State_Funding_Ratio",
            "State_Avg_Area", "District_Avg_Cost", "State_Name_Encoded", "District_Name_Encoded"]
X = data[features]
y = data["Cost_Per_Hectare"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction Function
def predict_cost_per_hectare(state, district, central_share, state_share):
    total_cost = central_share + state_share
    state_avg_area = data[data["State Name"] == state]["Area Sanctioned"].mean()
    district_avg_cost = data[data["District Name"] == district]["Total Cost"].mean()

    input_data = pd.DataFrame({
        "Central Share": [central_share],
        "State Share": [state_share],
        "Central_Funding_Ratio": [central_share / total_cost],
        "State_Funding_Ratio": [state_share / total_cost],
        "State_Avg_Area": [state_avg_area],
        "District_Avg_Cost": [district_avg_cost],
        "State_Name_Encoded": [le_state.transform([state])[0]],
        "District_Name_Encoded": [le_district.transform([district])[0]],
    })

    return model.predict(input_data)[0]

# Web UI
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        state = request.form["state"]
        district = request.form["district"]
        central_share = float(request.form["central_share"])
        state_share = float(request.form["state_share"])

        prediction = predict_cost_per_hectare(state, district, central_share, state_share)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
