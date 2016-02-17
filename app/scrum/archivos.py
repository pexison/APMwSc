# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

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
        print(name,url,dateAr,idbacklog)
        checkTypeName = type(name) == str
        checkTypeUrl = type(url) == str
        #checkTypedate = type(dateAr) == DateTime
        checkTypeBacklog = type(idbacklog) == str

        if checkTypeName and checkTypeUrl and checkTypeBacklog:
            found = self.findName(name);
            checkIdBacklog = clsBacklog.query.filter_by(BL_name = idbacklog).all()
            
            if found == [] and checkIdBacklog != []:
                print(name,url,dateAr,idbacklog)
                newArch = clsArchivos(name,url,dateAr,idbacklog)
                newArch.url = url
                print(newArch)
                db.session.add(newArch)
                db.session.commit()
                return True
        return False
        
    
    def deleteArchive(self, name):
        
        checkTypeName = type(name) == str

        if checkTypeName:
            foundName = self.findName(name)

            if foundName != []:
                tupla = clsArchivos.query.filter_by(AR_nameArch = name).first()    
                db.session.delete(tupla)
                db.session.commit()
                return True
        return False  
        
    
    def modifyArchive(self, name, new_name):   
                    
        checkTypeName          = type(name) == str
        checkTypeNewName       = type(new_name) == str
     
        if checkTypeName  and checkTypeNewName:
            foundName    = self.findName(name)
            foundNewName = self.findName(new_name)

            if foundName != [] and (foundNewName == [] or new_name == name):
                newArchive                = clsArchivos.query.filter_by(AR_nameArch = name).first()
                newArchive.AR_nameArch    = new_name 
                db.session.commit()
                return True
        return False
    

# Fin Clase Archivos
