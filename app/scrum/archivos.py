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
		'''Permite obtener todos los archivos de la tabla'''
		result = clsArchivos.query.all()
		return result

	
	def findName(self,name):
	'''Permite buscar un nombre de un archivo'''

		checkTypeName = type(name) == str

		if checkTypeName:
		    checkLongName = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME
		    
		    if checkLongName:
			oArchivos = clsArchivos.query.filter_by(AR_nameArch = name).all()
			return oArchivos
		return []
	
	
	def findIdArchives(self,idArchive):
     '''Permite buscar un elemento por su id'''
         
        checkTypeId = type(idArchive) == int
        found       = None
        
        if checkTypeId:
            found = clsArchivos.query.filter_by(AR_idArchivos = idArchive).first()
        return found

		
	def insertArchive(self,name,url,dateAr,idbacklog):
	'''Insertar un archivo'''

		checkTypeName = type(name) == str
		checkTypeUrl = type(url) == str
		#checkTypedate = type(dateAr) == DateTime
		checkTypeBacklog = type(idbacklog) == int

		if checkTypeName and checkTypeUrl and checkTypeBacklog:
			found = self.findName(name);
			checkIdBacklog = clsBacklog.query.filter_by(BL_idBacklog = idbacklog).all()
			
			if found == [] and checkIdBacklog != []:
				newArch = clsArchivos(name,url,dateAr,idbacklog)
				db.session.add(newArch)
				db.session.commit()
				return True
		return False
		
	
	def deleteArchive(self, name):
        '''Permite eliminar un archivo de la tabla'''
        
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
     '''Permite modificar el nombre de un archivo'''
                    
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
