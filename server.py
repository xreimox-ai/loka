cat << 'EOF' > server.py
from flask import Flask, jsonify, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Server is online!", "app": "AlphaShield Backend"})

@app.route('/get_sms', methods=['GET'])
def get_sms():
    number = request.args.get('number')
    if not number:
        return jsonify({"error": "No number provided"}), 400

    try:
        url = f"https://online-sms.org/api/get-messages?number={number}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF
