#!/usr/bin/python3
"""Database storage for the app
"""
from flask import app
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Define your SQLAlchemy models here
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    # Add other fields as needed

# Create a function to initialize the database with the Flask app
def init_app(app):
    db.init_app(app)

# Create a function to create the database tables
def create_tables():
    with app.app_context():
        db.create_all()
