#otvoriti terminal, pozicijonirati se u direktoriju sa datotekom i izvrsiti navedene naredbe
#export FLASK_APP=routing.py
#flask run

from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
#render_templates trazi datoteke unutar templates/ direktorija
    return 'Bok, %s' % name

@app.route('/')
def index():
    return 'Pocetna'

#zadatak: napisi route za rjesavanje jednostavnih jednadzbi
#pozivi na nacin /calculator/1/+/2