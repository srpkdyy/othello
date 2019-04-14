class Player:

    def __init__(self):
        self.color = None


    def set_piece_color(self, color):
        self.color = color


    def get_piece_color(self):
        return self.color
    

    def update(self, board):
        pass

    def move(self):
        return (0, 0)