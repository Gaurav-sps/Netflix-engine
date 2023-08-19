from flask import Flask, request, jsonify
from recommendation_engine import recommended_shows #Importing engine function
import pandas as pd
import pickle



from flask import Flask
app = Flask(__name__)
import controller, Shows_vectorizer, recommendation_engine, recommendation_api




@app.route('/')
def hello_world():
   return 'helloworld'

if __name__ == '__main__':
   app.run(debug=True)
