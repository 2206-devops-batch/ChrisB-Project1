from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome To Your Spy Journal!</h1>"

@app.route("/audio/")
def audio():
    return "<h1>Audio Steganography Configuration Coming Soon!</h1>"

@app.route("/visual/")
def visual():
    return "<h1>Visual Steganography Configuration Coming Soon!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
