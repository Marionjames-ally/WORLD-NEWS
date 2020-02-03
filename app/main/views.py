from flask import render_template,request,url_for,redirect
from . import main

# views
@main.route('/')
def index():
    """
    a function that returns the index page
    :return:
    """
    return render_template('index.html')
