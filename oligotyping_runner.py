from __future__ import print_function
from subprocess import call
import os
import sys
import re

for inFile in list(os.walk('/home/guillermo/Projects/TFM/Datos/Ejemplo_McMahon/strain.analysis/oligotyping/PRUEBA_runner/muestras/'))[0][2]:
    if inFile.endswith(tuple(map(str, range(10)))):
        print (inFile)
    call('o-pad-with-gaps /home/guillermo/Projects/TFM/Datos/Ejemplo_McMahon/strain.analysis/oligotyping/PRUEBA_runner/muestras/' + inFile, shell=True)
    call('entropy-analysis /home/guillermo/Projects/TFM/Datos/Ejemplo_McMahon/strain.analysis/oligotyping/PRUEBA_runner/muestras/' + inFile + '-PADDED-WITH-GAPS --no-display', shell=True)
    #call('oligotype /home/guillermo/Projects/TFM/Datos/Ejemplo_McMahon/strain.analysis/oligotyping/PRUEBA_runner/muestras/' + inFile + '-PADDED-WITH-GAPS /home/guillermo/Projects/TFM/Datos/Ejemplo_McMahon/strain.analysis/oligotyping/PRUEBA_runner/muestras/' + inFile + '-PADDED-WITH-GAPS-ENTROPY -c ####QUE NUMERO DE POSICIONES?', shell=True)

