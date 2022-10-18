from pxr import Usd, UsdGeom
from os import path
import numpy as np
from math import sin, pi

asset_dir = path.join(path.dirname(__file__), 'outputs')

stage = Usd.Stage.Open(path.join(asset_dir, 'pole_flag', 'pole_flag.usda'))

stage.SetStartTimeCode(1)
stage.SetEndTimeCode(30)
stage.SetTimeCodesPerSecond(30)

for prim_iter in stage.Traverse():
  print(prim_iter.GetPath())

flagMesh = UsdGeom.Mesh(stage.GetPrimAtPath('/scene/Meshes/flag/mesh'))

flagVerticesAttr = flagMesh.GetPointsAttr()
vertices = np.array(flagVerticesAttr.Get(), dtype=np.float32)
vertices_frame = np.zeros_like(vertices)

for frames in range(1, 30):
  for i in range(vertices.shape[0]):
    vertices_frame[i] = vertices[i]
    vertices_frame[i, 1] += 0.3 * sin(vertices[i, 0] * 10.0 + 2 * pi *
                                      (frames / 30))
  flagVerticesAttr.Set(value=vertices_frame, time=frames)

stage.GetRootLayer().Export(
    path.join(asset_dir, 'pole_flag', 'pole_flag_animation.usda'))
stage.GetRootLayer().Export(
    path.join(asset_dir, 'pole_flag', 'pole_flag_animation.usdc'))