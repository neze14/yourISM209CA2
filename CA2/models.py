from main import db
from datetime import date


class User(db.Model):
    __tablename__= 'customerregister'
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False, default=date.today() )
    residential_address = db.Column(db.String(60), unique=False, nullable=False)
    nationality = db.Column(db.String(50), unique=False, nullable=False)
    national_identification_number = db.Column(db.Integer, unique=True, nullable=False)


    def __repr__(self):
        return '<Register {}>'.format(self.id)

