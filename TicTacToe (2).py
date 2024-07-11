import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.window, text=" ", font=('normal', 40), width=5, height=2, 
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        self.window.mainloop()
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.create_board()

    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a, b, c in win_conditions)



    def on_button_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O")
        if self.check_winner("O"):
            messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
            self.reset_board()
        elif " " not in self.board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            self.reset_board()
        else:
            self.current_player = "X"

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if " " not in board:
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(score, best_score)
            return best_score

if __name__ == "__main__":
    TicTacToe()

