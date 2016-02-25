# -*- coding: utf-8 -*-.

import sys
import unittest
import datetime

# Ruta que permite utilizar el módulo anexo.py
sys.path.append('../app/scrum')

from archivos import *

class TestArchivo(unittest.TestCase):

    #############################################
    #         Pruebas para insertArchivo        #
    #############################################

    # Caso inicial
    #Verificar que el archivo se pueda cargar con el nombre correspondiente
    # Prueba 1
    def testInsertArchivoExist(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        # Eliminamos los datos insertados.
        aArchive = aArchive.findName('VtXcyr')
        aArchive.deleteArchive(aArchive.id)
        aBacklog.deleteProduct('Bxtyllz')

    # Casos Normales
    #Verificar que el archivo se pueda cargar con el nombre correspondiente
    # Prueba 2
    def testInsertArchivoElement(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        # Inicio de la prueba.
        aArchive      = archivos()
        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')
        self.assertTrue(result)
        # Eliminamos los datos insertados.
        aArchive = aArchive.findName('VtXcyr')
        aArchive.deleteArchive(aArchive.id)
        aBacklog.deleteProduct('Bxtyllz')

    # Casos fronteras
    #Archivo posee Mayuscula
    # Prueba 3
    #Archivo posee minusculas
    # Prueba 4
    #Archivo posee digitos
    # Prueba 5
    #Archivo posee combinacion de todas las anteriores
    # Prueba 6
    #Archivo nombre muy largo
    # Prueba 7

    # Casos esquina
    #Sin Backlog
    # Prueba 8
    #Descripcion de 140 o mas sin Backlog
    # Prueba 9

    # Casos maliciosos
    #Simbolos que representan PATH en nuestro SO
    # Prueba 10
    #Archivo nombre vacio
    # Prueba 11

    #############################################
    #         Pruebas para searchArchivo        #
    #############################################

    # Caso inicial
    # Busqueda exitosa
    # Prueba 11

    # Casos normales
    #Si el archivo existe
    # Prueba 12
    #Si el archivo no existe
    # Prueba 13

    # Casos maliciosos
    #El Id del archivo es invalido
    # Prueba 14
    #Valor del Id negativo
    # Prueba 15


    #############################################
    #         Pruebas para deleteArchivo        #
    #############################################

    # Caso inicial
    # Prueba 16

    # Casos Normales
    # El archivo existe y se borra exitosamente
    # Prueba 17

    # Casos Esquinas
    # Backlog invalido
    # Prueba 18

    # Casos fronteras
    # Longuitud de archivo (grande y pequeña)
    # Prueba 19
    # Prueba 20

    # Casos maliciosos
    # Entrada vacia
    # Prueba 21

