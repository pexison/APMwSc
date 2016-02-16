# -*- coding: utf-8 -*-

import os
from flask import request, session, Blueprint, json
from flask.ext.uploads import  *

documento = Blueprint('history', __name__)

@documento.route('/testUpload')
def index():
    return render_template('../../static/testUpload.html')

@documento.route('/upload', methods=['POST'])
def upload():
    """Upload a new file."""
    if request._method == 'POST':
        print('saving')
        save(request._files['upload'])
        return url_for('index')
