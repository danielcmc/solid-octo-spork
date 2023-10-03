from App.models import User
from App.models import Admin
from App.models import Student
from App.database import db

def create_User(username, password):
    newA = Admin(username=username, password=password)
    db.session.add(newA)
    db.session.commit()
    return newA   

def create_Admin(username, password):
    newA = Admin(username=username, password=password)
    db.session.add(newA)
    db.session.commit()
    return newA   

def create_Student(username, password):
    newStudent = Student(username=username, password=password)
    db.session.add(newStudent)
    db.session.commit()
    return newStudent   


def get_student_by_username(username):
    return Student.query.filter_by(username=username).first()

def get_student(id):
    return Student.query.get(id)

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [Student.get_json() for Student in students]
    return students

def update_student(id, username):
    Student = get_student(id)
    if Student:
        Student.username = username
        db.session.add(Student)
        return db.session.commit()
    return None

#def add_Competition(self, name: str, Creator: int):
 #       new_Competition = Competition(name=name, creator_id=self.id)
  #      db.session.add(new_Competition)
   #     db.session.commit()
    #    return new_Competition
    