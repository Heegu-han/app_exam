from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    result = "<!DOCTYPE HTML><html><head><title>Hello</title></head>"
    result = result + "<body><h1>Hello world</h1></body></html>"
    return result

@app.route("/hello/<uname>")
def hello(uname):
    result = "<!DOCTYPE HTML><html><head><title>Hello</title></head>"
    result = result + f"<body><h1>Hello {uname}</h1></body></html>"
    return result

if __name__ == "__main__":
    app.run(host="192.168.137.5",port=5001, debug=True)
