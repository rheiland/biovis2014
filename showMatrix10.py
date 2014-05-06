# Display just the first 10x10 regions of a connection matrix, labeled with region ids.
# Usage:  python showMatrix10.py 1X4I9DF0_adjacency_matrix_pcc.txt

import sys
import numpy as np
import matplotlib.pyplot as plt

fname = sys.argv[1]
#N = int(sys.argv[2])

# create a list of the first 10 brain region ids from roi_legend.txt
ids = ['ctx_lh_G_and_S_frontomargin',
'ctx_lh_G_and_S_occipital_inf',
'ctx_lh_G_and_S_paracentral',
'ctx_lh_G_and_S_subcentral',
'ctx_lh_G_and_S_transv_frontopol',
'ctx_lh_G_and_S_cingul-Ant',
'ctx_lh_G_and_S_cingul-Mid-Ant',
'ctx_lh_G_and_S_cingul-Mid-Post',
'ctx_lh_G_cingul-Post-dorsal',
'ctx_lh_G_cingul-Post-ventral']

#fname = '1X4I9DF0_adjacency_matrix_pcc.txt'
A = np.genfromtxt(fname, delimiter='\t')
#plt.imshow(A[:N,:N], interpolation='nearest')
plt.imshow(A[:10,:10], interpolation='nearest')
plt.colorbar(orientation='vertical')
plt.title(fname[0:8])
plt.xticks(range(len(ids)), ids, rotation=30, ha='right')
plt.yticks(range(len(ids)), ids)
plt.show()
