from flask import render_template, Blueprint, request, redirect, flash

views = Blueprint('views', __name__,
                        template_folder='templates', static_folder='static')


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/registration', methods=['GET', 'POST'])
def registration():

    if request.method == 'POST':
        name = request.form['name']
        surrname = request.form['surrname']
        email = request.form['email']
        password = request.form['password']

        print(f'{name}, {surrname}, {email}, {password}')

        flash('Rejestracja przebiegla pomyslnie')

        return redirect('/')

    return render_template('registration.html')