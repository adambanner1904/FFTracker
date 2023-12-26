from flask import Blueprint, render_template

events_bp = Blueprint('events', __name__, template_folder='templates',
                      static_folder='static', static_url_path='assets')


@events_bp.route('/')
def events():
    return render_template('events.html')