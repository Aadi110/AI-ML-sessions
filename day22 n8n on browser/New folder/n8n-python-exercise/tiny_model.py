from flask import Flask, request, jsonify

app = Flask(__name__)

def predict(hours, attendance):
       score = hours * 4 + attendance * 0.5
       label = "Pass" if score >= 60 else "Fail"
       confidence = round(min(score / 100, 0.99), 2)
       return label, confidence

@app.route("/predict", methods=["POST"])
def predict_route():
       data = request.get_json()
       hours = data.get("study_hours", 0)
       attendance = data.get("attendance", 0)
       label, confidence = predict(hours, attendance)
       return jsonify({"prediction": label, "confidence": confidence})

if __name__ == "__main__":
       app.run(port=5000)