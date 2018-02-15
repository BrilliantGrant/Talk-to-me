from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Doctor.query.get(int(user_id))


class Admin(UserMixin,db.Model):
    ___tablename__ = 'admin'

    id=  db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
  

    def __repr__(self):
        return f'User {self.username}'

class Doctor(UserMixin,db.Model):
    ___tablename__ = 'doctor'

    id=  db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    doc_details = db.relationship('Doctor_details', backref='docdetails',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
  

    def __repr__(self):
        return f'User {self.username}'

    
    @classmethod
    def get_doct(cls):
        Doctor = doctor.query.all()
        return doctor
    @classmethod
    def clear_doc(cls):
        Doctor.all_doctor.clear()



class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String())
    sad = db.Column(db.String())
    feeling = db.Column(db.String())
    mood = db.Column(db.String())
    category = db.Column(db.String(255))

    talks = db.relationship("Talks", backref="patient", lazy = "dynamic")



    def save_patients(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_patients(cls):
        Patient = patient.query.all()
        return patient
    @classmethod
    def clear_pitches(cls):
        Patient.all_patient.clear()

    def get_pitches(id):
        patient = Patient.query.all()
        return patient

     @classmethod
    def get_categories(cls, category):
        pitch_cat = Pitch.query.filter_by(category=category)
        return pitch_cat

    def __init__(self,body, category):
       
        self.body= body
        self.category= category



    

class Talks(db.Model):
    __tablename__ = 'talks'

    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String())
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))

    body=db.Column(db.String)
    
    def save_talks(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_talks(cls):
        Talks = talks.query.all()
        return talks
    @classmethod
    def clear_pitches(cls):
        Talks.all_patient.clear()
    def get_pitches(id):
        patient = Patient.query.all()
        return patient

class DocTalk(db.Model):
    __tablename__ = 'doctalks'

    id = db.Column(db.Integer,primary_key = True)
    body=db.Column(db.String)
    
    def save_doctalks(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_doctalks(cls):
        DocTalk = doctalks.query.all()
        return talks
    @classmethod
    def clear_pitches(cls):
        Talks.all_patient.clear()
    def get_pitches(id):
        patient = Patient.query.all()
        return patient



class PatientTalk(db.Model):
    __tablename__ = 'patienttalks'

    id = db.Column(db.Integer,primary_key = True)
    body=db.Column(db.String)
    
    def save_patienttalks(self):

class Doctor_details(db.Model):
    __tablename__ = 'docdetails'
    id = db.Column(db.Integer,primary_key = True)
    license = db.Column(db.String(255))
    phone_number = db.Column(db.Integer())
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    doc_id = db.Column(db.Integer, db.ForeignKey("doctor.id"))
    
    def save_docdetails(self):

        db.session.add(self)
        db.session.commit()

    @classmethod

    def get_patienttalks(cls):
        DocTalk = doctalks.query.all()
        return talks
    @classmethod
    def clear_pitches(cls):
        Talks.all_patient.clear()
    def get_pitches(id):
        patient = Patient.query.all()
        return patient



    def get_docdetails(cls):
        Doctor_details = docdetails.query.filter_by(id=id).all()
        return talks
    @classmethod
    def clear_docdetails(cls):
        Talks.all_patient.clear()
   

