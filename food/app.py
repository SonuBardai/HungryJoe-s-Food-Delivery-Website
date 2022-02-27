from flask import Flask, request, redirect, session, url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask("app")
app.secret_key="secretkey"

with open(os.path.join(app.root_path, 'food\\static\\config.json'), 'r') as f:
    params = json.load(f)["params"]

app.config['SQLALCHEMY_DATABASE_URI'] = params['database_uri']
db = SQLAlchemy(app)

from food import routes