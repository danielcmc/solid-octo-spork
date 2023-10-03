from App.models import User
from App.models import Admin
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def create_Admin(username, password):
    newA = Admin(username=username, password=password)
    db.session.add(newA)
    db.session.commit()
    return newA   

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

#def add_Competition(self, name: str, Creator: int):
 #       new_Competition = Competition(name=name, creator_id=self.id)
  #      db.session.add(new_Competition)
   #     db.session.commit()
    #    return new_Competition
    