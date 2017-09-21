import bpy
import math
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
r = 5
for i in range(1,360,5):
    g = math.pi/180*i
    y = math.sin(g)*r
    x = math.cos(g)*r
    bpy.ops.mesh.primitive_uv_sphere_add(segments = 7, ring_count=5, size=1, location=(0, y,x))


