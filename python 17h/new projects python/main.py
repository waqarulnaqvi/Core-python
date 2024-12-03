import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'

        # Create buttons
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        if self.buttons[i][j]['text'] == '':
            self.buttons[i][j]['text'] = self.current_player
            if self.check_winner(i, j):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[row][j]['text'] == self.current_player for j in range(3)):
            return True

        # Check column
        if all(self.buttons[i][col]['text'] == self.current_player for i in range(3)):
            return True

        # Check diagonals
        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)) or \
           all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
        self.current_player = 'X'


if _name_ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()