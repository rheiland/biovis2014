import sys
from vtk import *
#  python showOBJ.py average_lh_pial

print 'len(sys.argv) =',len(sys.argv)
if len(sys.argv) < 2:
  print 'Usage: ' + sys.argv[0] + ' filename (without suffix)'
  print " e.g.  python showOBJ.py average_lh_pial"
  sys.exit(1)
fname = sys.argv[1]

ren1 = vtkRenderer()
renWin = vtkRenderWindow()
renWin.AddRenderer(ren1)
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
reader = vtkOBJReader()
reader.SetFileName(fname + '.obj')
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
actor = vtkActor()
actor.SetMapper(mapper)
ren1.AddActor(actor)
renWin.Render()
iren.Initialize()
iren.Start()
