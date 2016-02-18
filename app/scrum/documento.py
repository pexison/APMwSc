# -*- coding: utf-8 -*-
import sys
sys.path.append('app/scrum')

from archivos import *
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


@documento.route('/upload/<path:nombrePila>', methods=['POST'])
def upload(nombrePila):
    """Upload a new file."""
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], file.filename))
    date = datetime.utcnow()
    url = str(app.config['UPLOADED_FILES_DEST'] + file.filename)
    c = archivos()
    c.insertArchive(file.filename, url, date, nombrePila)  
    return ('', 204)

@documento.route("/download/<path:filename>", methods=['GET'])
def download(filename):
    """Downloads a file."""
    return send_file(filename, as_attachment=True)
