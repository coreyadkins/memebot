"""Class object that opens a "Pic-Battle" or "Hot or Not" style voting window, with two clickable memes
that collect a vote for the meme clicked and close the window when voted on.
"""

import tkinter as tk
import vote

class DankOrStank:
    """Runs Gui for DankOrStank."""
    def __init__(self, master, meme_1, meme_2):
        """Structures window with two entered memes slotted next to each other."""
        self.master = master
        self.meme_1 = meme_1
        self.meme_2 = meme_2
        frame = tk.Frame(master)
        master.title("Memebot")
        master.geometry('900x600')
        frame.pack()

        self.label = tk.Label(master, text="Dank or Stank", font=('Times', 40))
        self.label.pack()

        self.blue_meme = tk.PhotoImage(file=meme_1)
        self.blue_meme_as_button = tk.Button(
            frame,
            compound=tk.TOP,
            width=375,
            height=410,
            image=self.blue_meme,
            text='Dank!',
            bg='light blue',
            command=self.vote_meme_1)
        self.blue_meme_as_button.pack(side='left', padx=25, pady=40)
        self.blue_meme_as_button.image = self.blue_meme

        self.red_meme = tk.PhotoImage(file=meme_2)
        self.red_meme_as_button = tk.Button(
            frame,
            compound=tk.TOP,
            width=375,
            height=410,
            image=self.red_meme,
            text='Dank!',
            bg='pink',
            command=self.vote_meme_2)
        self.red_meme_as_button.pack(side=tk.LEFT, padx=25, pady=40)
        self.red_meme_as_button.image = self.red_meme

    def vote_meme_1(self):
        """Returns a Vote Object for meme_1"""
        return vote.MemeVote([self.meme_1], [self.meme_2], [self.meme_1])
        self.master.quit()

    def vote_meme_2(self):
        """Returns a Vote Object for meme_2"""
        return vote.MemeVote([self.meme_1], [self.meme_2], [self.meme_2])
        self.master.quit()

