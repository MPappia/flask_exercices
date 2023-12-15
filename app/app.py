from flask import Flask
from flask import render_template
from .config import Config
from .routes import generales

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")
@app.route("/home")
def home():
    return "Hello World !"

#REV-2
@app.route("/division/<int:numerateur>/<int:denominateur>", methods=['GET'])
def division(numerateur, denominateur) : 
    resultat = numerateur/denominateur
    return str(resultat)

#REV-3
