from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.events.events import events_bp
from website.people.people import people_bp
from website.kitty.kitty import kitty_bp
from website.views import views

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hellostensetheisrntesrn'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .events import events
    from .kitty import kitty
    from .people import people

    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(kitty_bp, url_prefix='/kitty')
    app.register_blueprint(people_bp, url_prefix='/people')
    app.register_blueprint(views)

    create_database(app)

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all()
        print("Created database!")
