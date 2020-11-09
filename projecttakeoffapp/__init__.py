from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from projecttakeoffapp.commands import create_tables
from projecttakeoffapp.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from projecttakeoffapp.users.routes import users
    from projecttakeoffapp.posts.routes import posts
    from projecttakeoffapp.main.routes import main
    from projecttakeoffapp.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    app.cli.add_command(create_tables)



    return app

app = create_app()