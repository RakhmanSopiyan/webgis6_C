from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TEMP storage (later replaced by PostGIS)
features = []

@app.route("/")
def home():
    return "WebGIS API running"

@app.route("/api/features", methods=["GET"])
def get_features():
    return jsonify(features)

@app.route("/api/features", methods=["POST"])
def add_feature():
    data = request.json
    features.append(data)
    return {"status": "saved"}, 201

if __name__ == "__main__":
    app.run(debug=True)
