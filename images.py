from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Image Viewer")
root.iconbitmap("favicon.ico")

img = ImageTk.PhotoImage(Image.open("vscode.png"))
label = Label(image=img)
label.pack()

button_quit = Button(root, text="Quit", command=root.quit)
button_quit.pack()

root.mainloop()
