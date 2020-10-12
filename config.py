import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PersonalWebsite'
    UPLOAD_FOLDER = 'static/documents'
    #UPLOAD_FOLDER = '/home/slopezza/LangsFiles'
