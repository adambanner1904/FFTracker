from flask import Blueprint, render_template, request, flash
from website.models import Player
from website import db
from .forms import NewPlayerForm

people_bp = Blueprint('people', __name__, template_folder='templates',
                      static_folder='static', static_url_path='assets')


@people_bp.route('/')
def people():
    return render_template('people.html')


@people_bp.route('/add-player', methods=['GET', 'POST'])
def add_player():
    form = NewPlayerForm()

    name = form.name.data
    player_exists = Player.query.filter_by(name=name).first()
    if player_exists:
        flash("Player already exists", category='error')
    else:
        new_player = Player(name=name, credit=0)
        db.session.add(new_player)
        db.session.commit()
        flash('New player added!')

    return render_template('add_player.html', form=form)
