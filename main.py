"""Main."""

from gui import DankOrStank
import tkinter as tk
from vote.vote import MemeVote
import os


def run_gui(meme_1, meme_2):
    """Runs the Stank or Dank gui for memebot"""
    root = tk.Tk()
    meme_or_not = DankOrStank(root, meme_1, meme_2)
    root.mainloop()
    root.destroy()
    return meme_or_not.winner, meme_or_not.quit


def main():
    """ main """
    gui_quit = False
    while gui_quit is False:
        all_insts = ['output/' + x for x in os.listdir('output') if x[-4:] == '.jpg']
        use_insts = MemeVote().get_least_voted(all_insts)

        winner, gui_quit = run_gui(use_insts[0], use_insts[1])
        if not gui_quit:
            MemeVote().vote(use_insts[0], use_insts[1], winner)


if __name__ == '__main__':
    main()
