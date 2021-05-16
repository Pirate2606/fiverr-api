from flask import Flask
from flask_restful import Api, Resource
from config import Config
from cli import create_db
from models import db, Projects, People
import insertInDatabase
from urllib.parse import unquote
import json

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
app.cli.add_command(create_db)
db.init_app(app)


class InsertPeople(Resource):
    def get(self):
        insertInDatabase.insert_people()
        return "Successfully saved to database"

    def post(self, obj):
        data = unquote(obj)
        json_data = json.loads(data)
        people = People(
            first_name=json_data["first_name"],
            last_name=json_data["last_name"],
            email=json_data["email"],
            address=json_data["address"],
            skills=str(json_data["skills"]),
        )
        db.session.add(people)
        db.session.commit()
        return {"data": "Posted"}


class InsertProjects(Resource):
    def get(self):
        return insertInDatabase.insert_project()

    def post(self, obj):
        data = unquote(obj)
        json_data = json.loads(data)
        project = Projects(
            project_name=json_data["project_name"],
            date_posted=json_data["date_posted"],
            department=json_data["department"],
            description=json_data["description"],
            skills=str(json_data["skills"]),
        )
        db.session.add(project)
        db.session.commit()
        return {"data": "Posted"}


class SuitablePerson(Resource):
    def get(self, unique_id):
        project = Projects.query.filter_by(id=unique_id).first()
        people = People.query.all()
        skills_required = eval(project.skills)
        skilled_person = dict()
        for skill in skills_required:
            for p in people:
                if skill in set(eval(p.skills)):
                    if p.id in skilled_person:
                        skilled_person[p.id] += 1
                    else:
                        skilled_person[p.id] = 1
        return dict(sorted(skilled_person.items(), key=lambda item: item[1], reverse=True))


api.add_resource(InsertPeople, '/insert-people-to-database', '/insert-people-to-database/<obj>')
api.add_resource(InsertProjects, '/insert-projects-to-database', '/insert-projects-to-database/<obj>')
api.add_resource(SuitablePerson, '/search-person/<unique_id>')


if __name__ == '__main__':
    app.run()
