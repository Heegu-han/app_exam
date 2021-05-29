from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html",name="World")

@app.route("/hello/<uname>")
def hello(uname):
    return render_template("hello.html",name=uname)

if __name__ == "__main__":
    app.run(host="192.168.137.5",port=5001, debug=True)
