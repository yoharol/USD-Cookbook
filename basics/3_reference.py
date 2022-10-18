from pxr import Usd, UsdGeom
from os import path

working_dir = path.join(path.dirname(path.realpath(__file__)), 'outputs')
stage = Usd.Stage.CreateNew(path.join(working_dir, 'cube_reference.usda'))

baseXform = UsdGeom.Xform.Define(stage, '/root')
cube1 = UsdGeom.Cube.Define(stage, '/root/cube1')

UsdGeom.XformCommonAPI(cube1).SetScale((0.5, 0.5, 0.5))
UsdGeom.XformCommonAPI(cube1).SetTranslate((1.0, 0.0, 0.0))
cube1.GetDisplayColorAttr().Set([(0.8, 0.0, 0.0)])

cube2 = UsdGeom.Cube.Define(stage, '/root/cube2')
cube2.GetPrim().GetReferences().AddReference(assetPath='',
                                             primPath='/root/cube1')
UsdGeom.XformCommonAPI(cube2).SetTranslate((3.0, 0.0, 1.0))
cube2.GetDisplayColorAttr().Set([(0.0, 0.8, 0.0)])

cube2 = UsdGeom.Cube.Define(stage, '/root/cube3')
cube2.GetPrim().GetReferences().AddReference(assetPath='./cube.usda',
                                             primPath='/basic/cube')
cube2.GetDisplayColorAttr().Set([(0.0, 0.0, 0.8)])

stage.GetRootLayer().Save()