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
UsdGeom.XformCommonAPI(cubeGeom).SetScale((0.5, 0.5, 0.5))
cubePrim = cubeGeom.GetPrim()
cubeGeom.MakeInvisible()
#cubeGeom.GetVisibilityAttr().Set(UsdGeom.Tokens.invisible)

left = UsdGeom.Xform.Define(stage, '/base/left')
left_cube = UsdGeom.Cube.Define(stage, '/base/left/cube')
left_cube.GetPrim().GetReferences().AddReference(assetPath='',
                                                 primPath='/base_cube')
left_cube.MakeVisible()
#left_cube.SetXformOpOrder([])
UsdGeom.XformCommonAPI(left_cube).SetTranslate((1, 0, 0))
left_spin = left.AddRotateZOp(opSuffix='spin')
left_spin.Set(time=1, value=0)
left_spin.Set(time=240, value=1440)

middle = UsdGeom.Xform.Define(stage, '/base/middle')
middle_cube = UsdGeom.Cube.Define(stage, '/base/middle/cube')
middle_cube.GetPrim().GetReferences().AddReference(assetPath='',
                                                   primPath='/base_cube')
middle_cube.MakeVisible()
#middle_cube.SetXformOpOrder([])
UsdGeom.XformCommonAPI(middle_cube).SetTranslate((3, 0, 0))
middle_spin = middle.AddRotateYOp(opSuffix='spin')
middle_spin.Set(time=1, value=0)
middle_spin.Set(time=240, value=-720)

right = UsdGeom.Xform.Define(stage, '/base/right')
right_cube = UsdGeom.Cube.Define(stage, '/base/right/cube')
right_cube.GetPrim().GetReferences().AddReference(assetPath='',
                                                  primPath='/base_cube')
right_cube.MakeVisible()
#right_cube.SetXformOpOrder([])
UsdGeom.XformCommonAPI(right_cube).SetTranslate((5, 0, 0))
right_spin = right.AddRotateZOp(opSuffix='spin')
right_spin.Set(time=1, value=0)
right_spin.Set(time=240, value=-360)

animation2 = UsdGeom.Xform.Define(stage, '/base2')
animation2.GetPrim().GetReferences().AddReference(assetPath='',
                                                  primPath='/base')
UsdGeom.XformCommonAPI(animation2).SetTranslate((0, 0, 6))
UsdGeom.XformCommonAPI(animation2).SetScale((-1, -1, 1))

stage.GetRootLayer().Save()
