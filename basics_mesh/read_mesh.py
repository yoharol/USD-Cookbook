from pxr import Usd, UsdGeom
from os import path
import numpy as np
from warp import render

asset_dir = path.join(path.dirname(__file__), 'outputs')

stage = Usd.Stage.Open(path.join(asset_dir, 'bunny.usda'))

for prim_iter in stage.Traverse():
  print(prim_iter.GetPath())

bunnyPrim = stage.GetPrimAtPath('/root/bunny')
bunnyMesh = UsdGeom.Mesh(bunnyPrim)

print(bunnyPrim.GetPropertyNames())


