from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from website.events.events import events_bp
from website.people.people import people_bp
from website.kitty.kitty import kitty_bp
from website.views import views


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hellostensetheisrntesrn'

    from .events import events
    from .kitty import templates
    from .people import people

    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(kitty_bp, url_prefix='/kitty')
    app.register_blueprint(people_bp, url_prefix='/people')
    app.register_blueprint(views)

    return app
