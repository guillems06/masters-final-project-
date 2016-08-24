from __future__ import print_function
import sys #Importar funciones para contar argumentos etc
#scp ./samplecreator.py guillermo@zobel:~/Projects/TFM/Datos/Ejemplo_McMahon/oligot.analysis/samplecreator.py

#Le voy a introducir dos argumentos, el .fasta y el .count_table para que los almacene, de modo que va a poder hacerlo con cualquier fichero de este tipo, por si es util en futuros proyectos.
if len(sys.argv) != 3:   #Comprobamos que el numero de argumentos utilizados es el correcto, primero el fasta, luego el count; se pone tres porque este script se pondra despues de "python" y se cuenta como argumento
    print("Please, input the fasta and count files", file = sys.stderr)
    sys.exit(1)
else:
    pass
try:
    fasta = open(sys.argv[1], "r")
    print ("Fasta file found", file = sys.stderr)
except:
    print ("Couldn't find fasta file", file = sys.stderr)
    sys.exit(1)
    
try:
    count = open(sys.argv[2], "r")
    print ("Count table found", file = sys.stderr)
except:
    print("Couldn't find count table", file = sys.stderr)
    sys.exit(1)

seqabund={}

samples = count.readline()
samples = samples.strip().split('\t')[2:] #Lista de las muestras 

x=0
print('Reading count table...' , file = sys.stderr)
for line in count:
    x=x+1
    if x%10000 == 0:
        print(x, file = sys.stderr)
    seq = line.split('\t')[0]
    seq = '>' + seq
    abund = map(int, line.strip().split('\t')[2:])
    seqabund.update({seq: abund}) #Diccionario con secuencias y las abundancias en cada muestra ordenadas

fastadict=open('fastadict', 'w')
seqfasta={}
x=0
print('Reading fasta file...')
for line in fasta:
    x=x+1
    if x%10000 == 0:
        print(x, file= sys.stderr)
    if line.startswith('>'):
        seq=line.strip()
    else:
        fasta=line.strip()
    seqfasta.update({seq: fasta})

for index, sample in enumerate(samples):
    f = open(sample, 'w')
    print('Generating file ' + sample, file= sys.stderr)
    for seqname, abunds in seqabund.items():
        abund=abunds[index]
        for i in range(abund):
            print(seqname, file=f)
            print(seqfasta[seqname], file=f)


 
 
 
 
 
 
 
 