from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password: str):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password: str) -> bool:
        """Check hashed password."""
        return check_password_hash(self.password, password)


class Student(User):
    __tablename__ = 'Student'
    participations = db.relationship('Participation', backref='user', lazy=True)
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


class Admin(User):
    __tablename__ = 'admin'

    def add_Competition(self, name: str, Creator: int):
        new_Competition = Competition(name=name, creator_id=self.id)
        db.session.add(new_Competition)
        db.session.commit()
        return new_Competition

    def get_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": 'admin'
        }

    def __repr__(self):
        return f'<Admin {self.id} : {self.username} >'

