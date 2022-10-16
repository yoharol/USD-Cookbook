from pxr import Usd, UsdGeom
from os import path

dir_path = path.join(path.dirname(path.abspath(__file__)), 'outputs')
filepath = path.join(dir_path, 'cube_rotate_animation.usda')

stage = Usd.Stage.CreateNew(filepath)
# initialize metadata for animation
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)

cubeXformGeom = UsdGeom.Xform.Define(stage, '/base')
subXformGeom = UsdGeom.Xform.Define(stage, '/base/cube1')
cubeGeom = UsdGeom.Cube.Define(stage, '/base/cube1/mesh')
UsdGeom.XformCommonAPI(cubeGeom).SetScale((0.3, 0.3, 0.3))
UsdGeom.XformCommonAPI(cubeGeom).SetTranslate((1, 0, 0))

spin2 = cubeGeom.AddRotateXOp(opSuffix='spin')
spin2.Set(time=1, value=0)
spin2.Set(time=192, value=1440)
#tilt = cubeXformGeom.AddRotateXOp(opSuffix='tilt')
#tilt.Set(value=12)

spin = subXformGeom.AddRotateZOp(opSuffix='spin')
spin.Set(time=1, value=0)
spin.Set(time=192, value=1440)

stage.Save()