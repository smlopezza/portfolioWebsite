import os
from flask import render_template, flash, redirect, url_for, request
from app import app

from flask_bootstrap import Bootstrap
import git  # GitPython library

# Redirect to "next" page
# from werkzeug.urls import url_parse
from werkzeug.utils import safe_join
# from flask import safe_join

# files
# from flask import send_file, send_from_directory, safe_join, abort
from flask import send_file, send_from_directory, abort


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

@app.route('/portfolio_Speaking_Community')
def portfolio_Speaking_Community():
    return render_template("portfolio_Speaking_Community.html")

@app.route('/portfolio_CookFlow_Agent_v1')
def portfolio_CookFlow_Agent_v1():
    return render_template("portfolio_CookFlow_Agent_v1.html")

@app.route('/portfolio_CookFlow_Agent_v2')
def portfolio_CookFlow_Agent_v2():
    return render_template("portfolio_CookFlow_Agent_v2.html")

@app.route('/portfolio_SofIA')
def portfolio_SofIA():
    return render_template("portfolio_SofIA.html")

@app.route('/portfolio_DevFest2025')
def portfolio_DevFest2025():
    return render_template("portfolio_DevFest2025.html")

@app.route('/portfolio_FinancialReports')
def portfolio_FinancialReports():
    return render_template("portfolio_FinancialReports.html")
    


@app.route('/portfolioFile/<pdf_id>', methods=['GET', 'POST'])
def portfolioFile(pdf_id):
    filename = f"{pdf_id}.pdf"
    uploads = os.path.join( app.root_path, app.config['UPLOAD_FOLDER'])    
    return send_from_directory(directory=uploads, path=filename)

# Playground routes
@app.route('/playground_Titanic')
def playground_Titanic():
    return render_template("playground_Titanic.html")



# Webhook route for automatic deployment in PythonAnywhere
# From: https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664
# @app.route('/update_server', methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         repo = git.Repo('https://github.com/smlopezza/portfolioWebsite')
#         origin = repo.remotes.origin
#         origin.pull()
#         return 'Updated PythonAnywhere successfully', 200
#     else:
#         return 'Wrong event type', 400

# https://www.youtube.com/watch?v=AZMQVI6Ss64
@app.route('/update_server', methods=['POST'])
def update_server():
    repo = git.Repo('./portfolioWebsite')
    origin = repo.remotes.origin
    repo.create_head('master',
                     origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200
