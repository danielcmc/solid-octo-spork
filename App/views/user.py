from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import *

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/r', methods=['GET'])
def r():
    return ('users')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    students = get_all_students()
    return render_template('users.html', students=students)


@user_views.route('/api/competitions', methods=['GET'])
def get_competition_endpoint():
    competitions = get_all_competitions()
    return jsonify(competitions)


@user_views.route('/api/competitions/{{id}}', methods=['GET'])
def get_competition_by_id_endpoint():
    competitions = get_competition(id)
    return jsonify(competitions)



@user_views.route('/api/details/{{username}}', methods=['GET'])
def get_detail_endpoint(username):
  display_user_info(username)
    

"""@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    students = get_all_users_json()
    return jsonify(users)
"""

@user_views.route('/api/users', methods=['GET'])
def get_user_page1(): 
  students = Student.query.all() 
  if not students: 
    return [] 
  students = [Student.get_json() for Student in students] 
  return students 


@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_Student(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_Student(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


@user_views.route('/create_competition')
def create_competition():
    name = "Example Competition"
    ExampleId=4
    create_Competition(name, ExampleId)
    return "Competition created successfully!"

@user_views.route('/login', methods=['POST'])
def user_login_view():
  data = request.json
  token = user_login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  return jsonify(access_token=token)

@user_views.route('/identify')
@jwt_required()
def identify_view():
  username = get_jwt_identity() # convert sent token to user name
  #retrieve regular user with given username
  user = RegularUser.query.filter_by(username=username).first()
  if user:
    return jsonify(user.get_json()) #jsonify user object
  #retrieve admin user with given username
  admin = Admin.query.filter_by(username=username).first()
  if admin:
    return jsonify(admin.get_json())#jsonify admin object