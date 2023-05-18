from flask import Blueprint, render_template, redirect, url_for
from ..import counter
home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
@home.route('/home/')
def landing_page():
    print(f'About the render @home with counter={counter}')
    return render_template('home.html', counter=counter)

@home.route('/count/')
def count():
    global counter
    counter += 1
    return redirect(url_for('home.landing_page'))