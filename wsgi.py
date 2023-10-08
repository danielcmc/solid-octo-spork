import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import *

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_Admin('bob', 'bobpass')
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 


@user_cli.command("createAdmin", help="Creates a Competition")
@click.argument("username", default="Dave")
@click.argument("password", default="NBuster")
def create_admin_command(username, password):
    create_Admin(username, password)
    print(f'{username} is an Admin !')


@user_cli.command("createStudent", help="Creates a Student")
@click.argument("username", default="James")
@click.argument("password", default="T.Kirk")
def create_student_command(username, password):
    create_Student(username, password)
    print(f'{username} is an Student !')
"""
@user_cli.command("login", help="Lists users in the database")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def login_user_command(username, password):
    access_token = jwt_authenticate(username, password)
    if access_token:
        student = Student.query.filter_by(username=username).first()
        admin = Admin.query.filter_by(username=username).first()
        if student:
            return student, access_token, f'Token: {access_token}'
        elif admin:
            return admin, access_token, f'Access Token: {access_token}'
    return None, None, 'bad username or password given', 401
"""


@user_cli.command("login", help="Log in a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def login_user_command(username, password):
    access_token = jwt_authenticate(username, password)
    if access_token:
        student = Student.query.filter_by(username=username).first()
        admin = Admin.query.filter_by(username=username).first()
        if student:
            print(f'Student logged in!\nUser: {student}\nAccess Token: {access_token}')
        elif admin:
            print(f'Admin logged in!\nUser: {admin}\nAccess Token: {access_token}')
    else:
        print('Login unsuccessful!')

@user_cli.command("createCompetition", help="Creates a Competition")
@click.argument("name", default="RunTime")
def create_competition_command(name):
  admin = Admin.query.filter_by(username=username).first()
  if admin:
    Competition = create_Competition(Admin.id, name)
    create_Competition(name)
    print(f'{name} created!')



# Then define the command and any parameters and annotate it with the group (@)


# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_students())
    else:
        print(get_all_students_json()) 

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)