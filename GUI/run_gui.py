"""Runs the Gui Class
"""

import tkinter as tk
import gui


def run_gui(meme_1, meme_2):
    root = tk.Tk()
    meme_or_not = gui.DankOrStank(root, meme_1, meme_2)
    root.mainloop()


def test_main():
    run_gui('gui_mock_imgs/bluememe', 'gui_mock_imgs/redmeme')

test_main()