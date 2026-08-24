import tkinter as tk

current_player = "X"

board = []


def setup_game(canvas, size, cell_size):
    global board

    # Tạo bàn cờ trong bộ nhớ
    board = []

    for i in range(size):
        row = []

        for j in range(size):
            row.append("")

        board.append(row)

    # Bắt sự kiện click
    canvas.bind(
        "<Button-1>",
        lambda event: click(event, canvas, size, cell_size)
    )


def click(event, canvas, size, cell_size):
    global current_player

    # Xác định hàng và cột
    row = event.y // cell_size
    col = event.x // cell_size

    # Kiểm tra nằm trong bàn cờ
    if row < 0 or row >= size:
        return

    if col < 0 or col >= size:
        return

    # Kiểm tra ô đã có quân chưa
    if board[row][col] != "":
        return

    # Đặt quân
    board[row][col] = current_player

    # Tọa độ giữa ô
    x = col * cell_size + cell_size // 2
    y = row * cell_size + cell_size // 2

    # Vẽ X hoặc O
    canvas.create_text(
        x,
        y,
        text=current_player,
        font=("Arial", 24)
    )

    # Đổi lượt
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"