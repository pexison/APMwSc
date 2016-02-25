# -*- coding: utf-8 -*-.

import sys
import unittest
from datetime import datetime

# Ruta que permite utilizar el módulo anexo.py
sys.path.append('../app/scrum')

from model import *
from backLog import *
from archivos import *



class TestArchivo(unittest.TestCase):

    def testInsertArchivoExist(self):
        # Insertamos los datos necesarios.
        aBacklog  = backlog()
        aBacklog.insertBacklog('Bxtyllz','Mxtyrzx',1)
        findId    = aBacklog.findName('Bxtyllz')
        idBacklog = findId[0].BL_idBacklog
        print('-------------------------------------------------------------------------------------------------------------------------')
        print(findId)

         # Inicio de la prueba.
        aArchive      = archivos()

        aArchive.insertArchive('VtXcyr','/foo/bar/baz', datetime.datetime.now(), idBacklog, 'ASSASAS')


        # Eliminamos los datos insertados.
        aArchive = aArchive.findName('VtXcyr')
        #aArchive.deleteArchive(aArchive.id)
        print('1')
        print(aArchive)
        aBacklog.deleteProduct('Bxtyllz')

if __name__ == '__main__':
    unittest.main()
