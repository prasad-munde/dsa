import tkinter as tk
import random
board_size = 5
cell_size = 80
ladders = {5: 15, 9: 18, 11: 21}
snakes = {14: 8, 23: 17, 20: 2}
class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladders - 5x5")
        self.canvas = tk.Canvas(root, width=board_size * cell_size, height=board_size * cell_size)
        self.canvas.pack()
        self.dice_label = tk.Label(root, text="Player 1's Turn - Roll the Dice", font=("Arial", 14))
        self.dice_label.pack()
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()
        self.positions = [1, 1]  # Start positions for Player 1 and Player 2
        self.current_player = 0  # 0 for Player 1, 1 for Player 2
        self.draw_board()
        self.players = [
            self.canvas.create_oval(10, 10, 30, 30, fill="blue"),  # Player 1
            self.canvas.create_oval(10, 10, 30, 30, fill="red")   # Player 2
        ]
        self.update_position()
    def draw_board(self):
        for i in range(board_size):
            for j in range(board_size):
                if i % 2 == 0:
                    num = board_size * (board_size - i - 1) + (j + 1)
                else:
                    num = board_size * (board_size - i - 1) + (board_size - j)
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
                self.canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2,
                                        text=str(num), font=("Arial", 12, "bold"))
        for start, end in ladders.items():
            start_row, start_col = self.get_row_col(start)
            end_row, end_col = self.get_row_col(end)
            self.draw_ladder(start_row, start_col, end_row, end_col)
        for start, end in snakes.items():
            start_row, start_col = self.get_row_col(start)
            end_row, end_col = self.get_row_col(end)
            self.draw_snake(start_row, start_col, end_row, end_col)
    def draw_ladder(self, start_row, start_col, end_row, end_col):
        x_start = start_col * cell_size + cell_size // 2
        y_start = (board_size - start_row - 1) * cell_size + cell_size // 2
        x_end = end_col * cell_size + cell_size // 2
        y_end = (board_size - end_row - 1) * cell_size + cell_size // 2
        self.canvas.create_line(x_start, y_start, x_end, y_end, fill="green", width=3)
    def draw_snake(self, start_row, start_col, end_row, end_col):
        x_start = start_col * cell_size + cell_size // 2
        y_start = (board_size - start_row - 1) * cell_size + cell_size // 2
        x_end = end_col * cell_size + cell_size // 2
        y_end = (board_size - end_row - 1) * cell_size + cell_size // 2
        self.canvas.create_line(x_start, y_start, x_end, y_end, fill="red", width=3)
    def get_row_col(self, position):
        row = (position - 1) // board_size
        col = (position - 1) % board_size
        if row % 2 == 1:
            col = board_size - col - 1
        return row, col
    def roll_dice(self):
        roll = random.randint(1, 6)
        self.positions[self.current_player] += roll
        if self.positions[self.current_player] in ladders:
            self.positions[self.current_player] = ladders[self.positions[self.current_player]]
        elif self.positions[self.current_player] in snakes:
            self.positions[self.current_player] = snakes[self.positions[self.current_player]]
        if self.positions[self.current_player] >= board_size * board_size:
            self.positions[self.current_player] = board_size * board_size
            self.update_position()
            self.dice_label.config(text=f"🎉 Player {self.current_player + 1} Wins!")
            self.roll_button.config(state=tk.DISABLED)
            return
        self.update_position()
        self.dice_label.config(
            text=f"Player {self.current_player + 1} rolled: {roll}\nNow Player {((self.current_player + 1) % 2) + 1}'s Turn"
        )
        self.current_player = (self.current_player + 1) % 2
    def update_position(self):
        for i in range(2):  # Update position for both players
            row = (self.positions[i] - 1) // board_size
            col = (self.positions[i] - 1) % board_size
            if row % 2 == 1:
                col = board_size - col - 1
            x = col * cell_size + cell_size // 2
            y = (board_size - row - 1) * cell_size + cell_size // 2
            self.canvas.coords(self.players[i], x - 10, y - 10, x + 10, y + 10)
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()


