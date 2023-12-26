from flask import Blueprint, render_template

people_bp = Blueprint('people', __name__, template_folder='templates',
                      static_folder='static', static_url_path='assets')


@people_bp.route('/')
def people():
    return render_template('people.html')


@people_bp.route('/add-player')
def add_player():
    return render_template('add_player.html')
