#!/usr/bin/python3
"""
Main application initialization
"""
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

""" Load configuration settings from config.py"""
app.config.from_pyfile('config.py')

"""Initialize the database"""
db = SQLAlchemy(app)

"""Register routes from routes.py"""
from routes import *


if __name__ == '__main__':
    app.run(debug=True)
