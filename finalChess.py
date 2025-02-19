import tkinter as tk

# 棋盘大小
BOARD_SIZE = 10  # Update board size to 10
CELL_SIZE = 60
CELL_PADDING = 20  # 边框与棋盘线的距离
BOARD_WIDTH = CELL_SIZE * (BOARD_SIZE - 1)  # 9条垂直线的宽度
BOARD_HEIGHT = CELL_SIZE * (BOARD_SIZE - 1)

# 棋子初始位置
INITIAL_POSITIONS = {
    'r': [(0, 0), (8, 0)],
    'n': [(1, 0), (7, 0)],
    'b': [(2, 0), (6, 0)],
    'a': [(3, 0), (5, 0)],
    'k': [(4, 0)],
    'c': [(1, 2), (7, 2)],
    'p': [(0, 3), (2, 3), (4, 3), (6, 3), (8, 3)],
    'R': [(0, 9), (8, 9)],
    'N': [(1, 9), (7, 9)],
    'B': [(2, 9), (6, 9)],
    'A': [(3, 9), (5, 9)],
    'K': [(4, 9)],
    'C': [(1, 7), (7, 7)],
    'P': [(0, 6), (2, 6), (4, 6), (6, 6), (8, 6)]
}

# 棋子颜色
PIECE_COLORS = {
    'r': 'red',
    'n': 'red',
    'b': 'red',
    'a': 'red',
    'k': 'red',
    'c': 'red',
    'p': 'red',
    'R': 'black',
    'N': 'black',
    'B': 'black',
    'A': 'black',
    'K': 'black',
    'C': 'black',
    'P': 'black'
}

class Chessboard:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=BOARD_WIDTH + 2 * CELL_PADDING, height=BOARD_HEIGHT + 2 * CELL_PADDING)
        self.canvas.pack()
        self.pieces = {}
        self.selected_piece = None
        self.draw_board()
        self.place_pieces()
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_line(self, start_x, start_y, end_x, end_y, width=1, color="black"):
        """ 绘制一条线 """
        self.canvas.create_line(start_x, start_y, end_x, end_y, width=width, fill=color)

    def draw_board(self):
        # 绘制水平线
        for i in range(BOARD_SIZE):
            width = 3 if i in {0, 4, 5, BOARD_SIZE - 1} else 1
            self.draw_line(CELL_PADDING, i * CELL_SIZE + CELL_PADDING, 
                           BOARD_WIDTH - CELL_SIZE + CELL_PADDING, i * CELL_SIZE + CELL_PADDING,
                           width=width)
        
        # 绘制垂直线
        for i in range(BOARD_SIZE - 2):  # 绘制8条垂直线，去掉最后一条（第10条）
            width = 3 if i in {0, BOARD_SIZE - 2} else 1
            self.draw_line(i * CELL_SIZE + CELL_PADDING, CELL_PADDING, 
                            i * CELL_SIZE + CELL_PADDING, BOARD_HEIGHT + CELL_PADDING, 
                            width=width)

        # 恢复第9条垂直线样式
        self.draw_line((BOARD_SIZE - 2) * CELL_SIZE + CELL_PADDING, CELL_PADDING, 
                       (BOARD_SIZE - 2) * CELL_SIZE + CELL_PADDING, BOARD_HEIGHT + CELL_PADDING, 
                       width=3)

    def place_pieces(self):
        for piece, positions in INITIAL_POSITIONS.items():
            for x, y in positions:
                self.create_piece(piece, x, y)

    def create_piece(self, piece, x, y):
        """ 创建棋子 """
        x_pos = x * CELL_SIZE + CELL_PADDING
        y_pos = y * CELL_SIZE + CELL_PADDING
        piece_id = self.canvas.create_oval(x_pos - 20, y_pos - 20, x_pos + 20, y_pos + 20, fill=PIECE_COLORS[piece])
        self.pieces[piece_id] = (piece, x, y)

    def on_click(self, event):
        """ 处理点击事件，选择或移动棋子 """
        x = round((event.x - CELL_PADDING) / CELL_SIZE)
        y = round((event.y - CELL_PADDING) / CELL_SIZE)
        if self.selected_piece:
            self.move_piece(x, y)
            self.selected_piece = None
        else:
            self.select_piece(x, y)

    def select_piece(self, x, y):
        """ 选择棋子 """
        for piece_id, (piece, px, py) in self.pieces.items():
            if px == x and py == y:
                self.selected_piece = (piece_id, piece, px, py)
                break

    def move_piece(self, x, y):
        """ 移动棋子 """
        piece_id, piece, old_x, old_y = self.selected_piece
        x_pos = x * CELL_SIZE + CELL_PADDING
        y_pos = y * CELL_SIZE + CELL_PADDING
        self.canvas.coords(piece_id, x_pos - 20, y_pos - 20, x_pos + 20, y_pos + 20)
        self.pieces[piece_id] = (piece, x, y)

if __name__ == "__main__":
    root = tk.Tk()
    chessboard = Chessboard(root)
    root.mainloop()

