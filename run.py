from app.views import views
from app.database import db
from loginmanager import login_manager
from flask import Flask
from datetime import datetime

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

    from app.models import User, Patient

    with app.app_context():
        db.create_all()

        # # db.session.add(User('admin', 'admin', 'admin@gmail.com', 'admin'))
        # db.session.add(Patient('Krzysztof',
        #                        'Kononowicz',
        #                        '987654321',
        #                        True,
        #                        datetime.now().replace(second=0, microsecond=0)))
        # db.session.commit()
        # db.session.close()

    return app


if __name__ == '__main__':
    app = create_app()

    app.run()