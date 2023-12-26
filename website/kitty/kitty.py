from flask import Blueprint, render_template

kitty_bp = Blueprint('kitty', __name__, template_folder='templates',
                     static_folder='static', static_url_path='assets')


@kitty_bp.route('/')
def kitty():
    return render_template('kitty.html')
