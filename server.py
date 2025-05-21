import os
from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

#create Flask app
@app.route('/', methods=['GET'])
def server_check():
    return "MTCars Flask API is running!"

@app.route('/model', methods=['POST'])
def predict_route():
    to_predict = request.json
    pred = predict(to_predict)
    return jsonify({"predicted mpg": pred})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

    