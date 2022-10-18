from pxr import Usd, UsdGeom
from os import path

dir_path = path.join(path.dirname(path.abspath(__file__)), 'outputs')
filepath = path.join(dir_path, 'cube_animation.usda')

stage = Usd.Stage.CreateNew(filepath)
# initialize metadata for animation
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)
stage.SetTimeCodesPerSecond(60)

cubeXformGeom = UsdGeom.Xform.Define(stage, '/base')
cubeGeom = UsdGeom.Cube.Define(stage, '/base/cube1')
UsdGeom.XformCommonAPI(cubeGeom).SetScale((0.3, 0.3, 0.3), time=1)
UsdGeom.XformCommonAPI(cubeGeom).SetScale((0.7, 0.7, 0.7), time=192)
UsdGeom.XformCommonAPI(cubeGeom).SetTranslate((0, 0, 0), time=1)
UsdGeom.XformCommonAPI(cubeGeom).SetTranslate((1.5, 0, 0), time=192)

stage.Save()