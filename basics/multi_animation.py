from pxr import Usd, UsdGeom
from os import path

dir_path = path.join(path.dirname(path.abspath(__file__)), 'outputs')
filepath = path.join(dir_path, 'multi_cube_animation.usda')

stage = Usd.Stage.CreateNew(filepath)

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(240)
stage.SetTimeCodesPerSecond(60)

baseXformGeom = UsdGeom.Xform.Define(stage, '/base')
cubeGeom = UsdGeom.Cube.Define(stage, '/base_cube')
#cubePrim = cubeGeom.GetPrim()
cubeGeom.GetVisibilityAttr().Set(UsdGeom.Tokens.invisible)

left = UsdGeom.Xform.Define(stage, '/base/left')
middle = UsdGeom.Xform.Define(stage, '/base/middle')
right = UsdGeom.Xform.Define(stage, '/base/right')

stage.GetRootLayer().Save()
