from flask import Flask, request, jsonify,Response
from flask.views import View
from recommendation_engine import recommended_shows #Importing engine function
import pandas as pd
import pickle
from app import app
# from __main__ import app


# app = Flask(__name__)

# @app.route('/api/', methods=['POST'])
# def process_request():
# from flask import Flask, render_template, request
import csv
import os

# app = Flask(__name__)

@app.route('/a',methods=['GET'])
def get():
    return 'we are getting ready'



@app.route('/import',methods=['POST'])
def import_file():
    app.config['upload_folder']='uploads'
    if not os.path.exists(app.config['upload_folder']):
        os.makedirs(app.config['upload_folder'])
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'file not available '
    csv_file = request.files['file']

    if csv_file.filename == '':
        return 'no selected file'
    if csv_file:
        csv_filename = os.path.join(app.config['upload_folder'],csv_file.filename)
        csv_file.save(csv_filename)

    with open(csv_filename,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    return 'file uploaded successfully'
    
# if __name__ == '__main__':
#    app.run(debug=True)
