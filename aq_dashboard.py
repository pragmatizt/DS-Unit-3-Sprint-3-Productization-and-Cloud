"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template
import openaq

# setting flask
app = Flask(__name__)

# setting the api
api = openaq.OpenAQ()






@app.route('/')
def root():
    """This returns folder holding templates - home.html"""


    return render_template('home.html')

@app.route('/observations')
def get_data(city='Los Angeles', parameter='pm25'):
    """ Query OpenAQ for a city and corresponding air quality value """
    logs = []
    status, body = api.measurements(city=city, parameter=parameter)
    observations = [(obs['date']['utc'], obs['value'])
                      for entry in body['results']]
    for obs in observations:
        logs.append(datetime=obs[0], value=obs[1])
    return render_template('observations.html', logs=logs)

# PART 2 - raw list of tuples
@app.route('/raw')
def raw():
    # using str to convert it from tuples to string.
    return str(get_data(api, 'Los Angeles'))


if __name__ == '__main__':
    app.run()

#NOTES:
# renamed openaq_py.py as openaq
