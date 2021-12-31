from enums import Direction
import graphics as g

class Arrow:
  def __init__(self, center, radius, direction):
    self.center = center
    self.radius = radius
    self.direction = direction
    self.arrow = self.__initArrow()

  def __initArrow(self):
    p1 = self.center.clone()
    p2 = self.center.clone()
    arrowCorner1 = self.center.clone()
    arrowCorner2 = self.center.clone()
    arrowShapes = []
    lineRadius = self.radius * 0.9
    arrowCornerDist = self.radius * 0.1
    
    if(self.direction == Direction.UP):
      p1.move(0, lineRadius)
      p2.move(0, -lineRadius)

      arrowCorner1 = p1.clone()
      arrowCorner1.move(-arrowCornerDist, -arrowCornerDist)

      arrowCorner2 = p1.clone()
      arrowCorner2.move(arrowCornerDist, -arrowCornerDist)

    elif(self.direction == Direction.DOWN):
      p1.move(0, -lineRadius)
      p2.move(0, lineRadius)

      arrowCorner1 = p1.clone()
      arrowCorner1.move(arrowCornerDist, arrowCornerDist)

      arrowCorner2 = p1.clone()
      arrowCorner2.move(-arrowCornerDist, arrowCornerDist)

    elif(self.direction == Direction.LEFT):
      p1.move(-lineRadius, 0)
      p2.move(lineRadius, 0)

      arrowCorner1 = p1.clone()
      arrowCorner1.move(arrowCornerDist, arrowCornerDist)

      arrowCorner2 = p1.clone()
      arrowCorner2.move(arrowCornerDist, -arrowCornerDist)

    elif(self.direction == Direction.RIGHT):
      p1.move(lineRadius, 0)
      p2.move(-lineRadius, 0)

      arrowCorner1 = p1.clone()
      arrowCorner1.move(-arrowCornerDist, -arrowCornerDist)

      arrowCorner2 = p1.clone()
      arrowCorner2.move(-arrowCornerDist, arrowCornerDist)

    arrow = g.Polygon(p1, arrowCorner1, arrowCorner2)
    arrow.setFill('red')
    arrow.setOutline('red')
    arrowShapes.append(arrow)
    line = g.Line(p1, p2)
    line.setOutline('red')
    line.setFill('red')
    arrowShapes.append(line)
    return arrowShapes

  def draw(self, win):
    for shape in self.arrow:
      shape.draw(win)

class Tile:
  def __init__(self, center, radius, direction):
    self.center = center
    self.radius = radius

    self.p1 = center.clone()
    self.p1.move(-radius, -radius)

    self.p2 = center.clone()
    self.p2.move(radius, radius)

    self.tile = g.Rectangle(self.p1, self.p2)
    self.tile.setFill('white')

    self.arrow = Arrow(self.center, self.radius, direction)
  
  def draw(self, win):
    self.tile.draw(win)
    self.arrow.draw(win)
