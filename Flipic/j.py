import tkinter as tk
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Memory Game")

# Load and shuffle the images
image_paths = ["thor.png", "witch.png", "vision.png", "groot.png", "ironman.png", "spiderman.png"]
images = [Image.open(path) for path in image_paths]
images *= 2  # Duplicate the images to create pairs
shuffle(images)

buttons = [None] * 12
first_button = None
matched_pairs = 0

def on_button_click(index):
    global first_button, matched_pairs
    if buttons[index]["image"] != "":  # Check if the button has an image
        return
    
    image = images[index]
    buttons[index]["image"] = image
    buttons[index]["state"] = tk.DISABLED
    
    if first_button is None:
        first_button = buttons[index]
    else:
        if first_button["image"] == image:
            first_button = None
            matched_pairs += 1
            if matched_pairs == 6:
                messagebox.showinfo("Congratulations", "You've matched all pairs!")
        else:
            root.after(1000, reset_buttons, index)

def reset_buttons(index):
    global first_button
    buttons[index]["image"] = ""
    buttons[index]["state"] = tk.NORMAL
    first_button["image"] = ""
    first_button["state"] = tk.NORMAL
    first_button = None

for i in range(12):
    button = tk.Button(root, image="", width=20, height=10, command=lambda i=i: on_button_click(i))
    button.grid(row=i // 4, column=i % 4)
    buttons[i] = button

root.mainloop()