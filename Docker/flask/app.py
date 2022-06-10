from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    print("HIT API CALLS")
    return "<h1> HELLO </h1>"

# app.run()
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()