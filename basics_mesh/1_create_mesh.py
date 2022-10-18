from pxr import Usd, UsdGeom
import numpy as np
from os import path

asset_dir = path.join(path.dirname(__file__), 'outputs')

stage = Usd.Stage.CreateNew(path.join(asset_dir, 'low_poly_bunny.usda'))

with open(path.join(asset_dir, 'low_poly_bunny.npy'), 'rb') as f:
  vertices_pos = np.load(f)  # position of vertices
  tet_ids = np.load(f)  # composition of tetrahedrals
  edge_ids = np.load(f)  # composition of edges
  surface_ids = np.load(f)  # composition of surface faces

for npArray in [vertices_pos, tet_ids, edge_ids, surface_ids]:
  print(npArray.shape, npArray.dtype)

num_particles = vertices_pos.shape[0]
num_tets = tet_ids.shape[0]
num_edges = edge_ids.shape[0]
num_surfaces = surface_ids.shape[0]

rootXform = UsdGeom.Xform.Define(stage, '/root')
bunnyGeom = UsdGeom.Mesh.Define(stage, '/root/bunny')

bunnyGeom.GetPointsAttr().Set(vertices_pos)
bunnyGeom.GetFaceVertexIndicesAttr().Set(surface_ids)
bunnyGeom.GetFaceVertexCountsAttr().Set(num_surfaces * [3])
bunnyGeom.GetSubdivisionSchemeAttr().Set('none')

stage.GetRootLayer().Save()