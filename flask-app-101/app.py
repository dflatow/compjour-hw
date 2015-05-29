import csv
from flask import Flask
from flask import abort
from flask import render_template, url_for, redirect
app = Flask(__name__)

def get_csv():
    csv_path = './static/crime_sample.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<category>/')
def detail(category):
    template = 'index.html'
    object_list = get_csv()
    filtered_list = [x for x in object_list if x['Category'] == category]
    return render_template(template, object_list=filtered_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)