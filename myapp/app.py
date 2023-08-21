from flask import Flask, request, jsonify
from recommendation_engine import recommended_shows #Importing engine function
import pandas as pd
import pickle



from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
import controller, Shows_vectorizer, recommendation_engine, recommendation_api




# @app.route('/')
# def hello_world():
#    return 'helloworld'


import os


app.secret_key = os.urandom(24)  # Used for session encryption

users = {}  # In-memory user database (for demonstration purposes)

@app.route('/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      if username in users and users[username] == password:
         session['username'] = username
         return redirect(url_for('dashboard'))

   return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      if username not in users:
         users[username] = password
         return redirect(url_for('login'))

   return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
   if 'username' in session:
      username = session['username']
      return redirect(url_for('engine'))
      # return f"Welcome, {username}! This is your dashboard."
      # return render_template('engine.html')
   return redirect(url_for('login'))

@app.route('/engine')
def engine():
   return render_template('engine.html')


@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('login'))



if __name__ == '__main__':
   app.run(debug=True)


