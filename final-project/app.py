from flask import Flask
from flask import render_template
app = Flask(__name__)
import csv

def get_csv():
    csv_path = './static/data.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

@app.route('/<docNum>/')
def detail(docNum):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['docNum'] == docNum:
            return render_template(template, object=row)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)