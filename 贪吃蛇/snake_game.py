from game import Game
from config import DEFAULT_WIN_SCORE

if __name__ == '__main__':
    # 选择模式
    try:
        import tkinter as tk
        from tkinter import simpledialog, messagebox
        root = tk.Tk()
        root.withdraw()
        mode = messagebox.askyesno('Mode Select', 'Do you want to use AI mode?\nYes = AI, No = Player')
        mode = 'ai' if mode else 'player'
        value = simpledialog.askinteger('Win Score', 'Please enter win score (default 10):', minvalue=1)
        root.destroy()
        win_score = value if value else DEFAULT_WIN_SCORE
    except Exception:
        mode = 'player'
        win_score = DEFAULT_WIN_SCORE
    game = Game(win_score, mode)
    game.run() 