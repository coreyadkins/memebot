"""Main."""

from randomfile import get_random_input_file
from gui import DankOrStank
import tkinter as tk
from vote.vote import MemeVote

def run_gui(meme_1, meme_2):
    """Runs the Stank or Dank gui for memebot"""
    root = tk.Tk()
    meme_or_not = DankOrStank(root, meme_1, meme_2)
    root.mainloop()
    return meme_or_not.winner

def main ():
    image_1 = get_random_input_file(dir='output')
    image_2 = get_random_input_file(dir='output')
    winner = run_gui(image_1, image_2)
    MemeVote().vote(image_1, image_2, winner)

if __name__ == '__main__':
    main()