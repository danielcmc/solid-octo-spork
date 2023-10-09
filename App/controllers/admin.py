from App.models import User, Admin

from App.database import db
from flask_jwt_extended import create_access_token

def create_Admin(username, password, staff_id):
    newA = Admin(username=username, password=password, staff_id=staff_id)
    try:
      db.session.add(newA)
      db.session.commit()
    except Exception as e:
      db.session.rollback()
      print(f'{username} already exists!')
    else:
      print(f'{username} created!')
    return newA  

def get_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()

def get_Admin(id):
    return Admin.query.get(id)

def get_all_admins():
    return Admin.query.all()

def get_all_admins_json():
    admins = Admin.query.all()
    if not admins:
        return []
    admins = [Admin.get_json() for Admin in admins]
    return admins

def update_Admin(id, username):
    Admin = get_Admin(id)
    if Admin:
        Admin.username = username
        db.session.add(Admin)
        return db.session.commit()
    return None
