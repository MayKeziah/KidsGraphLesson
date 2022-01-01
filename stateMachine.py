from tkinter import Text
from tkinter.constants import N
from searchAgent import SearchAgent
import graphics as g
from roomba import Roomba
from room import Room
from enums import Direction, Mouse

class Button:
  def __init__(self, p1, p2, text):
    self.p1 = p1
    self.p2 = p2
    x = (p1.x + p2.x)/2
    y = (p1.y + p2.y)/2
    self.text = g.Text(g.Point(x, y), text)
    self.shape = g.Rectangle(p1, p2)

  def draw(self, win):
    self.shape.draw(win)
    self.text.draw(win)

  def undraw(self):
    self.shape.undraw()
    self.text.undraw()

  def clicked(self, point):
    xLow = min(self.p1.x, self.p2.x)
    xHigh = max(self.p1.x, self.p2.x)

    yLow = min(self.p1.y, self.p2.y)
    yHigh = max(self.p1.y, self.p2.y)

    containsX = xLow <= point.x and point.x <= xHigh
    containsY = yLow <= point.y and point.y <= yHigh

    # print("containsX: ", containsX)
    # print("containsY: ", containsY)
    return containsX and containsY

class StateMachine:
  def __init__(self, width = 4, height = 4):
    self.width = width
    self.height = height
    self.gridConversionCoeficient = 100
    self.title = "My Roomba's Journey"
    self.radius = 0.5
    self.startPosition = g.Point(0, 0)

    self.window = g.GraphWin(self.title, (width+2)*self.gridConversionCoeficient, (height+2)*self.gridConversionCoeficient)
    self.roomba = Roomba(self.startPosition, self.radius, self.window)
    self.room = Room(width, height, self.startPosition)

    self.modeManual = 'Mode: Manual'
    self.modeAuto = 'Mode: Auto'
    self.modeBtn = Button(g.Point(width - 2, height - 0.25), g.Point(width - 1, height), self.modeManual)
    self.manual = True

    self.exitBtn = Button(g.Point(width - 0.5, height - 0.25), g.Point(width - 0.2, height), 'Exit')
    self.resetBtn = Button(g.Point(width - 3.5, height - 0.25), g.Point(width - 2.5, height), 'Reset')
    self.buttons = [self.modeBtn, self.exitBtn, self.resetBtn]

    self.__initWindow()
    self.start()

  def __initWindow(self):
    self.window.setCoords(-1, -1, self.width, self.height)
    self.room.draw(self.window)
    self.roomba.draw(self.window)
    for button in self.buttons:
      button.draw(self.window) 
  
  def start(self):
    while(True):
      mouse = self.checkMouse()
      if(mouse == Mouse.EXIT): 
        break

      if(mouse == Mouse.ELSE):
        # print("mouse is none")
        if(self.manual):
          self.takeOneStep()
        else:
          agent = SearchAgent(self.window, self.room, self.roomba, self.checkMouse)
          if (agent.exitCommandRecieved):
            break
          self.window.checkKey()
  
  def reset(self):
    self.room.reset()
    self.roomba.reset()

  def checkMouse(self):
    # print('check mouse')
    mouse = self.window.checkMouse()
    if (mouse is None):
      return Mouse.ELSE

    if(self.exitBtn.clicked(mouse)): 
      self.close()
      return Mouse.EXIT

    if(self.modeBtn.clicked(mouse)):
      self.manual = not self.manual
      if(self.manual):
        self.modeBtn.text.setText(self.modeManual)
      else:
        self.modeBtn.text.setText(self.modeAuto)
      return Mouse.MODE

    if(self.resetBtn.clicked(mouse)):
      self.reset()
      return Mouse.RESET

    return Mouse.ELSE

  def close(self):
    self.window.close()

  def takeOneStep(self):
    direction = self.detectMove()
    if (direction is None):
      return
    tileIsInRoom = self.room.inRoom(self.roomba.center, direction)
    if (tileIsInRoom):
      newLocation = self.room.getTile(self.roomba.center, direction)
      self.room.cleanCurrentTile(self.roomba.center, direction, self.window)
      self.roomba.moveTo(newLocation)
  
  def detectMove(self):
    moves = {'Up': Direction.UP, 'Down': Direction.DOWN, 'Left': Direction.LEFT, "Right": Direction.RIGHT}
    move = self.window.checkKey()
    # print(move)
    if (move is not None and moves.__contains__(move)):
      return moves[move]
    return None

StateMachine()