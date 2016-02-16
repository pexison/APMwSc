# -*- coding: utf-8 -*-

import os
from flask import request, session, Blueprint, json, Flask, render_template
from flask.ext.uploads import  *

documento = Blueprint('documento', __name__)

@documento.route('/testUpload')
def index():
    return render_template('testUpload.html')
    

@documento.route('/upload', methods=['POST'])
def upload():
    """Upload a new file."""
    print('saving')
    save(request._files['upload'])
    return url_for('index')
