from pxr import Usd, UsdGeom
from math import sin, pi
from os import path
import numpy as np

asset_dir = path.join(path.dirname(__file__), 'outputs')

stage = Usd.Stage.CreateNew(path.join(asset_dir, 'bunny_animation.usda'))
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(180)
stage.SetTimeCodesPerSecond(60)

rootXform = UsdGeom.Xform.Define(stage, '/root')
bunny_animation = UsdGeom.Mesh.Define(stage, '/root/bunny_animation')

bunny_animation.GetPrim().GetReferences().AddReference(
    assetPath='./low_poly_bunny.usda', primPath='/root/bunny')

bunnyVerticesAttr = bunny_animation.GetPointsAttr()
vertices = np.array(bunnyVerticesAttr.Get(), dtype=np.float32)
vertices_frame = np.zeros_like(vertices)

for frames in range(1, 181):
  for i in range(vertices.shape[0]):
    vertices_frame[i] = vertices[i]
    vertices_frame[i, 1] += 0.05 * sin(vertices[i, 0] * 20.0 + 2 * pi *
                                       (frames / 180))
  bunnyVerticesAttr.Set(vertices_frame, frames)

stage.GetRootLayer().Save()
stage.GetRootLayer().Export(path.join(asset_dir, 'bunny_animation.usdc'))