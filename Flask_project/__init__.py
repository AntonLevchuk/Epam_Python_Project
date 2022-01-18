from flask import Flask

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

# from views import views_login


login_manager = LoginManager()

app = Flask(__name__, static_folder="static")


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anton:qwerty@localhost/ProjectData'
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True)

login_manager.init_app(app)
login_manager.login_view = 'login'
