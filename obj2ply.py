import sys,string

#
# obj2ply.py - Convert a .obj formatted file to .ply format
#  - assumes all vertices are listed, then all faces
#  python obj2ply.py average_rh_pial
#  python obj2ply.py single_subject_rh_pial
#

argc=len(sys.argv)
print 'argc=',argc

if (argc < 2):
  print 'Usage: %s <rootfilename of .obj file>' % sys.argv[0]
  print '   e.g. average_lh_inflated'
  sys.exit()

root_fname = sys.argv[1]


#----------------------------
"""
Get RGB for various parcel IDs from here:
#http://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/AnatomicalROI/FreeSurferColorLUT
#No.   Label Name:                              R   G   B    A
11100  ctx_lh_Unknown                           0   0   0    0
11101  ctx_lh_G_and_S_frontomargin             23 220  60    0
"""

fp_roi =open('roi_cmap.txt', 'r')
# Create a dictionary mapping ID --> RGB
vc = {}  # vertex color dictionary
count = 0
for line in fp_roi:
  if line[0] != '#':
    e = line.split()
    vc[int(e[0])] = e[2] + ' ' + e[3] + ' '+ e[4]
#    if count < 5:
#      count += 1
#      print vc

# Lastly, append white/gray for the 0th index
vc[0] = '187 187 187'
vc[0] = '255 255 255'
print 'len(vc) = ',len(vc)

#-------------------------------
# 1st pass through the .obj file: count # of verts and faces (triangles)
in_fname = root_fname + '.obj'
fp = open(in_fname, 'r')
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
roi_fname = root_fname[:root_fname.find('h_')+2] + 'vertex_ROIids.txt'
fproi = open(roi_fname, 'r')

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

#  print line,
fpout.close()

print '--> ' + out_fname
