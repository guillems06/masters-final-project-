from __future__ import print_function
import sys

if len(sys.argv) != 2:
    print('Please, input the shared file', file=sys.stderr)
else:
    pass

try:
    shared=open(sys.argv[1])
except:
    print('Shared file not found', file=sys.stderr)
xx=0
firstline = shared.readline()
firstline = firstline.strip().split('\t')[3:]
print('\t' + '\t'.join(firstline))
for line in shared:
    print('Reading...', file=sys.stderr)
    a=line.strip().split('\t')
    del a[2]
    del a[0]
    print('\t'.join(a))
            

sys.exit(0)
    