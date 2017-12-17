#otvoriti terminal, pozicijonirati se u direktoriju sa datotekom i izvrsiti navedene naredbe
#export FLASK_APP=autentifikacija.py
#flask run

from flask import Flask, render_template,request

app = Flask(__name__)

bazaPodataka = []


@app.route('/',methods = ['POST'])
def login():
    if request.method=='POST':
        #zadatak: ako su user i password u bazi podataka, upali ledicu, inace ispisi poruku da ih nema u bazi
        #if request.form...
    return render_template('login.html')

@app.route('dodajKorisnika/', methods = ['POST'])
def addUser():
    #koristeci login.html, napravi novi html koji ce sluziti za dodavanje korisnika u bazu
    

