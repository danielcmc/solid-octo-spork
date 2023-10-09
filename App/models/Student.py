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

    def add_Competition_to_student(self, student_id: int, competition_id: int):
        student = self.get_student(student_id)
        competition = self.get_competition(competition_id)
        if student and competition:
            student.competitions.append(competition)
            db.session.add(student)
            db.session.commit()
            return student
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