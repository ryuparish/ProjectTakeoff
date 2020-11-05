from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from projecttakeoffapp.extensions import db
from projecttakeoffapp.models import Post, User
from projecttakeoffapp.helpers import apology

main = Blueprint('main', __name__)

@main.route("/")
def index():

    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/join")
def join():
    return render_template("join.html")

@main.route("/videos")
def videos():
    #TODO
    return apology("something")

@main.route("/projects")
def projects():
    #TODO
    return apology("something")

