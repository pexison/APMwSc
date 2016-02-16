# -*- coding: utf-8 -*-

import os
from flask import request, session, Blueprint, json, Flask, render_template
from flask.ext import uploads

app = Flask(__name__)
documento = Blueprint('documento', __name__)
app.config['UPLOADED_FILES_DEST'] = 'uploadedFiles/'
files = uploads.UploadSet('files', uploads.ALL)
uploads.configure_uploads(app, files)

@documento.route('/testUpload')
def index():
    return render_template('testUpload.html')


@documento.route('/upload', methods=['POST'])
def upload():
    """Upload a new file."""
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], file.filename))
    #files.save(file, name = file.filename)
    return url_for('index')
