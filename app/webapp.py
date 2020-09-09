from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
#from app import app
from app import create_app
from flask_bootstrap import Bootstrap

# Redirect to "next" page
from werkzeug.urls import url_parse

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
@server_bp.route('/index')
def index():
    return render_template("index.html")
