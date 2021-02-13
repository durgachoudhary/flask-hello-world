import time
import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'

@app.route('/one')
def first_route():
    time.sleep(random.random() * 0.2)
    return 'Ok'

@app.route('/two')
def second_route():
    time.sleep(random.random() * 0.4)
    return 'Ok'

@app.route('/three')
def third_route():
    time.sleep(random.random() * 0.6)
    return 'Ok'

@app.route('/four')
def fourth_route():
    time.sleep(random.random() * 0.8)
    return 'Ok'

@app.route('/error')
def oops():
    return ':('

if __name__ == "__main__":
    app.run(debug=True)
