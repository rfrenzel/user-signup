from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup-form.html')

@app.route('/user-signup', methods =['POST'])
def signup_validate():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    email_error = ""

    


@app.route('/user-signup', methods = ['POST'])
def welcome():
    user_name = request.form['username']
    return render_template('welcome.html', name = username)


