#otvoriti terminal, pozicijonirati se u direktoriju sa datotekom i izvrsiti navedene naredbe
#export FLASK_APP=minimum.py
#flask run

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
