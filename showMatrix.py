import numpy as np
import matplotlib.pyplot as plt

fname = '1X4I9DF0_adjacency_matrix_pcc.txt'
A = np.genfromtxt(fname, delimiter='\t')
plt.imshow(A, interpolation='nearest')
plt.colorbar(orientation='vertical')
plt.title(fname[0:8])
plt.show()
