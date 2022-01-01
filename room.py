import graphics as g
from enums import Direction
from tile import Tile

class Grid(g._BBox):
  def __init__(self, p1, p2):
    g._BBox.__init__(self, p1, p2)
    self.background = self.__initBackground()
    self.gridLines = self.__initGrid()
  
  def __initGrid(self):
    gridLines = []
    # Verticals
    x = min(self.p1.x, self.p2.x)
    x2 = max(self.p1.x, self.p2.x)
    while x <= x2:
      low = g.Point(x, min(self.p1.y, self.p2.y))
      high = g.Point(x, max(self.p1.y, self.p2.y))
      verticalLine = g.Line(low, high)
      gridLines.append(verticalLine)
      x+=1

    # Horizontals
    y = min(self.p1.y, self.p2.y)
    y2 = max(self.p1.y, self.p2.y)    
    while y <= y2:
      left = g.Point(min(self.p1.x, self.p2.x), y)
      right = g.Point(max(self.p1.x, self.p2.x), y)
      horizontalLine = g.Line(left, right)
      gridLines.append(horizontalLine)
      y+=1

    return gridLines

  def __initBackground(self):
    background = g.Rectangle(self.p1, self.p2)
    background.setFill("grey")
    return background
        
  def __repr__(self):
      return "Grid({}, {})".format(str(self.p1), str(self.p2))
  
  def draw(self, win):
    self.background.draw(win)
    for line in self.gridLines:
      line.draw(win)
      
  def undraw(self):
      for line in self.gridLines:
        line.undraw()

  def clone(self):
      other = Grid(self.p1, self.p2)
      other.config = self.config.copy()
      return other

class Room:
  def __init__(self, width, height, start=g.Point(0, 0), radius = 0.5):
    self.radius = radius
    self.start = start
    self.end = g.Point(width, height)

    self.width = width
    self.height = height

    self.visitedGraph = self.__initVisitedGraph()
    self.tileGraph = {}
    self.grid = self.__initGrid()

  def __initVisitedGraph(self):
    graph = {}
    for row in range(self.height):
      for col in range(self.width):
        graph[(row, col)] = False
    return graph

  def __initGrid(self):
    gridP1 = self.start.clone()
    gridP1.move(-self.radius, -self.radius)
    gridP2 = self.end.clone()
    gridP2.move(-self.radius, -self.radius)
    return Grid(gridP1, gridP2)

  def draw(self, win):
    self.grid.draw(win)

  def getTile(self, roombaCoords, direction):
    newPoint = roombaCoords.clone()
    if (direction == Direction.UP):
      newPoint.move(0, 1)
    elif (direction == Direction.DOWN):
      newPoint.move(0, -1)
    elif (direction == Direction.RIGHT):
      newPoint.move(1, 0)
    elif (direction == Direction.LEFT):
      newPoint.move(-1, 0)
    return newPoint

  def cleanCurrentTile(self, point, direction, win):
    newTile = Tile(point, self.radius, direction)
    newTile.draw(win)
    coord = (point.x, point.y)
    if(not self.tileGraph.__contains__(coord)):
      self.tileGraph[coord] = []
    self.tileGraph[coord].append(newTile)
    self.visitedGraph[coord] = True

  def reset(self):
    self.visitedGraph = self.__initVisitedGraph()
    for tileList in self.tileGraph.values():
      for tile in tileList:
        tile.undraw()
    self.tileGraph = {}

  # '''
  #   Implement this function
  # '''
  # def legalMove(self, start, direction):
  #   newPoint = self.getCoordinates(start, direction)
  #   return self.inRoom(newPoint)
    
  def inRoom(self, start, direction):
    newPoint = self.getTile(start, direction)
    return self.visitedGraph.__contains__((newPoint.x, newPoint.y))

  # i.e. not visited, the graph contains this square and it's dirty
  def isDirty(self, start, direction):
    newPoint = self.getTile(start, direction)
    coord = (newPoint.x, newPoint.y)
    return self.visitedGraph.__contains__(coord) and not self.visitedGraph[coord]
