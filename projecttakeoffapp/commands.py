import click 
from flask.cli import with_appcontext

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    from projecttakeoffapp import db
    from projecttakeoffapp.models import User, Post
    db.create_all()
