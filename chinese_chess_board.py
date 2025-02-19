import tkinter as tk

class ChineseChessBoard(tk.Canvas):
    def __init__(self, master=None, width=600, height=335, grid_size=60, **kwargs):
        super().__init__(master, width=width, height=height, background='lightgoldenrodyellow', highlightthickness=0, **kwargs)
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid_color = 'black'
        self.river_color = 'blue'
        self.star_color = 'black'
        self.init_board()

    def init_board(self):
        self.draw_grid()
        self.draw_palaces()
        self.draw_border()

    def draw_grid(self):
        # Calculate the offset to center the chessboard in the canvas
        offset_x = (self.width - 9 * self.grid_size) // 2
        offset_y = (self.height - 5 * self.grid_size) // 2

        # Adjust the loop to retain only 5 horizontal lines
        for i in range(5):  # 5 horizontal lines
            x1 = offset_x
            y1 = offset_y + i * self.grid_size
            x2 = offset_x + 8 * self.grid_size  # Adjust the horizontal lines to terminate at the ninth vertical line
            y2 = y1
            self.create_line(x1, y1, x2, y2, fill=self.grid_color, width=2)

        # Adjust the vertical lines to extend down to the fifth horizontal line
        for j in range(9):  # 9 vertical lines
            x1 = offset_x + j * self.grid_size
            y1 = offset_y
            x2 = x1
            y2 = offset_y + 4 * self.grid_size
            self.create_line(x1, y1, x2, y2, fill=self.grid_color, width=2)

    def draw_palaces(self):
        # Calculate the offset to center the chessboard in the canvas
        offset_x = (self.width - 9 * self.grid_size) // 2
        offset_y = (self.height - 5 * self.grid_size) // 2

        # Palace 1 (top)
        x1 = offset_x + 3 * self.grid_size
        y1 = offset_y
        x2 = offset_x + 5 * self.grid_size
        y2 = offset_y + 2 * self.grid_size
        self.create_line(x1, y1, x2, y2, fill=self.grid_color, width=2)
        self.create_line(x1, y2, x2, y1, fill=self.grid_color, width=2)

    def draw_border(self):
        # Remove the outer black lines from the chessboard
        pass

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Chinese Chess Board")
    board = ChineseChessBoard(root)
    board.pack()
    root.mainloop()