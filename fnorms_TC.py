# Calculate the Forbenius norm of the difference between two networks/matrices:
#    F(test_network - contest_subject_network)

import glob
import numpy as np
import math
#from operator import itemgetter

#fnormList = {}
#fnormDict = {}  # a Python dictionary consists of (key, value) pairs
#aliasDict = {}  # a Python dictionary consists of (key, value) pairs
tNum = 0
#contestDir = '/Users/heiland/Documents/Heiland/BioVis14/contest_subject_networks/'
contestDir = '../contest_subject_networks/'

threshValue = input('Enter a threshold value [-1,1]: ')
print 'threshValue = ',threshValue

for testFile in glob.glob('*adjacency_matrix_pcc.txt'):    # for each matrix in this directory
  tNum += 1
  print
  tName = 'T' + str(tNum)
#  print '-------------------------'
#  print tName + ': ',
  try:
    T = np.genfromtxt(testFile, delimiter='\t')  # T.shape = (167, 167)
  except:
    print "Error opening " + testFile
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
  for contestFile in glob.glob(contestDir + '*adjacency_matrix_pcc.txt'):
    cNum += 1
    cName = 'C' + str(cNum)
    try:
      C = np.genfromtxt(contestFile, delimiter='\t')  # C.shape = (167, 167)
    except:
      print "Error opening " + testFile
#    print 'C=',C
#    mtx2 = numpy.asarray(mtx)
    cutoff = C < threshValue
    C[cutoff] = threshValue
#    print 'after threshold: C=',C

    T_minus_C = np.subtract(T,C)
    fnorm = np.linalg.norm(T_minus_C)
    fnorm = math.ceil(fnorm*100)/100.   # 2 decimal digits
#    print '%.2f,' % fnorm,
    if fnorm < minFnorm:  minFnorm = fnorm
#    fnormList.append(fnorm)

    idx = contestFile.find("_adjacency")
    mtxName = contestFile[idx-8:idx]
    nameList.append(mtxName)
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
  print tName + ':',
#  print aliasList
  for c in aliasList: print c,
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
