from flask import Flask
from flask_login import LoginManager

def create_app():
  app = Flask(__name__, static_folder='../static', static_url_path='/static')
  app.config['SECRET_KEY'] = 'prismgt40x97'

  # Initialize Flask-Login
  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = 'views.home'
  login_manager.login_message = 'Please log in to access this page.'

  from .models import User
  
  @login_manager.user_loader
  def load_user(user_id):
    return User.get(user_id)
  
  from .views import views
  from .models import models

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(models, url_prefix='/')
  
  return app
