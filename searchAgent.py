import time

from enums import Mouse

class SearchAgent:
  def __init__(self, win, room, roomba, checkMouseFn):
    self.checkMouseFn = checkMouseFn
    self.window = win
    self.room = room
    self.roomba = roomba
    self.exitCommandRecieved = False
    self.cleanAll()

  def cleanAll(self):
    while(not self.isTerminal()):
      mouse = self.checkMouseFn()
      if (mouse == Mouse.EXIT):
        self.exitCommandRecieved = True
        break
      if(mouse == Mouse.MODE):
        break
      self.takeOneStep()
      time.sleep(1)

  '''
    Implement function
  '''
  def isTerminal(self):
    return False

  '''
    Implement function
  '''
  def takeOneStep(self):
    print('step')