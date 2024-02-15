from flask import Flask,render_template,request

APP=Flask(__name__)

@APP.route('/')
def home():
    return render_template('index.html')
@APP.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        result=request.form
        print(result)
    return render_template('success.html',result=result)


APP.run(debug=True)