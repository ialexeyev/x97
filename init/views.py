from flask import Blueprint, render_template, request
from data.db import load, loadspec, loadunique, newuser

views = Blueprint('views', __name__)

#--- PAGES ---
# 0. HOME PAGE
@views.route('/')
def home():
  return render_template('home.html',
                         base=load('base', '*'),
                         services=load('services', '*'),
                         departments=loadunique('users', 'udepartment'),
                         positions=loadunique('users', 'uposition'),
                         supervisors=loadunique('users', 'usupervisor'))

# 1. MAIN PAGE
@views.route('/mainpage')
def mainpage():
  return render_template('mainpage.html',
                          base = load('base', '*'),
                          services = load('services', '*'))



#--- PROCESSORS ---
# 1. Sign in process
@views.route('/signinprocess', methods=['POST'])
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
@views.route('/signupprocess', methods=['POST'])
def signupprocess():
  if(newuser(request.form['newfname'], request.form['newlname'], request.form['newmail'], request.form['newdep'], request.form['newpos'], request.form['newsup']) == "OK"):
    return "OK"
  else:
    return "NOK"