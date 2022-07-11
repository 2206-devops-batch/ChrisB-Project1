from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "<h1>Welcome To Your Spy Journal!</h1>"
        "For more details, please visit: <a href="https://github.com/2206-devops-batch/ChrisB-Project0">https://github.com/2206-devops-batch/ChrisB-Project0</a>"
    )


@app.route("/audio/")
def audio():
    return "<h1>Audio Steganography Configuration Coming Soon!</h1>"


@app.route("/visual/")
def visual():
    return "<h1>Visual Steganography Configuration Coming Soon!</h1>"


@app.route("/health.json")
def health():
    return jsonify({"status": "UP"}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
