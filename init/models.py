from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import UserMixin, login_user, logout_user, login_required
from instance.db import loadspec, newuser

models = Blueprint('models', __name__)

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
    
    @staticmethod
    def get(user_id):
        # Check if user exists in database
        data = loadspec('users', 'uid')
        for user in data:
            if user[0] == user_id:
                return User(user_id)
        return None
    
    @staticmethod
    def authenticate(user_id, password):
        # Authenticate user credentials
        data = loadspec('users', 'uid', 'upassword')
        for user in data:
            if user[0] == user_id and user[1] == password:
                return User(user_id)
        return None


#--- PROCESSORS ---
# 1. Sign in process
@models.route('/signinprocess', methods=['POST'])
def signinprocess():
  user_id = request.form['userID']
  password = request.form['userPsw']
  
  # Authenticate user
  user = User.authenticate(user_id, password)
  
  if user:
    login_user(user)
    return "OK"
  else:
    # Check if it's password issue or user ID issue
    data = loadspec('users', 'uid')
    user_exists = any(u[0] == user_id for u in data)
    
    if user_exists:
      return "PASS NOK"
    else:
      return "ID NOK"

# Logout route
@models.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('views.home'))

# 2. Sign up process
@models.route('/signupprocess', methods=['POST'])
def signupprocess():
  if(newuser(request.form['userFirstName'], request.form['userLastName'], request.form['userEmail'], request.form['userDepartment'], request.form['userPosition'], request.form['userSupervisor']) == "OK"):
    return "OK"
  else:
    return "NOK"