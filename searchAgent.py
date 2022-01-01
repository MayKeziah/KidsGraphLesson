import time

from enums import Direction, Mouse

class SearchAgent:
  def __init__(self, win, room, roomba, checkMouseFn):
    self.checkMouseFn = checkMouseFn
    self.window = win
    self.room = room
    self.roomba = roomba
    self.exitCommandRecieved = False
    while(self.cleanAll()):
      time.sleep(1)

  def cleanAll(self):
    direction = self.getDirection()
    while(direction is not None):
      mouse = self.checkMouseFn()
      if (mouse == Mouse.EXIT):
        self.exitCommandRecieved = True
        break
      if (mouse == Mouse.MODE):
        break
      if (mouse == Mouse.RESET):
        return True
      self.takeOneStep(direction)
      direction = self.getDirection()
      time.sleep(1)
    return False

  '''
    Implement function
  '''
  def getDirection(self):
    return None

  '''
    Implement function
  '''
  def takeOneStep(self, direction):
    return