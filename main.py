import tkinter as tk
from game_logic import setup_game
SIZE = 15
CELL_SIZE = 40
window = tk.Tk()
window.title("Game Cờ Caro")
canvas = tk.Canvas(
    window,
    width=SIZE * CELL_SIZE,
    height=SIZE * CELL_SIZE
)
canvas.pack()
for i in range(SIZE + 1):
    canvas.create_line(
        0,
        i * CELL_SIZE,
        SIZE * CELL_SIZE,
        i * CELL_SIZE
    )
    canvas.create_line(
        i * CELL_SIZE,
        0,
        i * CELL_SIZE,
        SIZE * CELL_SIZE
    )
    setup_game(canvas, SIZE, CELL_SIZE)
window.mainloop()