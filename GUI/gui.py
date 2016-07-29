"""Opens a window and displays two random memes, user clicks meme and vote is saved,
then window loops with two more random memes.

Currently, just opens a window and displays two static memes and vote clicks do nothing. No loops as of yet.


Future goal, click button to open alternate window with top 5 memes displayed.
"""

import tkinter as tk
# import PIL


def memebot_display():
    window = tk.Tk()
    frame = tk.Frame(window)
    window.geometry('900x600')
    frame.pack()

    memebot_text = "MemeBot's Dank Memes"
    floating_text = tk.Label(window, text=memebot_text)
    floating_text.pack(fill='both', expand='yes')
    floating_text.place(x=375, y=5)


    blue_meme = tk.PhotoImage(file="gui_mock_imgs/bluememe.gif")
    blue_meme_as_button = tk.Button(frame, compound=tk.TOP, width=375, height=410, image=blue_meme,
                        text="That's a Dank blue Meme!!", bg='light blue')
    blue_meme_as_button.pack(side=tk.LEFT, padx=25, pady=40)
    blue_meme_as_button.image = blue_meme


    blue_button = tk.Button(window, text='Blue meme is so Dank!!', fg='blue')
    blue_button.pack(side='left', expand='no')


    red_meme = tk.PhotoImage(file="gui_mock_imgs/redmeme.gif")
    red_meme_as_button = tk.Button(frame, compound=tk.TOP, width=375, height=410, image=red_meme,
                        text="That's a Dank red Meme!", bg='pink')
    red_meme_as_button.pack(side=tk.LEFT, padx=25, pady=40)
    red_meme_as_button.image = red_meme
    red_button = tk.Button(window, text='Red meme is so Dank!', fg='red')
    red_button.pack(side='right', expand='no')

    window.mainloop()

def main():
    memebot_display()

main()