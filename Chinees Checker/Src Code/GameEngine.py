import tkinter as tk

from tkmacosx import Button as bt
from tkinter import *
import tkinter.font as font
from Game import start_game


def easyClick():
    root.destroy()
    winner = start_game(1, 'Chinese Checkers With Eazy Mood')
    root2 = tk.Tk()
    frame = get_frame(root2)
    printWinner(winner, frame)
    frame.grid()
    root2.mainloop()


def mediumClick():
    root.destroy()
    winner = start_game(2, 'Chinese Checkers With Medium Mood')
    root2 = tk.Tk()
    frame = get_frame(root2)
    printWinner(winner, frame)
    frame.grid()
    root2.mainloop()


def hardClick():
    root.destroy()
    winner = start_game(4, 'Chinese Checkers With Hard Mood')
    root2 = tk.Tk()
    frame = get_frame(root2)
    printWinner(winner, frame)
    frame.grid()
    root2.mainloop()


def printWinner(winner, frame):
    if winner == 1:
        txt = "Hard Luck AI Win !!"
        size = 25
    elif winner == 4:
        txt = "Congratulations you Win!!"
        size = 23
    else:
        txt = ""
        size = 25
    myfont1 = font.Font(family='Helvetica', size=size)
    label = Label(frame, text=txt, font=myfont1)
    label.place(x=150, y=66, anchor="center")


def center(root):
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2) - 50
    y = (hs / 2) - (h / 2) - 180
    root.geometry('+%d+%d' % (x, y))


def get_frame(root):
    center(root)
    root.title("Winner Board")
    frm = Frame(root)
    frm.config(width=300, height=150)
    frm.grid_propagate(flag=False)
    return frm


# First Screen
root = tk.Tk()
frm = Frame(root)
center(root)
root.title('Chinese checkers Game')
frm.config(bg='white')
frm.grid()
myFont = font.Font(family='Helvetica', size=25)
Label(frm, text="Choose a Level!", font=myFont, bg='white').pack(pady=10)
bt(frm, text="Easy", command=easyClick, bg='green', padx=130, pady=60, font=myFont).pack()
bt(frm, text="Medium", command=mediumClick, bg='yellow', padx=130, pady=60, font=myFont).pack()
bt(frm, text="Hard", command=hardClick, bg='red', padx=130, pady=60, font=myFont).pack()
root.mainloop()
