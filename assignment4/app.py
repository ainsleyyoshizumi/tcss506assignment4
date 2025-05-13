#!/usr/bin/env python3
#make a flask hello world app
from flask import Flask, render_template, request, session, redirect, url_for
import os

from api.fetch_data import fetch_tripadvisor_data
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    session['city'] = 'Tacoma'
    session['state'] = 'WA'
    session['category'] = 'restaurants'

    if request.method == 'GET':
        if request.args.get('city'):
            session['city'] = request.args.get('city')
        if request.args.get('state'):
            session['state'] = request.args.get('state')
        if request.args.get('category'):
            session['category'] = request.args.get('category')
        
    # Create a data object with business information
    location_data = fetch_tripadvisor_data(
        session['city'],
        session['state'],
        session['category'],
        use_cache_only=True
    )

    return render_template(
        'index.html',
        city=session['city'],
        state=session['state'],
        category=session['category'],
        location_data=location_data
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
