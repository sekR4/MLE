import pandas as pd
from flask import render_template

from worldbankapp import app
from preprocessing.prep import prepared_data

data = prepared_data()
print(data)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", data_set=data)

