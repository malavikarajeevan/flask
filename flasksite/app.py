from flask import Flask,render_template

APP=Flask(__name__)

@APP.route('/')
def home():
    return render_template('index.html')


APP.run(debug=True)