from App.models import User, Student, Competition, Participation
from App.controllers import competition

from App.database import db
from flask_jwt_extended import create_access_token

def create_Student(username, password):
    newStudent = Student(username=username, password=password)
    try:
      db.session.add(newStudent)
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      print(f'{username} already exists!')
    else:
      print(f'{username} created!')
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
