from .blueprints.default.views import default
from .helpers import create_db_tables, set_flask_environment
from .blueprints.extensions import db
from .extensions import migrate
from flask import Flask

def create_app(script_info=None):   # pylint: disable=W0613
    """Create the Flask app."""
    app = Flask(__name__)

    set_flask_environment(app)

    app.register_blueprint(default)

    db.init_app(app=app)
    migrate.init_app(app, db)

    # Create the tables
    create_db_tables(app, db)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    return app
