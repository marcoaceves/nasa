from flask import flash, request, redirect, session, url_for, render_template, json
import requests
from flask_app import app
import flask_app.controllers.creds as creds

import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
print (week_ago)
print (today)


from random import randrange
from datetime import timedelta

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60)
    random_second = randrange(int_delta)
    
    return start + timedelta(seconds=random_second)

from datetime import datetime



@app.route('/nasa')
def hello_nasa():
    api_key=creds.api_key
    data = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={week_ago}&end_date={today}'
    response = requests.get(data)
    
    nasa_data = response.json()
    nasa_data =list(reversed(nasa_data))
    print(nasa_data[1])
    # print(nasa_data[1])
    picture = nasa_data[1]["url"]
    picture2 = nasa_data[2]["url"]
    picture3 = nasa_data[3]["url"]
    for i in range(len(nasa_data)):
        print(nasa_data[i]["url"])

    return render_template('index.html', picture=picture, picture2=picture2, picture3 =picture3, nasa_data=nasa_data)

@app.route('/random_nasa')
def random_nasa():
    # random date generator
    d1 = datetime.strptime('06/20/1995', '%m/%d/%Y')
    todayran = datetime.today()
    print(d1, "d1")
    d2 = todayran
    print(d2, "d2")
    my_ran_date= random_date(d1, d2).date()

    print(my_ran_date, "random date!")

    api_key=creds.api_key
    data = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={my_ran_date}&concept_tags=True'
    response = requests.get(data)
    
    nasa_data = response.json()
    print(nasa_data, "random data")


    return render_template('random.html', nasa_data=nasa_data)