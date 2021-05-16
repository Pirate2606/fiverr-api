import json
from models import People, db, Projects
from app import app


def insert_people():
    f = open('static/resources/people.json')
    json_file = json.load(f)

    for data in json_file:
        with app.app_context():
            people = People(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                address=data["address"],
                skills=str(data["skills"]),
            )
            db.session.add(people)
            db.session.commit()


def insert_project():
    f = open('static/resources/projects.json')
    json_file = json.load(f)

    for data in json_file:
        with app.app_context():
            project = Projects(
                project_name=data["project_name"],
                date_posted=data["date_posted"],
                department=data["department"],
                description=data["description"],
                skills=str(data["skills"]),
            )
            db.session.add(project)
            db.session.commit()
