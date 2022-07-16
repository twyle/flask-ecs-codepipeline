import sqlalchemy
import os

from .blueprints.default.models import User


def set_flask_environment(app) -> str:
    """Set the flask development environment.

    Parameters
    ----------
    app: flask.Flask
        The flask application object

    Raises
    ------
    KeyError
        If the FLASK_ENV environment variable is not set.

    Returns
    -------
    str:
        Flask operating environment i.e development

    """
    try:
        if os.environ['FLASK_ENV'] == 'production':  # pragma: no cover
            app.config.from_object('api.config.config.ProductionConfig')
        elif os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
            app.config.from_object('api.config.config.DevelopmentConfig')
        elif os.environ['FLASK_ENV'] == 'test':
            app.config.from_object('api.config.config.TestingConfig')
        elif os.environ['FLASK_ENV'] == 'stage':
            app.config.from_object('api.config.config.StagingConfig')
    except KeyError:
        app.config.from_object('api.config.config.DevelopmentConfig')
        return 'development'

    return os.environ['FLASK_ENV']

def seed_db(db):
    """Create the initial records."""
    db.session.add(User(
        email='lyle@notreal.com',
    ))
    db.session.add(User(
        email='michael@notreal.com',
    ))
    db.session.commit()


def create_db_tables(app, db):
    """Create the database tables if they do not exist."""
    with app.app_context():
        try:
            User.query.all()
        except sqlalchemy.exc.ProgrammingError as e:
            db.create_all()
            db.session.commit()
            seed_db(db)