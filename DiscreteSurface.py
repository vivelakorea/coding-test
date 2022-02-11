class DiscreteSurface:

  def __init__(self):
    self.surfaces = {}

  def add_surface(self, elem_id, quadrangle_points):
    """
    Add one surface.
    Arguments
      elem_id : id of NAND part's element that have the surface
      quadrangle_points : 
        [(x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4)] 
        four nodes of the surface
    """
    self.surfaces[elem_id] = quadrangle_points[:] # avoid shallow copy
  
  def point_in_quadrangle(self, quadrangle_points, point):
    """
    Check if the 2d point is in 2d sqaure
    Arguments:
      quadrangle_points : [(x1,y1),(x2,y2), (x3,y3), (x4,y4)]
      point : (x,y)
    It doesn't mean that only xy plane can be used. 
    yz, zx plane can be used as well.
    """
    def _point_on_line(_p1, _p2, _point):
      # corner case: _point is _p1 or _p2
      if _p1 == _point or _p2 == _point:
        return True

      # corner case: slope of line is infinite
      if _p1[0] == _p2[0]:
        if _point[0] == _p1[0] and (_p1[1] - _point[1]) * (_point[1] - _p2[1]) > 0:
          return True
        else:
          return False
      
      if _p1[0] - _point[0] == 0: return False
      _slope1 = (_p1[1] - _point[1]) / (_p1[0] - _point[0])
      if _point[0] - _p2[0] == 0: return False
      _slope2 = (_point[1] - _p2[1]) / (_point[0] - _p2[0])

      if _slope1 == _slope2 and (_p1[0] - _point[0]) * (_point[0] - _p2[0]) > 0:
        return True
      
      return False

    areas = []

    for i in range(4):
      p1 = quadrangle_points[i%4]
      p2 = quadrangle_points[(i+1)%4]

      # point on edge
      if _point_on_line(p1, p2, point):
        return True
      
      # point not on edge
      area = ((p2[0]*point[1]-point[0]*p2[1])-(p2[0]*p1[1]-p1[0]*p2[1])+(point[0]*p1[1]-p1[0]*point[1]))/2
      areas.append(area)

    sign_set = set()
    for area in areas:
      if area < 0:
        sign_set.add(-1)
      elif area == 0:
        sign_set.add(0)
      else:
        sign_set.add(1)
    if len(sign_set) == 1:
      return True

    return False

  def find_x(self, y, z):
    """
    Let's express the discrete surfae as f(x,y,z) = 0.
    Then if the y and z values are fixed, there might be or not be
    x that satisfies the y and z values. If not, it returns None, and
    if there is(are), it returns smallest x.
    find_y and find_z are same but different only in order.
    """

    xs = []

    point = (y,z)

    for surface in self.surfaces.values():
      quadrangle_points = [
        (surface[0][1],surface[0][2]),
        (surface[1][1],surface[1][2]),
        (surface[2][1],surface[2][2]),
        (surface[3][1],surface[3][2]),
      ]

      if self.point_in_quadrangle(quadrangle_points, point):
        # This follows http://www.gisdeveloper.co.kr/?p=801 's formula
        x1, y1, z1 = surface[0]
        x2, y2, z2 = surface[1]
        x3, y3, z3 = surface[2]

        A = y1*(z2-z3)+y2*(z3-z1)+y3*(z1-z2)
        if A == 0:
          x1, y1, z1 = surface[3]
          A = y1*(z2-z3)+y2*(z3-z1)+y3*(z1-z2)
          if A == 0:
            continue
        B = z1*(x2-x3)+z2*(x3-x1)+z3*(x1-x2)
        C = x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
        D = -(x1*(y2*z3-y3*z2)+x2*(y3*z1-y1*z3)+x3*(y1*z2-y2*z1))
        
        # plane : Ax + By + Cz + D  = 0
        # x = -(By + Cz + D) / A
        x = -(B*y+C*z+D)/A

        xs.append(x)
    
    if len(xs) == 0:
      return None
    
    return min(xs)



# test cases
DS = DiscreteSurface()
DS.add_surface(1, [(1,0,1),(1,0.5,1.5),(1,1,2),(2,1,1)])
DS.add_surface(2, [(1,1,2),(1,1.5,1.5),(1,2,1),(2,1,1)])
DS.add_surface(3, [(1,2,1),(1,1.5,0.5),(1,1,0),(2,1,1)])
DS.add_surface(4, [(1,1,0),(1,0.5,0.5),(1,0,1),(2,1,1)])

assert DS.find_x(0,0) == None
assert DS.find_x(1,1) == 2
assert DS.find_x(0.5,0.5) == 1
assert DS.find_x(1,0) == 1
assert DS.find_x(0,1) == 1
assert DS.find_x(0.75, 0.75) == 1.5
assert DS.find_x(0.75, 1.25) == 1.5
assert DS.find_x(1.25, 1.25) == 1.5
assert DS.find_x(1.25, 0.75) == 1.5