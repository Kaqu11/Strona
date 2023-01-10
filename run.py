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

    from app.models import Doctor, Patient, Visit
    
    with app.app_context():
        db.drop_all()
        db.create_all()
    
        dc1 = Doctor('Kacper', 'Wojniak','kwojniak@lekarz.com','lekarz')
        dc2 = Doctor('Kim', 'Abdul','pletwa@lekarz.com','lekarz')

        pt1 = Patient('Krzysztof', 'Kononowicz', 'konon', 0, '12457896378','606823475', 'konon@pl')
        pt2 = Patient('Major', 'Suchodolski', 'nitro', 1, '19685445454', '2137997', 'dj00r@nt')
        pt3 = Patient('Jan', 'Wstawaj', '123', 1, '123456789555', '506731154', 'kimr@pl')


        #visit1 = Visit(datetime.now().replace(second=0, microsecond=0), doctor_id=dc1.id, patient_id=pt1.id)
        #visit2 = Visit(datetime.now().replace(second=0, microsecond=0), doctor_id=dc1.id, patient_id=pt2.id)
        
        dc1.patient.append(pt1)
        dc1.patient.append(pt2)
        dc2.patient.append(pt3)

        #pt1.doctor.append(dc1)
        #pt2.doctor.append(dc1)
        
        db.session.add(pt1)
        db.session.add(pt2)
        db.session.add(pt3)
        db.session.add(dc1)
        db.session.add(dc2)
        #db.session.add(visit1)
        #db.session.add(visit2)

        db.session.commit()
        db.session.close()

    return app


if __name__ == '__main__':
    app = create_app()

    app.run()
