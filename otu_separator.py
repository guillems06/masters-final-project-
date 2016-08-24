from __future__ import print_function
import os
import sys
import re

if len (sys.argv) != 4:
    print('Please, input a .list, a .fasta and a .count_table file', file=sys.stderr)
    sys.exit(1)
else:
    pass
try:
    otu.file=open(sys.argv[1], 'r')
    print('list file found', file=sys.stderr)
except:
    print("Couldn't find list file", file = sys.stderr)
    sys.exit(1)
try:
    fasta.file=open(sys.argv[2], 'r')
    print('fasta file found', file=sys.stderr)
except:
    print("Couldn't find fasta file", file = sys.stderr)
    sys.exit(1)
try:
    count.file=open(sys.argv[3], 'r')
    print('count file found', file=sys.stderr)
except:
    print("Couldn't find count file", file = sys.stderr)
    sys.exit(1)

for line in otu.file:
    if line.startswith("0.02"):
        