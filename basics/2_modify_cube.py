from pxr import Usd, UsdGeom
import os

working_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'outputs')
stage = Usd.Stage.Open(os.path.join(working_dir, 'cube.usda'))

# Get UsdPrim obecjt from stage
xformPrim = stage.GetPrimAtPath('/basic')
cubePrim = stage.GetPrimAtPath('/basic/cube')

# print all attributes you can get form UsdPrim object
print("Xform prims:", xformPrim.GetPropertyNames())
print("Cube prims:", cubePrim.GetPropertyNames())

print("==================CubePrim Attributes====================")
for attr_name in cubePrim.GetPropertyNames():
  nxtAttr = cubePrim.GetAttribute(attr_name)
  print(f"{attr_name}: {nxtAttr.Get()}\t\t({nxtAttr.GetTypeName()})")

# edit attributes of UsdPrim
sizeAttr = cubePrim.GetAttribute('size')
sizeAttr.Set(1.0)
extentAttr = cubePrim.GetAttribute('extent')
extentAttr.Set([(-0.5, -0.5, -0.5), (0.5, 0.5, 0.5)])

# Get UsdGeom.Cube object from UsdPrim object
cubeGeom = UsdGeom.Cube(cubePrim)
# edit attributes of UsdGeom
print("==================CubeGeom Attributes====================")
print(list(filter(lambda x: 'Attr' in x, dir(cubeGeom))))

color = cubeGeom.GetDisplayColorAttr()
color.Set([(0, 1, 1)])
# cubeGeom.GetXformOpOrderAttr().Set([])

# edit Xformable APIs of an object
UsdGeom.XformCommonAPI(xformPrim).SetTranslate((1, 0, 0))

stage.SetDefaultPrim(xformPrim)

stage.GetRootLayer().Export(os.path.join(working_dir, 'cube_modified.usda'))
