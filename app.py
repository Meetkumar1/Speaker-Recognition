from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from train import *
from test import *

root = Tk()
root.title("Speaker Recognition")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.state('zoomed')

## Function for resizing the Image

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo

## Resizable Image

image = Image.open(r'pics/background_main.gif')
global copy_of_image
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

## Function

def training():
    Training_file()

def testing():
    Testing_file()

## Adding Buttons

train_button = Button(root, fg="black", highlightbackground='dark blue' ,font=("Courier New",30,'bold'), activeforeground="orange", text='Enroll', height=1, width= 15, padx=10, pady=10, command = training)
train_button.place(relx=0.7, rely=0.6, anchor=CENTER)

test_button = Button(root, fg="black", highlightbackground='dark blue' ,font=("Courier New",30,'bold'), text='Login', height=1, width= 15, padx=10, pady=10, command = testing)
test_button.place(relx=0.7, rely=0.7, anchor=CENTER)

quit = Button(root, fg="black", highlightbackground='dark blue' ,font=("Courier New",30,'bold'), text="Quit", height=1, width= 5, command=root.destroy, padx=10, pady=10)
quit.place(relx=0.9, rely=0.3, anchor=CENTER)

root.mainloop()
