import sympy.geometry as geo

A = geo.Point(0, 0)
B = geo.Point(14, 0)
C = geo.Point(5, 12)
tri = geo.Triangle(A, B, C)
print('内心 = ', tri.incenter)
print('半径 = ', tri.inradius)