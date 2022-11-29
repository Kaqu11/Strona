from app.models import User
from app.views import views
from app.database import db
from loginmanager import login_manager
from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder='app/templates',
        static_folder='app/static'
    )

    app.debug = True
    app.secret_key = 'a206feaca73e86c740a2d017c1ead06d'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'

    db.init_app(app)

    login_manager.login_view = 'login'
    login_manager.init_app(app)

    app.register_blueprint(views)
    with app.app_context():
        db.create_all()
        db.session.commit()
        db.session.close()

    return app


if __name__ == '__main__':
    app = create_app()

    app.run()