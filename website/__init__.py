from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.views import views

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hellostensetheisrntesrn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from website.events.events import events_bp
    from website.people.people import people_bp
    from website.kitty.kitty import kitty_bp

    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(kitty_bp, url_prefix='/kitty')
    app.register_blueprint(people_bp, url_prefix='/people')
    app.register_blueprint(views)

    from .models import Club, Income, Expense, Player, Payment, Debt, Game, Training

    create_database(app)

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        with app.app_context():
            # db.drop_all()
            db.create_all()

            # from .models import Club
            #
            # club = Club(name='DY Athletic')
            # db.session.add(club)
            # db.session.commit()
            # print('DY created')
        print("Created database!")
