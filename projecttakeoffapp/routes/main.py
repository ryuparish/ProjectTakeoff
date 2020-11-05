from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from projecttakeoffapp.extensions import db
from projecttakeoffapp.models import Question, User
from projecttakeoffapp.helpers import apology

main = Blueprint('main', __name__)

@main.route("/")
def index():

    return render_template("index.html")

@main.route("/members")
def members():

    return render_template("members.html")

@main.route("/about")
def about():

    return render_template("about.html")

@main.route("/join")
def join():
    #TODO
    return apology("TODO")

@main.route("/videos")
def videos():
    #TODO
    return apology("TODO")

@main.route("/projects")
def projects():
    #TODO
    return apology("TODO")

