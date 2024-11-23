from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Shea Butter App!"

@app.route('/api/info')
def shea_info():
    data = {
        "product": "Shea Butter",
        "benefits": [
            "Moisturizes skin",
            "Reduces inflammation",
            "Rich in vitamins A, E, and F"
        ],
        "origin": "Northern Ghana"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

