import enum

class Direction(enum.Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Mouse(enum.Enum):
  EXIT = 0
  MODE = 1
  ELSE = 2