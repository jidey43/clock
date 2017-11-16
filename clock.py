from flask import Flask
import schedule
import time
from threading import Thread
import RPi

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/add")
def add():
    schedule.every(1).seconds.do(ring)
    return "coucou"


def ring():
    print("Drrrrrriiinng")


def run_scheduled():
    while 1:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    t = Thread(target=run_scheduled)
    t.start()
    app.run()


