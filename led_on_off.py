from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


@app.route("/")
def index():
    return render_template("control_panel.html")

@app.route("/on")
def led_on():
    GPIO.output(4, True)
    return render_template("control_panel.html")

@app.route("/off")
def led_off():
    GPIO.output(4, False)
    return render_template("control_panel.html")

if __name__ == "__main__":
    app.run(host="192.168.137.5",port=5001, debug=True)
