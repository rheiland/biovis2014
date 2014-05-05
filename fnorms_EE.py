# Calculate the Forbenius norm of a matrix.

import glob
import numpy as np
import math
#from operator import itemgetter

#fnormList = {}
#fnormDict = {}  # a Python dictionary consists of (key, value) pairs
#aliasDict = {}  # a Python dictionary consists of (key, value) pairs
tNum = 0
fullDir = '/Users/heiland/Documents/Heiland/BioVis14/example_networks/'

threshValue = input('Enter a threshold value [-1,1]: ')
print 'threshValue = ',threshValue

# 5 subjects, 4 measures each
#  example1_1_adjacency_matrix_pcc.txt --> example5_4_adjacency_matrix_pcc.txt
#for nw1File in glob.glob('example1_*adjacency_matrix_pcc.txt'):    # for each matrix in this directory
for nw1File in glob.glob('*adjacency_matrix_pcc.txt'):    # for each matrix in this directory
  tNum += 1
  print
  idx = nw1File.find("_adjacency")
  mtx1Name = nw1File[idx-3:idx]
#  print mtxName + ':',
  tName = 'T' + str(tNum)
#  print '-------------------------'
#  print tName + ': ',
  T = np.genfromtxt(nw1File, delimiter='\t')  # T.shape = (167, 167)
#  print 'T=',T
#  mtx2 = numpy.asarray(mtx)
  cutoff = T < threshValue
  T[cutoff] = threshValue
#  print 'after threshold: T=',T

  nameList = []
  aliasList = []
  fnormList = []

  cNum = 0
  minFnorm = 999.0
#  for nw2File in glob.glob('example1_*adjacency_matrix_pcc.txt'):
  for nw2File in glob.glob('*adjacency_matrix_pcc.txt'):
    if nw1File == nw2File: 
      continue
    cNum += 1
    cName = 'C' + str(cNum)
    C = np.genfromtxt(nw2File, delimiter='\t')  # C.shape = (167, 167)
#    print 'C=',C
#    mtx2 = numpy.asarray(mtx)
    cutoff = C < threshValue
    C[cutoff] = threshValue
#    print 'after threshold: C=',C

    T_minus_C = np.subtract(T,C)
    fnorm = np.linalg.norm(T_minus_C)
#    fnorm = math.ceil(fnorm*100)/100.   # 2 decimal digits
    fnorm = math.ceil(fnorm*10)/10.   # 1 decimal digit
#    print '%.2f,' % fnorm,
    if fnorm < minFnorm:  minFnorm = fnorm
#    fnormList.append(fnorm)

    idx = nw2File.find("_adjacency")
    mtx2Name = nw2File[idx-3:idx]
    nameList.append(mtx2Name)
    aliasList.append('C' + str(cNum))
    fnormList.append(fnorm)
  # we know the matrix names are unique, therefore they become the keys of our dictionary
#  fnormDict[mtxName] = fnorm  
#  aliasDict[mtxName] = 
#  info = '%s %.3f' % (mtxName,fnorm)
#  info = '%s %.3f' % (mtxName,fnorm)
#  print info
#  print 'minFnorm= %.2f' % minFnorm
#  print '---- after sorting by fnorm, with threshold=',threshValue
  fnormList, nameList, aliasList = (list(x) for x in zip(*sorted(zip(fnormList, nameList, aliasList))))
#  print 'sorted fnormList=',fnormList
#  print nameList
#  print tName + ':',
  print mtx1Name + ':',
#  print aliasList
#  for c in aliasList: print c,
  for c in nameList: print c,
  print
  for v in fnormList: print v,

#  if tNum == 3: break
#  print fnormList
#print 'fnormDict=',fnormDict
# created a list of the fnorm values, sorted least to greatest
#sortedList = numpy.sort(fnormDict.values())  
#print 'sortedList=',sortedList
#print 'aliasDict=',aliasDict
#newlist = sorted(fnormDict, key=itemgetter('name')) 
#print '------ unsorted lists:'
#print fnormList
#print nameList
#print aliasList

#for name in nameList:
  
#print '------ after sorting by fnorm, with threshold=',threshValue
#fnormList, nameList, aliasList = (list(x) for x in zip(*sorted(zip(fnormList, nameList, aliasList))))
#print fnormList
#print nameList
#print aliasList
