import json

import pandas as pd
import plotly
import plotly.express as px

import plotly.graph_objects as go
from flask import render_template
from preprocessing.prep import prepared_data

from worldbankapp import app

data, df = prepared_data()
# print(data)


graph_one = []
for data_tuple in data:
    graph_one.append(
        go.Scatter(x=data_tuple[1], y=data_tuple[2], mode="lines", name=data_tuple[0])
    )

layout_one = dict(
    title="Some bla <br> ... and bla",
    xaxis=dict(title="Year", autotick=False, tick0=2000, dtick=25),
    yaxis=dict(title="Hectares"),
)

figures = [dict(data=graph_one, layout=layout_one)]

# ids for html tags
ids = [f"figure-{i}" for i, _ in enumerate(figures)]

# figures to json for javascript in html
figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

# NOTE: The code above does not throw errors. However, the HTML page
# does not show any graph. Let's try it with updated syntax

# https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
# https://stackoverflow.com/questions/63616028/how-to-integrate-plotly-express-chart-to-flask-app
# https://community.plotly.com/t/plotly-flask-heatmap-not-showing-on-localhost/50281
fig = px.line(
    df,
    x="year",
    y="prp_rural_pop",
    color="Country Name",
    title=r"% rural population by country",
)
graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html", ids=ids, figuresJSON=figuresJSON, graphJSON=graphJSON
    )

if __name__ == "__main__":
    print("figures", figures, "", sep="\n")
    print("fig", fig, "", sep="\n")

