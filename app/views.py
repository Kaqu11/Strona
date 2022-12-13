from flask import render_template, Blueprint, request, redirect, flash
from flask_login import login_user, logout_user, login_required

from app.database import db
from app.models import User, Patient

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

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Rejestracja przebiegła pomyślnie')

            user = User(name=name,
                        surname=surname,
                        email=email,
                        password=password)

            db.session.add(user)
            db.session.commit()
            db.session.close()

            return redirect('/')
        else:
            flash('Email jest już zajęty')
            return redirect('/registration')

    return render_template('registration.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.password == password:
            flash('Sprawdź, czy wprowadzone dane są poprawne')
            return redirect('/login')

        login_user(user)
        flash('Zalogowano pomyślnie')
        return redirect('/')

    return render_template('login.html')


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@views.route('/test')
def test():
    User.query.delete()
    db.session.commit()
    user = User.query.all()
    return f'{[i.email for i in user]}'

@views.route('/patient-list', methods=['GET', 'POST'])
@login_required
def patientList():

    patient_list = Patient.query.all()
    return render_template('patient-list.html', patient_list=patient_list)

@views.route('/patient-list/delete/<int:id>', methods=['POST'])
@login_required
def patientDelete(id):
    Patient.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/patient-list')
