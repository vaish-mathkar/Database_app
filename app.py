#!/usr/bin/env python
from flask import Flask,render_template,request
from flaskext.mysql import MySQL

import json
app= Flask(__name__)

mysql = MySQL()
#app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 
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
    
@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"





if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)


