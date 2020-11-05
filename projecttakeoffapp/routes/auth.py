from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from projecttakeoffapp.extensions import db
from projecttakeoffapp.models import User

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    #TODO
    return apology("TODO")

@auth.route("/login", methods=['GET', 'POST'])
def login():
    #TODO
    return apology("TODO")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))