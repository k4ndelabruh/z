from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title='Главная - Грузовозофф')

@main.route('/about')
def about():
    return render_template('about.html', title='О нас - Грузовозофф') 