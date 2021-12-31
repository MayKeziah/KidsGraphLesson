import graphics as g

class Roomba:
  def __init__(self, center, radius):
      self.center = center
      self.radius = radius
      self.shape = self.__initShape()
  
  def __initShape(self):
    roomba = g.Circle(self.center, self.radius)
    roomba.setFill('black')

    buttonOuter = g.Circle(self.center, self.radius*0.25)
    buttonOuter.setFill('grey')

    buttonLight = g.Circle(self.center, self.radius*0.18)
    buttonLight.setFill('green')

    buttonInner = g.Circle(self.center, self.radius*0.13)
    buttonInner.setFill('grey')
    return [roomba, buttonOuter, buttonLight, buttonInner]

  def draw(self, win):
    for shape in self.shape:
      shape.draw(win)

  def undraw(self):
    for shape in self.shape:
          shape.undraw()

  def move(self, dx, dy):
    self.center.move(dx, dy)
    for shape in self.shape:
      shape.move(dx, dy)
