from flask import Flask

app = Flask(__name__)
# app = Flask() comes first to eliminate circular deps.
# Views may bepends on the above variable.
from app import views
