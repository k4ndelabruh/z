import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    # Initialize app
    app = Flask(__name__)
    
    # Configure app
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_for_development')
    
    # Use SQLite instead of PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gruzovozoff.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.routes.auth_routes import auth
    from app.routes.main_routes import main
    from app.routes.request_routes import request
    
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(request)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app 