from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from projecttakeoffapp.extensions import db
from projecttakeoffapp.models import Post, User
from projecttakeoffapp.helpers import sapology

station = Blueprint('station', __name__)

@station.route("/space")
@login_required
def space():
    
    return render_template("space.html")

@station.route("/asteroids")
@login_required
def asteroid():
    
    return sapology("something")

@station.route("/astronauts")
@login_required
def astronauts():
    astronauts = User.query.all()

    context = {
        'astronauts' : astronauts
    }

    return render_template('astronauts.html', **context)

@station.route("/posts")
@login_required
def posts():
    
    return sapology("something")
