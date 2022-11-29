from flask import render_template, Blueprint, request, redirect, flash
from flask_login import login_user, logout_user, login_required

from app.database import db
from app.models import User

views = Blueprint('views', __name__,
                        template_folder='templates', static_folder='static')


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/registration', methods=['GET', 'POST'])
def registration():

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surrname']
        email = request.form['email']
        password = request.form['password']


        flash('Rejestracja przebiegla pomyslnie')

        user = User()

        user.name = name
        user.surname = surname
        user.email = email
        user.password = password

        db.session.add(user)
        db.session.commit()
        db.session.close()

        return redirect('/')

    return render_template('registration.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.password == password:
            flash('Please check your login details and try again.')

        login_user(user)
        flash('Logged in successfully.')
    return render_template('login.html')


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@views.route('/test')
def test():
  user = User.query.all()
  return f'{[i.email for i in user]}'