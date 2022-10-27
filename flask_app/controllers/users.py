from flask import flash, request, redirect, session, url_for, render_template, json
import requests
from flask_app import app



@app.route('/')
def hello_world():
    data = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&start_date=2017-07-08&end_date=2017-07-11'
    response = requests.get(data)
    
    nasa_data = response.json()
    # print(nasa_data)
    # print(nasa_data[1])
    picture = nasa_data[1]["url"]
    print(nasa_data[1]["url"])

    return render_template('index.html', picture=picture)