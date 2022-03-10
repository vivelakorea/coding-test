class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def onSegment(p, q, r):
	if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
		(q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
		return True
	return False

def orientation(p, q, r):
	val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
	if (val > 0):
		
		# Clockwise orientation
		return 1
	elif (val < 0):
		
		# Counterclockwise orientation
		return 2
	else:
		
		# Collinear orientation
		return 0

def doIntersect(p1,q1,p2,q2):
	o1 = orientation(p1, q1, p2)
	o2 = orientation(p1, q1, q2)
	o3 = orientation(p2, q2, p1)
	o4 = orientation(p2, q2, q1)

	# General case
	if ((o1 != o2) and (o3 != o4)):
		return True

	# Special Cases

	# p1 , q1 and p2 are collinear and p2 lies on segment p1q1
	if ((o1 == 0) and onSegment(p1, p2, q1)):
		return True

	# p1 , q1 and q2 are collinear and q2 lies on segment p1q1
	if ((o2 == 0) and onSegment(p1, q2, q1)):
		return True

	# p2 , q2 and p1 are collinear and p1 lies on segment p2q2
	if ((o3 == 0) and onSegment(p2, p1, q2)):
		return True

	# p2 , q2 and q1 are collinear and q1 lies on segment p2q2
	if ((o4 == 0) and onSegment(p2, q1, q2)):
		return True

	# If none of the cases
	return False

def pointInSquare(squarePoints, point):
  # squarePoints: [p1, p2, p3, p4]

  orientations = set()

  for i in range(4):
    p = squarePoints[i%4]
    q = squarePoints[(i+1)%4]

    # point on edge
    if onSegment(p, point, q):
      return True
    
    # point not on edge
    orientations.add(orientation(p, q, point))

  if len(orientations) == 1:
    return True

  return False


T = int(input())
for _ in range(T):
  xstart, ystart, xend, yend, xleft, ytop, xright, ybottom = map(
                                                float, input().split())
  p = Point(xstart, ystart)
  q = Point(xend, yend)
  s1 = Point(max(xleft, xright), max(ybottom, ytop))
  s2 = Point(max(xleft, xright), min(ybottom, ytop))
  s3 = Point(min(xleft, xright), min(ybottom, ytop))
  s4 = Point(min(xleft, xright), max(ybottom, ytop))

  squarePoints = [s1, s2, s3, s4]
  
  if pointInSquare(squarePoints, p) and pointInSquare(squarePoints, q):
    print('T')
    continue
  
  if ( doIntersect(s1, s2, p, q) or
       doIntersect(s2, s3, p, q) or
       doIntersect(s3, s4, p, q) or
       doIntersect(s4, s1, p, q) ):
       print('T')
       continue
  
  print('F')
  continue
