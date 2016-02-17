# -*- coding: utf-8 -*-

import os
from flask import request, Blueprint, Flask, render_template, send_file
from datetime import datetime

app = Flask(__name__)
documento = Blueprint('documento', __name__)

# Where files are going to be uploaded
app.config['UPLOADED_FILES_DEST'] = 'uploadedFiles/'


@documento.route('/testUpload')
def index():
    """Renders from example."""
    return render_template('testUpload.html')


@documento.route('/upload', methods=['POST'])
def upload():
    """Upload a new file."""
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], file.filename))
    # app.config['UPLOADED_FILES_DEST'] + file.filename -> es el path
    # usar ese path para guardarlo en la base de datos.
    date = datetime.today()
    # si sqlAlchemy no agarra datetime.today(), datetime.utcnow() puede que funcione
    return 'Archivo subido en: ' + app.config['UPLOADED_FILES_DEST'] + file.filename

@documento.route("/download/<path:filename>")
def download(filename):
    """Downloads a file."""
    return send_file(app.config['UPLOADED_FILES_DEST'] + filename, as_attachment=True)
