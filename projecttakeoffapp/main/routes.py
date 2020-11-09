from flask import render_template, request, Blueprint, redirect, url_for, abort
from projecttakeoffapp.models import Post
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
    abort(404)

@main.route("/projects")
def projects():
    #TODO
    abort(404)