from . import player
import numpy as np



class Human(player.Player):

    def __init__(self):
        super().__init__()


    def move(self):
        pos = map(int, input('y x :').split())
        return tuple(pos)
