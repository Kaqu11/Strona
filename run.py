from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates')

@app.route('/')
def hello_world():
    return render_template('index.html')