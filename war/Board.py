from Field import FIElD
import tkinter as tk
window = tk.Tk()

class Board:
    def __init__(self):
        self.window = window
        self.canvas = self.create_canvas()
        self.map = FIElD.copy()
        self.cell_size = 30

    def create_canvas(self):
        field_width = len(FIElD[0])
        field_height = len(FIElD)
        self.window.config(
            width=field_width,
            height=field_height
        )

        self.window.resizable(
            width=True,
            height=True
        )

        canvas = tk.Canvas(
            self.window,
            width=field_width,
            height=field_height,
            bg='black'
        )
        canvas.pack(fill=tk.BOTH, expand=True)

        return canvas

    def draw_field(self):
        width = len(self.map[0])
        height = len(self.map)

        color = ''

        for i in range(height):
            for j in range(width):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                if self.map[i][j] == 1:
                    color = "blue"
                elif self.map[i][j] == 0:
                    color = "black"
                elif self.map[i][j] == 2:
                    color = "blue"
                elif self.map[i][j] == 3:
                    color = "pink"
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )
        self.canvas.pack()


if __name__ == '__main__':
    board = Board()
    board.draw_field()
    window.mainloop()


