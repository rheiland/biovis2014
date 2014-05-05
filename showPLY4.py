import vtk
import sys,string
#
#  Usage: python renderPLY4.py 1X4I9DF0 average_lh_inflated
#
#  old:
# python renderPLY4.py U050E1IO_adjacency_matrix_pcc.txt average_lh_inflated 25 2 -90 -70

idx=1
#nw_fname = sys.argv[idx]
outname = sys.argv[idx]
idx += 1
fname = sys.argv[idx]
#idx += 1
#xp = int(sys.argv[idx])
#idx += 1
#yp = int(sys.argv[idx])
#print 'xp,yp=',xp,yp
#idx += 1
#rotY = float(sys.argv[idx])
rotY = -90
#idx += 1
#rotZ = float(sys.argv[idx])
rotZ = -70

#outname = nw_fname[0:8]

renWin = vtk.vtkRenderWindow()
renWin.SetSize(512,512)

xmins = [0,.5,0,.5]
xmaxs = [0.5,1,0.5,1]
#ymins = [0,0,.5,.5]
ymins = [0.5,0,0,.5]

#ymaxs = [0.5,0.5,1,1]
ymaxs = [1,0.5,0.5,1]
i=0
ren1 = vtk.vtkRenderer()
ren1.SetViewport(xmins[i],ymins[i],xmaxs[i],ymaxs[i])
renWin.AddRenderer(ren1)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

reader = vtk.vtkPLYReader()
reader.SetFileName(fname + '.ply')

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
#actor.RotateY(rot);
#actor.RotateZ(45);

xform = vtk.vtkTransform()
xform.PostMultiply()
sf = 5.2
xform.Scale(sf,sf,sf)
#xform.Translate(10.0, 0.0, 0.0)
xform.RotateY(rotY)
xform.RotateZ(rotZ)
actor.SetUserTransform(xform)

ren1.AddActor(actor)

#textActor = vtk.vtkTextActor()
#textActor.GetTextProperty().SetFontSize ( 18 )
#textActor.SetPosition2( xp, yp )
#textActor.SetDisplayPosition( xp, yp )
#textActor.SetInput(outname)
#textActor.GetTextProperty().SetColor( 1.0, 1.0, 1.0 )
#ren1.AddActor2D( textActor )


zf=1.5
ren1.ResetCamera()  # must do this, otherwise get bad clipping effects
ren1.GetActiveCamera().Zoom(zf)

renWin.Render()

#---------------------
ren2 = vtk.vtkRenderer()
renWin.AddRenderer(ren2)
i=1
ren2.SetViewport(xmins[i],ymins[i],xmaxs[i],ymaxs[i])

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper)
#actor.RotateY(rot);
#actor.RotateZ(45);

xform2 = vtk.vtkTransform()
xform2.PostMultiply()
sf = 5.2
xform2.Scale(sf,sf,sf)
#xform.Translate(10.0, 0.0, 0.0)
xform2.RotateY(rotY)
xform2.RotateZ(rotZ)
actor2.SetUserTransform(xform2)
#xform.Identity()
# Rotate 180 degs to render the Medial (inside) view (vs. Lateral view above)
xform2.RotateY(180)
#xform.RotateZ(-rotZ)
xform2.Update()
actor2.SetUserTransform(xform2)
ren2.AddActor(actor2)

ren2.ResetCamera()  # must do this, otherwise get bad clipping effects
#ren2.GetActiveCamera().Zoom(zf)
ren2.GetActiveCamera().Zoom(zf)
renWin.Render()

#=======================================================
#fname = 'average_rh_inflated'
iunder = string.find(fname,'_')
if fname[iunder+1] == 'l':
  fname2 = string.replace(fname,'_lh_','_rh_')
#  fname.substitute(who='_lh_', what='_rh_')
else:
#  fname2 = fname[iunder:iunder+3] = '_lh_'
#  fname.substitute(who='_rh_', what='_lh_')
  fname2 = string.replace(fname,'_rh_','_lh_')
print 'fname2=',fname2
ren3 = vtk.vtkRenderer()
renWin.AddRenderer(ren3)
i=2
ren3.SetViewport(xmins[i],ymins[i],xmaxs[i],ymaxs[i])

reader3 = vtk.vtkPLYReader()
reader3.SetFileName(fname2 + '.ply')

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputConnection(reader3.GetOutputPort())

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
#actor.RotateY(rot);
#actor.RotateZ(45);

xform3 = vtk.vtkTransform()
xform3.PostMultiply()
sf = 5.2
xform3.Scale(sf,sf,sf)
#xform.Translate(10.0, 0.0, 0.0)
xform3.RotateY(rotY)
xform3.RotateZ(rotZ)
actor3.SetUserTransform(xform3)

ren3.AddActor(actor3)

ren3.ResetCamera()  # must do this, otherwise get bad clipping effects
ren3.GetActiveCamera().Zoom(zf)
renWin.Render()

#---------------------
ren4 = vtk.vtkRenderer()
renWin.AddRenderer(ren4)
i=3
ren4.SetViewport(xmins[i],ymins[i],xmaxs[i],ymaxs[i])

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper3)

xform4 = vtk.vtkTransform()
xform4.PostMultiply()
sf = 5.2
xform4.Scale(sf,sf,sf)
#xform.Translate(10.0, 0.0, 0.0)
xform4.RotateY(rotY)
xform4.RotateZ(rotZ)
actor4.SetUserTransform(xform3)
#xform.Identity()
# Rotate 180 degs to render the Medial (inside) view (vs. Lateral view above)
xform4.RotateY(180)
#xform.RotateZ(-rotZ)
xform4.Update()
actor4.SetUserTransform(xform4)

ren4.AddActor(actor4)

#textActor = vtk.vtkTextActor()
#textActor.GetTextProperty().SetFontSize ( 18 )
#textActor.SetPosition2( xp, yp )
#textActor.SetDisplayPosition( xp, yp )
#textActor.SetInput(outname)
#textActor.GetTextProperty().SetColor( 1.0, 1.0, 1.0 )
#ren4.AddActor2D( textActor )

ren4.ResetCamera()  # must do this, otherwise get bad clipping effects
ren4.GetActiveCamera().Zoom(zf)
renWin.Render()


# finally, write png
w2i = vtk.vtkWindowToImageFilter()
w2i.SetInput(renWin)
w2i.Update()

writer2 = vtk.vtkPNGWriter()
writer2.SetInputConnection(w2i.GetOutputPort())
outname = outname + '-4.png'
print 'outname = ',outname
writer2.SetFileName(outname)
writer2.Write()

#iren.Initialize()
#iren.Start()
