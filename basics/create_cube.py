from pxr import Usd, UsdGeom
import os

output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           "outputs")
stage = Usd.Stage.CreateNew(os.path.join(output_path, 'cube.usda'))

xformGeom = UsdGeom.Xform.Define(stage, '/basic')
cubeGeom = UsdGeom.Cube.Define(stage, '/basic/cube')
cubePrim = cubeGeom.GetPrim()
print(cubePrim.GetPropertyNames())

# cubeXformable = UsdGeom.Xformable(cubeGeom)
UsdGeom.XformCommonAPI(xformGeom).SetTranslate((1.0, 0.0, 1.0))
UsdGeom.XformCommonAPI(cubePrim).SetScale((0.5, 0.5, 0.5))

print(stage.GetRootLayer().ExportToString())

for prim_iter in stage.Traverse():
  print(prim_iter.GetPath())

stage.GetRootLayer().Save()
