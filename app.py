from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tweede/<voornaam>')
def hello_city(voornaam):
    return f'Hello, {voornaam}!'    

