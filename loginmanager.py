from flask_login import LoginManager

from app.models import Doctor

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Doctor.query.get(int(user_id))

