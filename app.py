# app.py
from flask import Flask, render_template
import json

app = Flask(__name__)

# Load data from JSON files (simulating database)
def load_data(filename):
    with open(f'static/data/{filename}.json', 'r') as file:
        return json.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/goals')
def goals():
    initiatives = load_data('initiatives')
    return render_template('goals.html', initiatives=initiatives)

@app.route('/progress')
def progress():
    progress_data = load_data('progress')
    return render_template('progress.html', progress=progress_data)

@app.route('/data')
def data():
    statistics = load_data('statistics')
    return render_template('data.html', statistics=statistics)

@app.route('/resources')
def resources():
    resources_data = load_data('resources')
    return render_template('resources.html', resources=resources_data)

if __name__ == '__main__':
    app.run(debug=True)
