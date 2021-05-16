from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(512))
    last_name = db.Column(db.String(512))
    email = db.Column(db.String(512))
    address = db.Column(db.String(512))
    skills = db.Column(db.String(512))

    def __init__(self, first_name, last_name, email, address, skills):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.skills = skills


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(512))
    date_posted = db.Column(db.String(512))
    department = db.Column(db.String(512))
    description = db.Column(db.String(512))
    skills = db.Column(db.String(512))

    def __init__(self, project_name, date_posted, department, description, skills):
        self.project_name = project_name
        self.date_posted = date_posted
        self.department = department
        self.description = description
        self.skills = skills
