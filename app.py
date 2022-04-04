from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

##############################################################################
##############################################################################

@app.route('/', methods=['GET'])
def home():
    # Main page
    return render_template('index.html')

##############################################################################

@app.route('/aboutme', methods=['GET'])
def aboutme():
    # About me page
    return render_template('aboutme.html')

@app.route('/work', methods=['GET'])
def work():
    # Work page
    return render_template('work.html')


##############################################################################
##############################################################################


if __name__ == '__main__':
    app.run(debug=True)
