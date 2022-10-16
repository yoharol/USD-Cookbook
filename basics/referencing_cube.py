from pxr import Usd, UsdGeom
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')

refStage = Usd.Stage.CreateNew(os.path.join(path, "ref_cubes.usda"))

# Create an override prim and retun a UsdPrim object
refCube = refStage.OverridePrim('/refCube')
# cube.usda needs to have a default prim
refCube.GetReferences().AddReference('./cube.usda')

# Get UsdGeomXformable object from UsdPrim object
refXform = UsdGeom.Xformable(refCube)
refXform.SetXformOpOrder([])  # ignore all transform op

refCube2 = refStage.OverridePrim('/refCube2')
refCube2.GetReferences().AddReference('./cube.usda')

refCubeGeom = UsdGeom.Cube.Get(refStage, '/refCube2/cube')
refCubeGeom.GetDisplayColorAttr().Set([(1, 0, 0)])

refStage.GetRootLayer().Save()

print(refStage.ExportToString())