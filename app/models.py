from flask_login import UserMixin
from app.database import db


class Doctor(UserMixin, db.Model):
    __tablename__ = "doctor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    patient = db.relationship('Patient', secondary='visit', back_populates='doctor')

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def to_json(self):
        return {"name": self.name,
                "email": self.email}

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Patient(UserMixin, db.Model):
    __tablename__ = "patient"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    phone_number = db.Column(db.String(20), unique=False, nullable=False)
    sex = db.Column(db.Boolean, unique=False, nullable=False)
    pesel = db.Column(db.String(80), unique=True, nullable=False)

    doctor = db.relationship('Doctor', secondary='visit', back_populates='patient')


    def __init__(self, name, surname, password, phone_number, sex, pesel, visit):
        self.name = name
        self.surname = surname
        self.password = password
        self.phone_number = phone_number
        self.sex = sex
        self.pesel = pesel


class Visit(UserMixin, db.Model):
    __tablename__ = "visit"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
































