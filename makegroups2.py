from __future__ import print_function
import os
import sys
import re

ffile = open("PruebaMcMahon.fasta", 'w')
gfile = open('PruebaMcMahon.groups', 'w')   #Genera los archivos en los que vamos a escribir



for inFile in list(os.walk('/home/guillermo/TFM/Datos/Ejemplo_McMahon/Muestras_McMahon/'))[0][2]: #Almacena los nombres de los archivos
    if not inFile.endswith("fna"):
        continue
    print (inFile)
    try:
        A = open('/home/guillermo/TFM/Datos/Ejemplo_McMahon/Muestras_McMahon/'+inFile, "r")
    except:
        print("Could not find file", file = sys.stderr)
        sys.exit(1)

    xx=0
    for line in A:
        xx+=1
        if xx%1000 ==0:
            print(xx, file = sys.stderr)
        if line.startswith(">"):
            seqName = line.lstrip('>').split('/')[0].replace(':','_') #Elimina el >, el /2 y sustituye ':' por '_'.
            group = inFile.split('.')[0]
            print('>' + seqName, file = ffile) #Imprime el ID al archivo .fasta
            print(seqName+'\t'+(group), file = gfile) #Imprime el ID y el nombre de la muestra al .groups
        else:
            print(line.strip(), file = ffile) #Imprime la secuencia al .fasta

sys.exit(0)
