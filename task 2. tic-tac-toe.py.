import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")

        self.board = [" " for _ in range(9)]  # Represents the Tic-Tac-Toe board
        self.current_player = "X"  # Start with player X

        self.buttons = [tk.Button(self.window, text=" ", font=("Helvetica", 20), width=5, height=2,
                                  command=lambda i=i: self.on_button_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def start(self):
        self.window.mainloop()

    def on_button_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        # Simple AI using Minimax algorithm
        best_score = float("-inf")
        best_move = None

        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = i

        self.on_button_click(best_move)

    def minimax(self, board, depth, is_maximizing):
        scores = {"X": -1, "O": 1, "draw": 0}

        winner = self.check_winner(board)
        if winner:
            return scores[winner]

        if is_maximizing:
            max_eval = float("-inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    eval = self.minimax(board, depth + 1, False)
                    board[i] = " "  # Undo the move
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    eval = self.minimax(board, depth + 1, True)
                    board[i] = " "  # Undo the move
                    min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self, board=None):
        if board is None:
            board = self.board

        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                return board[combo[0]]  # Return the winning player

        if " " not in board:
            return "draw"  # The board is full, it's a draw

        return None  # No winner yet

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ")

        self.current_player = "X"  # Start with player X

if __name__ == "__main__":
    game = TicTacToe()
    game.start()
