# -*- coding: utf-8 -*-

import os
from flask import request, Blueprint, Flask, render_template, send_file
from datetime import datetime
from app.scrum.model import clsArchivos, db

app = Flask(__name__)
documento = Blueprint('documento', __name__)

# Where files are going to be uploaded
app.config['UPLOADED_FILES_DEST'] = 'uploadedFiles/'


@documento.route('/testUpload')
def index():
    """Renders from example."""
    return render_template('testUpload.html')


@documento.route('/upload/<path:nombrePila>', methods=['POST'])
def upload(nombrePila):
    """Upload a new file."""
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], file.filename))
    date = datetime.today()
    url = str(app.config['UPLOADED_FILES_DEST'] + file.filename)
    newFile = clsArchivos(file.filename, url, date, nombrePila)
    db.session.add(newFile)
    db.session.commit()    
    return 'Archivo subido en: ' + app.config['UPLOADED_FILES_DEST'] + file.filename

@documento.route("/download/<path:filename>")
def download(filename):
    """Downloads a file."""
    return send_file(app.config['UPLOADED_FILES_DEST'] + filename, as_attachment=True)
