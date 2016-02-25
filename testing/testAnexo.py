# -*- coding: utf-8 -*-.

import sys
import unittest

# Ruta que permite utilizar el módulo anexo.py
sys.path.append('../app/scrum')

from anexo import *

class TestAnexo(unittest.TestCase):

    #############################################
    #         Pruebas para insertAnexo          #
    #############################################


#Para Carga
	Casos Bordes
		-Verificar que el archivo se pueda cargar con el nombre correspondiente
		-Archivo posee Mayuscula
		-Archivo posee minusculas
		-Archivo posee digitos
		-Archivo nombre vacio
		-Archivo nombre muy largo

	Casos Esquina
		-Sin Backlog
		-Descripcion de 140 o mas sin Backlog

	Casos maliciosos
		-El String no existe
		-Simbolos que representan PATH en nuestro SO
		-Archivos con caracteres reservados a directorio

Para Search
	Casos Bordes
		-Si el archivo existe
		-Si el archivo no existe
		-El Id del archivo es invalido
		-Valor del Id negativo

	Maliciosos
		-Verificar si la busqueda es invalida


Para Delete
	Casos Normal
		- El archivo existe y se borra exitosamente
		- El archivo no existe
		- Longuitud de archivo (grande y pequeña)
		- Backlog invalido
#
