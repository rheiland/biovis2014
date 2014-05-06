# Display just the first 10x10 regions of a connection matrix, labeled with region ids.
# Usage:  python showMatrix10.py 1X4I9DF0_adjacency_matrix_pcc.txt

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import networkx as nx


#fname = sys.argv[1]
fname = '1X4I9DF0_adjacency_matrix_pcc.txt'

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
A = A[:10,:10]
threshold = input ('Enter threshold: ')
cutoff = A < threshold
A[cutoff] = 0



G = nx.from_numpy_matrix(A)
print 'nodes= ',G.nodes()
print 'len(edges)= ',len(G.edges())

#nx.draw(G)
#nx.draw_spectral(G)

colors = range(len(G.edges()))
print 'type(colors)=',type(colors)
print colors
idx=0
for edge in G.edges():
  colors[idx] = A[edge[0],edge[1]]
  idx += 1
#nx.draw_networkx(G,pos=nx.spring_layout(G),node_size=30.0,with_labels=False)
#nx.draw_networkx(G,pos=nx.spring_layout(G),edge_color=colors,edge_cmap=plt.cm.Blues,width=4)
nx.draw_networkx(G,pos=nx.spring_layout(G),edge_color=colors,edge_cmap=plt.cm.Reds,width=4)
plt.axis('off')
#nx.draw_networkx(G,pos=nx.spring_layout(G))
#nx.draw_circular(G)
#nx.draw_circular(G,with_labels=False,node_size=30.0)
#nx.draw_circular(G,with_labels=False)
#nx.draw_circular(G)
plt.savefig('showGraph10.png')
plt.show()
