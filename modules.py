import numpy as np
#from pylab import *
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm
import bct

my_cmap = cm.get_cmap('rainbow')

#mc=[['255 0 0'],['0 255 0'],['0 0 255'],['255 255 0'],['0 255 255']]

threshVal=0.3
threshVal=0.0
threshVal=input("Enter threshold: ")

#testDir = '/Users/heiland/Documents/Heiland/BioVis14/contest_subject_networks/'
#fname = 'U050E1IO_adjacency_matrix_pcc.txt'
fname = '1X4I9DF0_adjacency_matrix_pcc.txt'
#d = np.genfromtxt(testDir + fname, delimiter='\t')
try:
  A = np.genfromtxt(fname, delimiter='\t')
except:
  print "Error opening " + fname

bct.threshold_absolute(A,threshVal)

# Calculate the network's modularity
[Ci,Q]=bct.modularity_und(A)

print Ci
for i in range(len(Ci)):
  for j in range(i+1,len(Ci)):
#    print i,j
    if Ci[i] > Ci[j]:
      temp = Ci[i]
      Ci[i] = Ci[j]
      Ci[j] = temp
      print str(i) + ' <-> ' + str(j)
      A[[i,j]] = A[[j,i]]  # swap rows
      A[:,[i,j]] = A[:,[j,i]]  # swap cols
print Ci

#Ci=array([1, 1, 3, 3, 1, 3, 3, 3, 1, 3, 3, 1, 1, 1, 1, 1, 3, 3, 4, 3, 1, 3, 3, ...

#A2 = np.empty((167,167))
#A2 = A

# Mask all diagonal entries as "bad" and color black
#A = np.ma.masked_where(abs(A) < 0.0001, A)
#A_masked = np.ma.masked_where(A2 == 0.0, A2)
#cmap = plt.cm.OrRd
#cmap.set_bad(color='black')

# to color all zero elements black
#A_masked = np.ma.masked_where(A == 0.0, A)
#my_cmap.set_bad(color='black')

#plt.imshow(A_masked, interpolation='nearest', cmap=my_cmap)
plt.imshow(A, interpolation='nearest')
plt.colorbar(orientation='vertical')
plt.title(fname[0:8] + ', # modules='+str(Ci.max()))

plt.show()
