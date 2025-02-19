class Piece:
    def __init__(self, piece_type, color, x, y):
        self.piece_type = piece_type
        self.color = color  # e.g., "red" or "black"
        self.x = x  # grid x coordinate
        self.y = y  # grid y coordinate

    def __repr__(self):
        return f"{self.color} {self.piece_type} at ({self.x}, {self.y})"
