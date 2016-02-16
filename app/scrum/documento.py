# -*- coding: utf-8 -*-

import os
from flask import request, Blueprint, Flask, render_template

app = Flask(__name__)
documento = Blueprint('documento', __name__)
app.config['UPLOADED_FILES_DEST'] = 'uploadedFiles/'


@documento.route('/testUpload')
def index():
    return render_template('testUpload.html')


@documento.route('/upload', methods=['POST'])
def upload():
    """Upload a new file."""
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], file.filename))
    return 'Archivo subido en: ' + app.config['UPLOADED_FILES_DEST'] + file.filename
