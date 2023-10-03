from App.database import db
from App.models import User

class Student(User):
    __tablename__ = "student"
    competitions = db.relationship('Competition', secondary="participation", overlaps='participants', lazy=True)
    point = db.Column(db.Integer, default=0)

    def participate_in_competition(self, competition):
        if isinstance(self, Student):
            participation = Participation(user=self, competition=competition)
            db.session.add(participation)
            db.session.commit()
            return participation
        else:
            return None

    def get_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": 'Student'
        }

    def __repr__(self):
        return f'<Student {self.id} : {self.username}>'