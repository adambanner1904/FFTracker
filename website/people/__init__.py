from select import select

from flask import Blueprint, render_template, request, flash, redirect
from website.models import Player
from website import db
from forms import NewPlayerForm, EditPlayerForm
from sqlalchemy import select

people_bp = Blueprint('people', __name__, template_folder='templates',
                      static_folder='static', static_url_path='assets')


@people_bp.route('/')
def people():
    players = db.session.scalars(select(Player)).all()
    return render_template('people.html', players=players)


@people_bp.route('/add-player', methods=['GET', 'POST'])
def add_player():
    form = NewPlayerForm()
    if form.validate_on_submit():
        name = form.name.data.lower()
        club_id = 1  # For now DY is the only club
        is_active = True  # Will always be true when creating them
        balance = float(form.balance.data)
        player_exists = Player.query.filter_by(name=name).first()
        if player_exists:
            flash("Player already exists", category='error')
        else:
            new_player = Player(name=name, balance=balance, is_active=is_active, club_id=club_id)
            db.session.add(new_player)
            db.session.commit()
            flash('New player added!')

    return render_template('add_player.html', form=form)


@people_bp.route('/edit-person/<name>', methods=['GET', 'POST'])
def edit_person(name):
    players = db.session.scalars(select(Player)).all()
    return render_template('edit_person.html', players=players)
