from flask import Flask as flask    # type:ignore
from flask_sqlalchemy import SQLAlchemy # type:ignore
from flask_cors import CORS # type:ignore 

app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

