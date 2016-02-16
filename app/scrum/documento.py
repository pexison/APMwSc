# -*- coding: utf-8 -*-

import os
from flask                       import request, session, Blueprint, json, upload
from app.scrum.accions           import *
from app.scrum.backLog           import *
from app.scrum.actorsUserHistory import *
from app.scrum.userHistory       import *

history = Blueprint('history', __name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request._files['file']
    # Make the filename safe, remove unsupported chars
    filename = secure_filename(file.filename)
    # Move the file form the temporal folder to
    # the upload folder we setup
    # TODO nombre de proyecto en folder y mezclar la fecha con el nombre de
    # archivo al guardar. De esta forma se evita la sobreescritura de
    # archivos
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Redirect the user to the uploaded_file route, which
    # will basicaly show on the browser the uploaded file
    return filename

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #TODO cuidado con el UPLOAD_FOLDER
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
