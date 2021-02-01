from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

import models

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost/customerregister'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost:5435/customerregister'


@app.route("/")
def home():
    return '''My name is Chinezelum Okadigbo. This is my CA2 work. 
    My GitHub URL is https://github.com/neze14''', render_template('home.html', title ="Home")


@app.route("/registration/")
def registration():
    return render_template('registration.html', title="REGISTRATION", information="Use this form to register")


@app.route("/process-registration/", methods=['POST'])
def process_registration():
    firstname = request.form['firstname']
    surname = request.form['surname']
    date_of_birth = request.form['date_of_birth']
    residential_address = request.form['residential_address']
    nationality = request.form['nationality']
    national_identification_number = request.form['national_identification_number']

    try:
        user = models.User(firstname=firstname, surname=surname, date_of_birth=date_of_birth, residential_address=residential_address, nationality=nationality, national_identification_number=national_identification_number)
        db.session.add(user)
        db.session.commit()

    except Exception as e:
        information = 'Could not submit. The error message is {}'.format(e.__cause__)
        return render_template('registration.html', title="REGISTRATION", information=information)

    information = 'User by name {} {} successfully added. The NIN is  {}.'.format(firstname, surname, national_identification_number)

    return render_template('registration.html', title="REGISTRATION", information=information)


if __name__ == "__main__":
    app.run(port=5005)

# BELOW IS TO CREATE THE DOCKER CONTAINER
# docker run -d -p5435:5435 -e
# POSTGRES_USER=postgres -e POSTGRES_PASSWORD=mtnregister -e
# POSTGRES_DB=postgres --name customerregister postgres:10

# docker exec -it customerregister bash
# psql -U postgres
# create database customerregister;

# FOR PYTHON CONSOLE
# from models import db
# db.create_all()
# * BACK IN TERMINAL *
# \c customerregister
# select * from customerregister