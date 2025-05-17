#!/usr/bin/env python3
#make a flask hello world app
from flask import Flask, render_template, request, session, redirect, url_for
import os

from api.fetch_data import fetch_tripadvisor_data
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    # Default to Tacoma if no city is selected
    city = session.get('city', 'Tacoma')
    state = session.get('state', 'WA')
    category = session.get('category', 'restaurants')
    
    # Fetch data for the default or selected city
    location_data = fetch_tripadvisor_data(
        city,
        state,
        category,
        use_cache_only=True
    )

    return render_template(
        'index.html',
        city=city,
        state=state,
        category=category,
        location_data=location_data
    )

@app.route('/city/<city_name>')
def city_view(city_name):
    # Capitalize city name for consistency
    city = city_name.capitalize()
    state = 'WA'  # All cities are in Washington
    
    # Store the selected city in session
    session['city'] = city
    session['state'] = state
    
    # Initialize categories dictionary to store all data
    categories = {}
    
    # Fetch data for all categories
    for category in ['restaurants', 'hotels', 'attractions']:
        categories[category] = fetch_tripadvisor_data(
            city,
            state,
            category,
            use_cache_only=True
        )
    
    return render_template(
        'index.html',
        city=city,
        state=state,
        category='all',  # Show all categories
        location_data=categories
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
