from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route("/home")
def home():
    return "Hello World !"

#REV_2 Séance 2 
@app.route("/division/<int:numerateur>/<int:denominateur>", methods=['GET'])
def division(numerateur, denominateur) : 
    resultat = numerateur/denominateur
    return str(resultat)
