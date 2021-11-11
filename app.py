from enum import unique
from logging import debug
from os import name
import re
from flask import Flask
from flask.templating import render_template
from flask.wrappers import Request
from wtforms.validators import DataRequired
from form import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
from flask import request
import models
import secrets
from flask import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'QWERTYUIMNBVCZXADFH AJSDUSADUHASUD SDAD SDASDGHGH'

crypt = Bcrypt(app)

# database

models.db.app = app
models.db.init_app(app)
models.db.create_all()


@app.route('/home')
def home():
    return 'Hello ZeroAutumn'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        apikey = secrets.token_urlsafe(20)
        temp = models.User(form.username.data, form.email.data, crypt.generate_password_hash(form.password.data).decode('utf-8'), apikey)
        models.db.session.add(temp)
        models.db.session.commit()
        return f'\tYou have Succesfully Registered   make sure to note down your api key:      {apikey} '  
    return render_template('register.html', form = form)



# API ROUTE
# auth tokens are sent in headers (it also can be sent in auth but stfu and send in headers)
# requests.headers.get('header key value') can give the sent header
# the client should send their usrname and api key in the headers
# headers = {'user': 'username', 'apikey': 'key'}


def create_json(valid):
    if valid:
        # create json
        details = models.Book.query.all()
        bookList = models.Book.object_as_dict(details)
        d = { 'Books': bookList
        }
    else:
        # create invalid json
        d = 'Auth Error'
    
    return json.dumps(d)

@app.route('/api', methods =['GET'])
def api():
    usr = request.headers.get('user')
    key = request.headers.get('apikey')

    dbusr = models.User.query.filter_by(username = usr).first()
    print(dbusr)
    if dbusr:
        if dbusr.apiKey == key:
            res = app.response_class(response=create_json(True), status=200)
            return  res
            # send json valid json data
    
    res = app.response_class(response=create_json(False), status=401)
    return res
        # send invalid json data

if __name__ == '__main__':
    app.run(debug = True)