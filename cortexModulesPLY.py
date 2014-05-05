#
#  Generate a .ply file from a .obj, where vertices are colored according to
#  the module they belong to.
# 
#  e.g. 
#    python plot1_anatomy_modules.py average_rh_inflated U050E1IO_adjacency_matrix_pcc.txt 0.0
#    python plot1_anatomy_modules.py average_rh_inflated 1X4I9DF0_adjacency_matrix_pcc.txt 0.0
#
import sys
import numpy as np
import bct
#import os

argc=len(sys.argv)
print 'argc=',argc

if (argc < 2):
#  print 'Usage: %s <obj_rootname> <nw_fname> <threshold>' % sys.argv[0]
  print 'Usage: %s <obj_rootname> <threshold>' % sys.argv[0]
#  print '   e.g. average_lh_inflated  U050E1IO_adjacency_matrix_pcc.txt 0.0'
  print '   e.g. average_lh_inflated  0.0'
  sys.exit()

root_fname = sys.argv[1]
#nw_fname = sys.argv[2]
nw_fname = "1X4I9DF0_adjacency_matrix_pcc.txt"
threshold = float(sys.argv[2])
print 'threshold=',threshold

adjMtx = np.genfromtxt(nw_fname, delimiter='\t')

"""Rubinov,Sporns 2010:  all self-connections or negative connections
(such as functional anticorrelations) must currently be removed
from the networks prior to analysis"""

bct.threshold_absolute(adjMtx,threshold)

# NB! be sure to put before masking the matrix
[Ci,Q]=bct.modularity_und(adjMtx)

roi_legend = 'roi_legend.txt'
try:
  fp_roi =open(roi_legend, 'r')
except:
  print("Error opening " + roi_legend)

# Create a dictionary mapping ID --> RGB
vc = {}  # vertex color dictionary
count = 0
# colors (rgb) for modules (Q: what's the max # of modules we'll have??)
# rf. http://www.rapidtables.com/web/color/RGB_Color.htm
# Red,Green,Yellow,Blue,...
module_rgb_dict = {1:'255 0 0', 2: '0 255 0', 3: '255 255 0', 4: '0 0 255', 5: '255 0 255', 6: '51 255 255'}
count = 0
for line in fp_roi:
#  if line[0] != '#':
  elms = line.split()
  vc[int(elms[1])] = module_rgb_dict[Ci[count]]    # id -> 'r g b'
  count += 1

vc[0] = '255 255 255'   # vertex id not assoc'd with any parcel gets colored white

degs = bct.degrees_und(adjMtx)

#-------------------------------
# 1st pass through the .obj file: count # of verts and faces (triangles)
in_fname = '../anatomy/' + root_fname + '.obj'
try:
  fp = open(in_fname, 'r')
except:
  print("Error opening " + in_fname)

numv = 0
numf = 0
for line in fp:
  if line[0] == 'v':
    numv += 1
  elif line[0] == 'f':
    numf += 1
fp.close()
print 'numv,numf = ',numv,numf

#-------------------------------
# 2nd pass - generate .ply formatted file
fp = open(in_fname, 'r')
out_fname = root_fname + '.ply'

#roi_fname = 'average_lh_vertex_ROIids.txt'
roi_fname = '../anatomy/' + root_fname[:root_fname.find('h_')+2] + 'vertex_ROIids.txt'
print 'using ',roi_fname
try:
  fproi = open(roi_fname, 'r')
except:
  print("Error opening " + roi_fname)

fpout = open(out_fname, "w")
fpout.write("""ply
format ascii 1.0
comment PLY-formated file from .obj\n""")

s = "element vertex %d\n" % numv
fpout.write(s)
#element vertex 163842
fpout.write("""property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue\n""")

#element face 327680
s = "element face %d\n" % numf
fpout.write(s)
fpout.write("""property list uchar int vertex_indices
end_header\n""")

numv = 0
numf = 0
for line in fp:
  if line[0] == 'v':
    numv += 1
#    fpout.write(line[1:])
    s = line[1:].split()
    v1 = float(s[0])
    v2 = float(s[1])
    v3 = float(s[2])
    s = "%.4f %.4f %.4f " % (v1,v2,v3)
#    fpout.write(line[1:])
#    fpout.write(s)

    vid = fproi.readline()
    vid.split()
    s +=  vc[int(vid)] + '\n'
    fpout.write(s)

#    if numv > 10: break
  elif line[0] == 'f':
    numf += 1
    vi = line[1:].split()  # get vertex indices (of triangles)
#    fpout.write('3' + line[1:])   # NB! indices are 0-offset in PLY and 1-offset in OBJ
    s = "3 %d %d %d\n" % (int(vi[0])-1,int(vi[1])-1,int(vi[2])-1)
    fpout.write(s)   # NB! indices are 0-offset in PLY and 1-offset in OBJ

fpout.close()

print '--> ' + out_fname
