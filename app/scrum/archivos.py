# -*- coding: utf-8 -*-.

import sys
import datetime
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *
from backLog import *

# Declaracion de constantes.
CONST_MAX_NAME        = 50
CONST_MIN_NAME        = 1


class archivos(object):
    '''Clase que permite manejar los archivos'''
    def getAllArchives(self):
        result = clsArchivos.query.all()
        return result


    def findName(self,name):

        checkTypeName = type(name) == str
        if checkTypeName:
            checkLongName = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME

            if checkLongName:
                oArchivos = clsArchivos.query.filter_by(AR_nameArch = name).all()
                return oArchivos
        return []


    def findIdArchives(self,idArchive):

        checkTypeId = type(idArchive) == int
        found       = None

        if checkTypeId:
            found = clsArchivos.query.filter_by(AR_idArchivos = idArchive).first()
        return found


    def insertArchive(self,name,url,dateAr,idbacklog):
        oBackLog    = backlog()
        checkTypeName = type(name) == str
        checkTypeUrl = type(url) == str
        checkTypedate = type(dateAr) == DateTime
        checkTypeBacklog = type(idbacklog) == str

        

        if  checkTypeName and checkTypeUrl and checkTypeBacklog:
            
            checkIdBacklog = clsBacklog.query.filter_by(BL_name = idbacklog).all()

            
            x = oBackLog.searchFile(idbacklog,name)

            if x == True:
                print('Archivo repetido')
            
            if x == False and checkIdBacklog != []:
               
                newArch = clsArchivos(name,url,dateAr,idbacklog)
                newArch.url = url

                db.session.add(newArch)
                db.session.commit()

                return True


        return False



    def deleteArchive(self, name, nameBacklog):

        checkTypeName = type(name) == str
        checkTypeBacklog = type(nameBacklog) == str


        if checkTypeName and checkTypeBacklog:

            checkIdBacklog = clsBacklog.query.filter_by(BL_name = nameBacklog).all()

            foundName = self.findName(name)
            tupla = clsArchivos.query.filter_by(AR_nameArch = name, AR_nameBacklog = nameBacklog).first()

            if foundName != [] and checkIdBacklog != [] and tupla != None:       
                db.session.delete(tupla)
                db.session.commit()
                return True
        
        return False





# Fin Clase Archivos
