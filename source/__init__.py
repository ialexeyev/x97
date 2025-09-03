from flask import Flask

def create_app():
  app = Flask(__name__, static_folder='static', static_url_path='/static')
  app.config['SECRET_KEY'] = 'prismgt40x97'

  from .views import views
  from .models import models

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(models, url_prefix='/')
  
  return app
