from flask import Flask, render_template
from os import environ
from dotenv import load_dotenv

#Initialize app
app = Flask(__name__)
#Secret Key
SECRET_KEY = environ.get('SECRET_KEY')

@app.route('/<name>')
def home(name):
    return f'This is the home page. Hello {name} {SECRET_KEY}'

@app.route('/home')
def index():
    return render_template('index.html',title='This is the homepage')

