"""
window_heterozygosity.py

Script takes output from Daren's calcHet script and determines proportion of heterozygosity within a given window size. 

usage: python window_quantify_repeats.py <windowfile.txt> <het.txt> <out.txt>
"""

import sys
from decimal import * 

out = open(sys.argv[3], 'w')

#read in window file and make list of entries
windows = []

for line in open(sys.argv[1], 'r'):
	windows.append(line)

#read in tab-delimited file of per-site heterozygosity and make list of entries
hetero = []

for line in open(sys.argv[2], 'r'):
	chrom = line.split('\t')[0]
	pos = line.split('\t')[1]
	het = line.split('\t')[7]

	hetero.append(chrom+'_'+pos+'_'+het)

#iterate through windows, find all sites within window, and calculate proportion of heterozygosity within window
for window in windows:
	total = 0
	size = int(window.split()[2]) - int(window.split()[1])
	
	matches = [h for h in hetero if h.split('_')[0] == window.split()[0] and int(h.split('_')[1]) > int(window.split()[1]) and int(h.split('_')[1]) < int(window.split()[2])]
	for m in matches:
		het = m.split('_')[2]
		
		total = total + float(het)
	
	getcontext().prec = 11
	heterozygosity = Decimal(total)/Decimal(size)
	out.write(window.split()[0]+'\t'+window.split()[1]+'\t'+window.split()[2]+'\t'+str(heterozygosity)+'\n')
