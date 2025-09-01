from flask import Blueprint, render_template
from flask_login import login_required, current_user
from instance.db import load, loadunique

views = Blueprint('views', __name__)

#--- PAGES ---
# 0. HOME PAGE
@views.route('/', methods= ['GET', 'POST'])
def home():
  return render_template('home.html',
                         base=load('base', '*'),
                         services=load('services', '*'),
                         departments=loadunique('users', 'udepartment'),
                         positions=loadunique('users', 'uposition'),
                         supervisors=loadunique('users', 'usupervisor'))

# 1. MAIN PAGE
@views.route('/mainpage')
@login_required
def mainpage():
  return render_template('mainpage.html',
                          base = load('base', '*'),
                          services = load('services', '*'),
                          current_user = current_user)



