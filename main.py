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
    root.destroy()
    return meme_or_not.winner, meme_or_not.quit


def main():
    gui_quit = False
    while gui_quit is False:
        image_1 = get_random_input_file(dir='output')
        image_2 = get_random_input_file(dir='output')
        winner, gui_quit = run_gui(image_1, image_2)
        if not gui_quit:
            MemeVote().vote(image_1, image_2, winner)


if __name__ == '__main__':
    main()
