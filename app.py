import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movieDetails", methods=['POST'])
def movieDetails():
    baseUrl_251 = "http://www.omdbapi.com/"
    movieName_251 = request.form['movieName']
    apiKey = os.getenv('apiKey')

    params_251 = {'apiKey': apiKey, 't': movieName_251}
    response_251 = requests.get(baseUrl_251, params=params_251)

    if response_251.status_code == 200:
        movieData_251 = response_251.json()

        if movieData_251['Response'] == 'True':
            details_251 = " <h2>  Movie Details </h2> <br> "
            details_251 += f"Title: {movieData_251['Title']} <br>"
            details_251 += f"Year: {movieData_251['Year']} <br>"
            details_251 += f"Genre: {movieData_251['Genre']} <br>"
            details_251 += f"Director: {movieData_251['Director']} <br>"
            details_251 += f"Plot: {movieData_251['Plot']} <br>"
            return details_251+""
        else:
            return f"Error: {movieData_251['Error']}"
    else:
        return f"Error: Unable to fetch data. Status code: {response_251.status_code}"
