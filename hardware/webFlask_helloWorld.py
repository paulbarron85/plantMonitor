from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi Pies, this is Pi! Hello World!"

if __name__ == "__main__":
    app.run(host='192.168.1.74', port=80, debug=True)
