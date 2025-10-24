from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Product service is running!"

@app.route('/products')
def get_products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Smartwatch"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
