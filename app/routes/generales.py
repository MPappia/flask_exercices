from ..app import app
from flask import render_template


@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

#REV-2
@app.route("/division/<int:numerateur>/<int:denominateur>", methods=['GET'])
def division(numerateur, denominateur) : 
    resultat = numerateur/denominateur
    return str(resultat)

#REV-3


# Retour cours
@app.route("/pays/<string:nom>")
def pays(nom):
    return render_template("pages/pays.html", pays=nom)