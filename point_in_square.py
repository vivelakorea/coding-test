def point_on_line(_p1, _p2, _point):
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

def point_in_square(sqaure_points, point):
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
  # sqaure_points: [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

  areas = []

  for i in range(4):
    p1 = sqaure_points[i%4]
    p2 = sqaure_points[(i+1)%4]

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

# debug point_on_line
def debug_point_on_line():
  assert (point_on_line((0,0),(1,0),(-1,1))) == False
  assert (point_on_line((0,0),(1,0),(-1,0))) == False
  assert (point_on_line((0,0),(1,0),(-1,-1))) == False

  assert (point_on_line((0,0),(1,0),(0,1))) == False
  assert (point_on_line((0,0),(1,0),(0,0))) == True
  assert (point_on_line((0,0),(1,0),(0,-1))) == False

  assert (point_on_line((0,0),(1,0),(0.5,1))) == False
  assert (point_on_line((0,0),(1,0),(0.5,0))) == True
  assert (point_on_line((0,0),(1,0),(0.5,-1))) == False

  assert (point_on_line((0,0),(1,0),(1,1))) == False
  assert (point_on_line((0,0),(1,0),(1,0))) == True
  assert (point_on_line((0,0),(1,0),(1,-1))) == False

  assert (point_on_line((0,0),(1,0),(2,1))) == False
  assert (point_on_line((0,0),(1,0),(2,0))) == False
  assert (point_on_line((0,0),(1,0),(2,-1))) == False



  assert (point_on_line((0,0),(0,1),(-1,2))) == False
  assert (point_on_line((0,0),(0,1),(0,2))) == False
  assert (point_on_line((0,0),(0,1),(1,2))) == False

  assert (point_on_line((0,0),(0,1),(-1,1))) == False
  assert (point_on_line((0,0),(0,1),(0,1))) == True
  assert (point_on_line((0,0),(0,1),(1,1))) == False

  assert (point_on_line((0,0),(0,1),(-1,0.5))) == False
  assert (point_on_line((0,0),(0,1),(0,0.5))) == True
  assert (point_on_line((0,0),(0,1),(1,0.5))) == False

  assert (point_on_line((0,0),(0,1),(-1,0))) == False
  assert (point_on_line((0,0),(0,1),(0,0))) == True
  assert (point_on_line((0,0),(0,1),(1,0))) == False

  assert (point_on_line((0,0),(0,1),(-1,-1))) == False
  assert (point_on_line((0,0),(0,1),(0,-1))) == False
  assert (point_on_line((0,0),(0,1),(1,-1))) == False



  assert (point_on_line((0,0),(1,1),(0,2))) == False
  assert (point_on_line((0,0),(1,1),(1,2))) == False
  assert (point_on_line((0,0),(1,1),(2,2))) == False

  assert (point_on_line((0,0),(1,1),(-1,1))) == False
  assert (point_on_line((0,0),(1,1),(0,1))) == False
  assert (point_on_line((0,0),(1,1),(1,1))) == True
  assert (point_on_line((0,0),(1,1),(2,1))) == False

  assert (point_on_line((0,0),(1,1),(0.5,0.5))) == True

  assert (point_on_line((0,0),(1,1),(-1,0))) == False
  assert (point_on_line((0,0),(1,1),(0,0))) == True
  assert (point_on_line((0,0),(1,1),(1,0))) == False
  assert (point_on_line((0,0),(1,1),(2,0))) == False

  assert (point_on_line((0,0),(1,1),(-1,-1))) == False
  assert (point_on_line((0,0),(1,1),(-1,0))) == False
  assert (point_on_line((0,0),(1,1),(-1,1))) == False

def debug_point_in_square():
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(-1,2)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0,2)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0.5,2)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(1,2)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(2,2)) == False

  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(-1,1)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0,1)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0.5,1)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(1,1)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(2,1)) == False

  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(-1,0.5)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0,0.5)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0.5,0.5)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(1,0.5)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(2,0.5)) == False

  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(-1,0)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0,0)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0.5,0)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(1,0)) == True
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(2,0)) == False

  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(-1,-1)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0,-1)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(0.5,-1)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(1,-1)) == False
  assert point_in_square([(0,0),(1,0),(1,1),(0,1)],(2,-1)) == False

  

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,2)) == False

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,1)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,1)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,1)) == False

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,0.5)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,0.5)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-0.5,0.5)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,0.5)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0.75,0.5)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,0.5)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,0.5)) == False

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,0)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,0)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-0.5,0)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,0)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0.5,0)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,0)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,0)) == False

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,-0.5)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,-0.5)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-0.5,-0.5)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,-0.5)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0.25,-0.5)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,-0.5)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,-0.5)) == False

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,-1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,-1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-0.5,-1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,-1)) == True
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0.5,-1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,-1)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,-1)) == False

  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-2,-2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(-1,-2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(0,-2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(1,-2)) == False
  assert point_in_square([(0,1),(1,1),(0,-1),(-1,0)],(2,-2)) == False
  

debug_point_on_line()
debug_point_in_square()