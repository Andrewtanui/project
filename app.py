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

@app.route('/student')
def student():
    return 'This is the student page'

@app.route('/staff')
def staff():
    return 'This is the staff portal'

@app.route('/student/login')
def student_login():
    return 'Student Login Page'

@app.route('/student/settings/<int:id>')
def student_settings(id):
    return 'This is the student settings page. Id is {id}'

@app.route('/staff/login')
def admin_login():
    return 'This is the admin page'

@app.route('/staff/settings/<int:id>')
def staff_settings(id):
    return f'This is the staff settings section. Your id is {id}'