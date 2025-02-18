import tkinter as tk

class ChineseChessBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("中国象棋")
        
        # 棋盘参数
        self.board_size = 500
        self.cell_size = self.board_size // 9
        self.piece_radius = self.cell_size // 3
        
        # 创建画布
        self.canvas = tk.Canvas(master, 
                              width=self.board_size,
                              height=self.board_size,
                              bg="#FFD700")
        self.canvas.pack()
        
        # 绘制棋盘
        self.draw_board()
    
    def draw_board(self):
        # 绘制纵向线
        for col in range(9):
            x = col * self.cell_size
            self.canvas.create_line(x, 0, x, self.board_size)
        
        # 绘制横向线
        for row in range(10):
            y = row * self.cell_size
            self.canvas.create_line(0, y, self.board_size, y)
        
        # 绘制九宫斜线
        self.canvas.create_line(3*self.cell_size, 0, 
                              5*self.cell_size, 2*self.cell_size, 
                              fill="red", width=2)
        self.canvas.create_line(3*self.cell_size, 2*self.cell_size,
                              5*self.cell_size, 0,
                              fill="red", width=2)
        self.canvas.create_line(3*self.cell_size, 7*self.cell_size,
                              5*self.cell_size, 9*self.cell_size,
                              fill="red", width=2)
        self.canvas.create_line(3*self.cell_size, 9*self.cell_size,
                              5*self.cell_size, 7*self.cell_size,
                              fill="red", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    game = ChineseChessBoard(root)
    root.mainloop()
