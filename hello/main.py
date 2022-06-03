
from flask import Flask, flash, render_template, request, make_response, redirect, session, url_for
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest
import os
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] ='SUPER SECRETO'

tareas = ["comprar cafe", "comprar comida", "hacer tareas"]

class Loginform(FlaskForm):
    username = StringField('nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    SubmitField = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(500)
def critical_erro(error):
    return render_template('505.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    session['user-ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip =session.get('user_ip')
    login = Loginform()
    username=session.get('username')
    context ={
        'user_ip':user_ip, 
        'tareas':tareas,
        'login': login,
        'username': username
    }
    if login.validate_on_submit():
        username = login.username.data
        session['username']=username
        flash('nombre de usuario registrado con exito')
        return redirect(url_for('index'))
    return render_template('hello.html', **context)

