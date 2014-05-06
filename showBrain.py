from vtk import *
import glob

ren1 = vtkRenderer()
renWin = vtkRenderWindow()
renWin.AddRenderer(ren1)
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


fnames = ['average_lh_inflated', 'average_rh_inflated']
fnames = ['average_lh_pial', 'average_rh_pial']
fnames = ['single_subject_lh_pial', 'single_subject_rh_pial']

reader = vtkPLYReader()
reader.SetFileName(fnames[0]+'.ply')
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
actor = vtkActor()
actor.SetMapper(mapper)
ren1.AddActor(actor)

reader2 = vtkPLYReader()
reader2.SetFileName(fnames[1]+'.ply')
mapper2 = vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort())
actor2 = vtkActor()
actor2.SetMapper(mapper2)
ren1.AddActor(actor2)

renWin.Render()

w2i = vtkWindowToImageFilter()
w2i.SetInput(renWin)
w2i.Update()

writer = vtkPNGWriter()
writer.SetInputConnection(w2i.GetOutputPort())
print '--> fullBrain.png'
writer.SetFileName("fullBrain.png")
writer.Write()
iren.Initialize()
iren.Start()
