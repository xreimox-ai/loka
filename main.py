from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "AlphaShield Backend is running successfully!"
    })

if __name__ == '__main__':
    app.run()
