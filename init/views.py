from flask import Blueprint, render_template
from data.db import load 

views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template('base.html',
                         base=load('base', '*'))

