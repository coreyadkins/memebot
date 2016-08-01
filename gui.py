"""Class object that opens a "Pic-Battle" or "Hot or Not" style voting window, with two clickable memes
that collect a vote for the meme clicked and close the window when voted on.
"""

import tkinter as tk
from PIL import ImageTk
from vote.vote import MemeVote
import PIL


class DankOrStank:
    """Runs Gui for DankOrStank."""
    def __init__(self, master, meme_1, meme_2):
        """Structures window with two entered memes slotted next to each other."""
        self.master = master
        self.meme_1 = meme_1
        self.meme_2 = meme_2
        self.winner = None
        self.quit = False
        frame = tk.Frame(master)
        master.title("Memebot")
        master.geometry('1050x600')
        frame.pack()

        self.label = tk.Label(master, text="Dank or Stank", font=('Times', 40))
        self.label.pack()

        self.left_meme = PIL.ImageTk.PhotoImage(PIL.Image.open(meme_1))
        self.left_meme_as_button = tk.Button(
            frame,
            compound=tk.TOP,
            width=375,
            height=410,
            image=self.left_meme,
            text='Dank!',
            bg='light blue',
            command=self.vote_meme_1)
        self.left_meme_as_button.pack(side='left', padx=25, pady=40)
        self.left_meme_as_button.image = self.left_meme

        self.quit_button = tk.Button(
            frame,
            compound=tk.CENTER,
            width=10,
            height=10,
            text='Quit',
            bg='red',
            command=self.quit_gui)
        self.quit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_meme = PIL.ImageTk.PhotoImage(PIL.Image.open(meme_2))
        self.right_meme_as_button = tk.Button(
            frame,
            compound=tk.TOP,
            width=375,
            height=410,
            image=self.right_meme,
            text='Dank!',
            bg='pink',
            command=self.vote_meme_2)
        self.right_meme_as_button.pack(side=tk.LEFT, padx=25, pady=40)
        self.right_meme_as_button.image = self.right_meme

    def vote_meme_1(self):
        """Returns a Vote Object for meme_1"""
        self.winner = self.meme_1
        self.master.quit()

    def vote_meme_2(self):
        """Returns a Vote Object for meme_2"""
        self.winner = self.meme_2
        self.master.quit()

    def quit_gui(self):
        """Quits the GUI"""
        self.winner = None
        self.quit = True
        self.master.quit()



