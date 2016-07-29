import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
window.geometry('900x600')
frame.pack()

redbutton = tkinter.Button(frame, text="Green meme is so Dank!", fg="green")
redbutton.pack(side=tkinter.LEFT)

bluebutton = tkinter.Button(frame, text="Blue meme is so Dank!!", fg="blue")
bluebutton.pack(side=tkinter.RIGHT)

img_1 = "This will totally be an image! Go green meme!"
image_1 = tkinter.Label(window, text=img_1)
image_1.pack(side="left", fill="both", expand="yes")

img_2 = "This will totally be an image! Go blue meme!"
image_2 = tkinter.Label(window, text=img_2)
image_2.pack(side="right", fill="both", expand="yes")




window.mainloop()
