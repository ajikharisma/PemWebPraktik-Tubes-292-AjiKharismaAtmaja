from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from secrets import token_urlsafe
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()  # Memuat .env
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Mengaktifkan debug mode secara eksplisit
    app.config['DEBUG'] = True  # Ini memastikan debug mode aktif
    app.config['FLASK_ENV'] = 'development'

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = token_urlsafe(32)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

