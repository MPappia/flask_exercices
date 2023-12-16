from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

bootstrap= Bootstrap(app)

from .routes import generales