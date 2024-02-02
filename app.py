import time
from threading import Timer
from flask import Flask, render_template, request, url_for, redirect, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

opacity = 1



@app.route('/over')
def over():
    return "over"


@app.route('/last_line')
def last_line():
    return str(opacity)


def timeout():
    global opacity
    for i in range(20):
        time.sleep(1)
        opacity -= 0.02
        if opacity < 0.5:
            return 'over'
        print(opacity)
    print("A")


def timer():
    t = Timer(10.0, timeout)
    t.start()




@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html", opacity=opacity)


@app.route('/update_text', methods=['POST'])
def update_text():
    global opacity
    text = request.form['text']
    print(f"Received text update: {text}")
    # You can perform any processing with the received text here
    if text:
        timer()
        opacity = 1
    return 'OK'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
