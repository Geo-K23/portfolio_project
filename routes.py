#!/usr/bin/python3
"""Define routes and route handlers
"""

import json
from flask import request, jsonify, render_template
from app import app, db
from models import User, Product

poultry_products = [
    {'name': 'Fresh Eggs', 'price': 2.99},
    {'name': 'Whole Chicken', 'price': 5.99},
    {'name': 'Chicken Wings', 'price': 3.99},
]

# Load the poultry data from the JSON file
with open('data/poultry_data.json', 'r') as json_file:
    poultry_data = json.load(json_file)

""" Define a route for the home page"""
@app.route('/')
def home():
    return render_template('index.html')

""" Define routes and handlers for user registration, product listing, etc."""
@app.route('/register', methods=['POST'])
def register_user():
    """ Handle user registration logic"""
    return jsonify({'message': 'User registered successfully'})

"""Define routes and handlers for the products list"""
@app.route('/products')
def poultry_products_list():
    return render_template('product.html', products=poultry_products)

@app.route('/api/poultry', methods=['GET'])
def get_poultry_data():
    return jsonify(poultry_data)
