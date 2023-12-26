from flask import Blueprint, render_template

events_bp = Blueprint('events', __name__, template_folder='templates',
                      static_folder='static', static_url_path='assets')


@events_bp.route('/')
def events():
    return render_template('events.html')


@events_bp.route('/add-training')
def add_training():
    return render_template('add_training.html')


@events_bp.route('/add-game')
def add_game():
    return render_template('add_game.html')
