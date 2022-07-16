# -*- coding: utf-8 -*-
"""Provide commands for starting the application, creating the database and seeding the database."""
from api import create_app
from flask.cli import FlaskGroup


app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    cli()
