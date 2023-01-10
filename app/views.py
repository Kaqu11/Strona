from flask import render_template, Blueprint, request, redirect, flash, session
from flask_login import login_user, logout_user, login_required

from app.database import db
from app.models import Doctor, Patient, Visit

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
        pesel = request.form['pesel']
        sex = int(request.form['sex'])
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        user = Patient.query.filter_by(pesel=pesel).first()

        if not user:
            flash('Rejestracja przebiegła pomyślnie')

            user = Patient(name=name,
                        surname=surname,
                        pesel=pesel,
                        sex=sex,
                        password=password,
                        phone=phone,
                        email=email)

            db.session.add(user)
            db.session.commit()
            db.session.close()

            return redirect('/')
        else:
            flash('Użytkownik już istnieje w bazie')
            return redirect('/registration')

    return render_template('registration.html')


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['choosePre']

        print(user_type)

        session['login_type'] = user_type

        if str(user_type) == "doctor":
            user = Doctor.query.filter_by(email=email).first()
        elif str(user_type) == "patient":
            user = Patient.query.filter_by(email=email).first()
            
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
    Doctor.query.delete()
    db.session.commit()
    user = Doctor.query.all()
    return f'{[i.email for i in user]}'

@views.route('/visit-list/<id>', methods=['GET', 'POST'])
@login_required
def patientList(id):
    visit_list = db.engine.execute(f'SELECT DISTINCT visit.date, patient.name, patient.surname, patient.phone FROM visit, patient WHERE visit.doctor_id == {id}')
    print(visit_list)
    return render_template('patient-list.html', visit_list=visit_list)

@views.route('/patient-list/delete/<int:id>', methods=['POST'])
@login_required
def patientDelete(id):
    Patient.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/patient-list')

@views.route('/user-details/<id>', methods=['GET', 'POST'])
@login_required
def userDetails(id):
    users = Patient.query.filter_by(id=id)

    return render_template('user-details.html', users=users)


