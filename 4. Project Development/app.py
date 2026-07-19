from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("credit_card_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    employment_days = float(request.form["employment_days"])

    data = pd.DataFrame({
        "AMT_INCOME_TOTAL": [income],
        "YEARS_EMPLOYED": [employment_days]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "✅ Credit Card Approved"
    else:
        result = "❌ Credit Card Rejected"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
