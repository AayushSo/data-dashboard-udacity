from myapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data import return_figures

@app.route('/')
@app.route('/index')
def index():

    figures,titles,l = return_figures()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    print(titles[0])
    return render_template('index.html',
                           ids=ids,
						   titles=titles,
						   number_of_elements=l,
                           figuresJSON=figuresJSON)

@app.route('/dataset_cleaning')
def dataset_cleaning():
    return render_template('dataset_cleaning.html')
