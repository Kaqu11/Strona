from flask import render_template, Blueprint, request, redirect, flash

from database import db
from loginmanager import load_user
from app.models import User, UserTest

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

        print(f'{name}, {surname}, {email}, {password}')

        flash('Rejestracja przebiegla pomyslnie')

        user = UserTest(name, surname, email, password)
        load_user(user)

        db.session.add(user)
        db.session.commit()

        return redirect('/')

    return render_template('registration.html')


@views.route('/login')
def login():
    return render_template('login.html')