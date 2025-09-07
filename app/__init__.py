# -*- coding: utf-8 -*-
"""
Updated on September 2025
"""

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap  # To use bootstrap styles

app = Flask(__name__)
#fa = FontAwesome(app)

app.config.from_object(Config)
app.static_folder = 'static'


bootstrap = Bootstrap(app)


from app import routes
