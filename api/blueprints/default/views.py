import os
from flask import Blueprint, jsonify
from sqlalchemy_utils import database_exists
from .models import User


default = Blueprint('default', __name__, template_folder='templates', static_folder='static')


@default.route('/', methods=['GET'])
def home():
    """Confirm that the application is working."""
    data = {
        'flask env': os.environ['FLASK_ENV'],
        'secret key': os.environ['SECRET_KEY'],
        'postgres host': os.environ['POSTGRES_HOST']
    }
    return jsonify(data), 200


@default.route('/db', methods=['GET'])
def db_exist():
    """Confirm that the database is working."""
    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_DB = os.environ['POSTGRES_DB']
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    db_exists = database_exists(db_conn_string)
    data = {
        'Database Exists': db_exists
    }
    return jsonify(data), 200


@default.route('/users', methods=['GET'])
def all_users():
    """Get all the users."""
    users = User.query.all()
    return jsonify(users), 200