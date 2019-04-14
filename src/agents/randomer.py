from . import player
import numpy as np



class Randomer(player.Player):

    def __init__(self):
        super().__init__()


    def move(self):
        pos = np.random.randint(1, 9, size=2)
        return tuple(pos)
