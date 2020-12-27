import os
from flask import render_template, flash, redirect, url_for, request
from app import app

from flask_bootstrap import Bootstrap

# Redirect to "next" page
from werkzeug.urls import url_parse

# files
from flask import send_file, send_from_directory, safe_join, abort


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/playground')
def playground():
    return render_template("playground.html")

@app.route('/aboutMe')
def aboutMe():
    return render_template("aboutMe.html")


# Portfolio routes
@app.route('/portfolio_PhDThesis')
def portfolio_PhDThesis():
    return render_template("portfolio_PhDThesis.html")

@app.route('/portfolio_Smartsito')
def portfolio_Smartsito():
    return render_template("portfolio_Smartsito.html")

@app.route('/portfolio_Upskilling')
def portfolio_Upskilling():
    return render_template("portfolio_Upskilling.html")

@app.route('/portfolio_RecruitApp')
def portfolio_RecruitApp():
    return render_template("portfolio_RecruitApp.html")

@app.route('/portfolio_Logeo')
def portfolio_Logeo():
    return render_template("portfolio_Logeo.html")


@app.route('/portfolioFile/<pdf_id>', methods=['GET', 'POST'])
def portfolioFile(pdf_id):
    filename = f"{pdf_id}.pdf"
    uploads = os.path.join( app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)

# # Playground routes
# @app.route('/Playground01')
# def Playground01():
#     return render_template("playground_BankTransactions.html")
