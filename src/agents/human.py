from . import player
import numpy as np



class Human(player.Player):

    def __init__(self):
        super().__init__()


    def move(self):
        pos = map(int, input('x y :').split())
        return tuple(pos)
