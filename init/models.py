from flask import Blueprint, request
from instance.db import loadspec, newuser

models = Blueprint('models', __name__)


#--- PROCESSORS ---
# 1. Sign in process
@models.route('/signinprocess', methods=['POST'])
def signinprocess():
  data = loadspec('users', 'uid', 'upassword')
  result = "checking"
  for i in range(0, len(data)):
    if (data[i][0] == request.form['userid']):
      if (data[i][1] == request.form['userpass']):
        result = "OK"
        break
      else:
        result = "PASS NOK"
        break
    else:
      result = "ID NOK"   
  return result

# 2. Sign up process
@models.route('/signupprocess', methods=['POST'])
def signupprocess():
  if(newuser(request.form['newfname'], request.form['newlname'], request.form['newmail'], request.form['newdep'], request.form['newpos'], request.form['newsup']) == "OK"):
    return "OK"
  else:
    return "NOK"