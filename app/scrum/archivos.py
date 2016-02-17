# -*- coding: utf-8 -*-. 

import sys
# Ruta que permite utilizar el módulo model.py
sys.path.append('app/scrum')

from model import *

# Declaracion de constantes.
CONST_MAX_DESCRIPTION = 140
CONST_MIN_DESCRIPTION = 1
CONST_MAX_NAME        = 50
CONST_MIN_NAME        = 1
CONST_MIN_ID          = 1


class archivos(object):

	
	def findName(self,name):

		'''Permite buscar un nombre'''

		checkTypeName = type(name) == str

		if checkTypeName:
		    checkLongName = CONST_MIN_NAME <= len(name) <= CONST_MAX_NAME
		    
		    if checkLongName:
			oArchivos = clsArchivos.query.filter_by(AR_nameArch = name).all()
			return oArchivos
		return []

		
	def insertArchive(self,nameArch):

		checkTypeName = type(name) == str

		if checkTypeName: 
			newProd = clsArchivos(nameArch)
			db.session.add(newProd)
			db.session.commit()
			return True

		return False



# Fin Clase Archivos
