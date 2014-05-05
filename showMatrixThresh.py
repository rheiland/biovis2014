import numpy as np
import matplotlib.pyplot as plt

fname = '1X4I9DF0_adjacency_matrix_pcc.txt'
try:
  A = np.genfromtxt(fname, delimiter='\t')
except:
  print("Error opening " + fname)

threshold = input ('Enter threshold: ')
cutoff = A < threshold
A[cutoff] = 0

plt.imshow(A, interpolation='nearest')
plt.colorbar(orientation='vertical')
plt.title(fname[0:8])
plt.show()
