from flask_login import LoginManager

from app.models import Doctor,Patient

from flask import session

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    login_type = session.get('login_type')

    if login_type == "doctor":
        return Doctor.query.get(int(user_id))
    else:
        return Patient.query.get(int(user_id))

