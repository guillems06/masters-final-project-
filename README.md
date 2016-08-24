# masters-final-project-
Python scripts used to complete my masters final project

makegroups2.py --> configured to open every files in a determined path, reading them and copying all fasta sequences to a single fasta file (with the name of the sequence and the sequence) and a group file (with the name of the sequence and the sample where it was found)

sharedr.py --> takes as input a .shared filed and generates a table which R can read:
'\t'		OTU1 	OTU2
Sample1	abund	abund
Sample2	abund	abund

samplecreator.py --> generates new samples files after processing sequences with Mothur. Takes as input a .fasta and a .count_table. 

otu_separator.py --> takes as input a .list file and makes a new file for each Mothur OTU.

oligotyping_runner --> runs every oligotyping command to obtain the analysis entropy.
