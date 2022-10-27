from flask import flash, request, redirect, session, url_for, render_template, json
import requests
from flask_app import app
import flask_app.controllers.creds as creds

import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
print (week_ago)
print (today)

@app.route('/')
def hello_world():
    api_key=creds.api_key
    data = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={week_ago}&end_date={today}'
    response = requests.get(data)
    
    nasa_data = response.json()
    # print(nasa_data)
    # print(nasa_data[1])
    picture = nasa_data[1]["url"]
    picture2 = nasa_data[2]["url"]
    picture3 = nasa_data[3]["url"]
    print(nasa_data[1]["url"])
    print(nasa_data[2]["url"])
    print(nasa_data[3]["url"])

    return render_template('index.html', picture=picture, picture2=picture2, picture3 =picture3)