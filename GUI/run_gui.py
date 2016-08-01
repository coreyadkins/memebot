"""Runs the Gui Class
"""

import tkinter as tk
import gui


def run_gui(meme_1, meme_2):
    """Runs the Stank or Dank gui for memebot"""
    root = tk.Tk()
    meme_or_not = gui.DankOrStank(root, meme_1, meme_2)
    root.mainloop()


def test_main():
    """Just a test running file, because I have no idea how to doctest graphical stuff."""
    run_gui('gui_mock_imgs/bluememe.jpg', 'gui_mock_imgs/redmeme.jpg')

test_main()