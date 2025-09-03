from flask import Blueprint, render_template
from instance.db import load, loadunique

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


