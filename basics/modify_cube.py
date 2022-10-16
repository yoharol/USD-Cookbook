from pxr import Usd, UsdGeom
import os

working_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'outputs')
stage = Usd.Stage.Open(os.path.join(working_dir, 'cube.usda'))

# Get UsdPrim obecjt from stage
xformPrim = stage.GetPrimAtPath('/basic')
cubePrim = stage.GetPrimAtPath('/basic/cube')

print("Xform prims:", xformPrim.GetPropertyNames())
print("Cube prims:", cubePrim.GetPropertyNames())

for attr_name in cubePrim.GetPropertyNames():
  nxtAttr = cubePrim.GetAttribute(attr_name)
  print(f"{attr_name}: {nxtAttr.Get()}\t\t({nxtAttr.GetTypeName()})")

sizeAttr = cubePrim.GetAttribute('size')
sizeAttr.Set(1.0)
extentAttr = cubePrim.GetAttribute('extent')
extentAttr.Set([(-0.5, -0.5, -0.5), (0.5, 0.5, 0.5)])

# Get UsdGeom.Cube object from UsdPrim object, which is inherent from UsdGeomGprim
cubeGeom = UsdGeom.Cube(cubePrim)
color = cubeGeom.GetDisplayColorAttr()
color.Set([(0, 1, 1)])

UsdGeom.XformCommonAPI(xformPrim).SetTranslate((1, 1, 1))

stage.SetDefaultPrim(xformPrim)

#stage.GetRootLayer().Save()
stage.GetRootLayer().Export(os.path.join(working_dir, 'cube_modified.usda'))
