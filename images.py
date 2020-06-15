from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Image Viewer")
root.iconbitmap("favicon.ico")

img1 = ImageTk.PhotoImage(Image.open("vscode.png"))
img2 = ImageTk.PhotoImage(Image.open("python.png"))
img3 = ImageTk.PhotoImage(Image.open("node.png"))
img4 = ImageTk.PhotoImage(Image.open("java.png"))
img5 = ImageTk.PhotoImage(Image.open("unity.png"))

image_list = [img1, img2, img3, img4, img5]

status = Label(root, text="Image 1 of " +
               str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)  # "East" or right side of window

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)


def forward(img_index):
    global label
    global button_forward
    global button_back

    # Forget current image as program changes to new image
    label.grid_forget()
    label = Label(image=image_list[img_index-1])
    button_forward = Button(
        root, text="->", command=lambda: forward(img_index+1))
    button_back = Button(root, text="<-", command=lambda: back(img_index-1))

    if img_index == 5:
        button_forward = Button(root, text="->", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    label.grid(row=0, column=0, columnspan=3)

    # Update status bar
    status = Label(root, text="Image " + str(img_index) + " of " +
                   str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(img_index):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label = Label(image=image_list[img_index-1])
    button_forward = Button(
        root, text="->", command=lambda: forward(img_index+1))
    button_back = Button(root, text="<-", command=lambda: back(img_index-1))

    if img_index == 1:
        button_back = Button(root, text="<-", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    label.grid(row=0, column=0, columnspan=3)

    # Update status bar
    status = Label(root, text="Image " + str(img_index) + " of " +
                   str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<-", command=back, state=DISABLED)
button_forward = Button(root, text="->", command=lambda: forward(2))
button_quit = Button(root, text="Quit", command=root.quit)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2, pady=10)
button_quit.grid(row=1, column=1)
# West+East makes this stretch across width of window
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
