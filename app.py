#!/usr/bin/env python
from flask import Flask,render_template,request
import json
app= Flask(__name__)


 
@app.route("/")
def main():
    return render_template('index.html')
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
#read posted values from UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    #validate the received value
    if _name and _email and _password:
        return json.dumps({'html':'<span> All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span> Enter the required field</span>'})
    






if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)


