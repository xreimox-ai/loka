from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "AlphaShield Backend is running successfully!"
    })

@app.route('/<path:path>')
def catch_all(path):
    return jsonify({
        "status": "success",
        "message": f"AlphaShield Backend is running! Path: /{path}"
    })

if __name__ == '__main__':
    app.run()
