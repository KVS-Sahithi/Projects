import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class MatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Matching Game")
        
        self.images = [
            "groot.png", "blackpanther.png", "ironman.png", 
            "groot.png", "blackpanther.png", "ironman.png"
        ]
        
        random.shuffle(self.images)
        self.buttons = []
        self.first_button = None
        
        for _ in range(6):
            button = tk.Button(self.root, command=lambda b=button: self.on_button_click(b))
            button.grid(row=_ // 2, column=_ % 2)
            self.buttons.append(button)
        
        self.load_images()
    
    def load_images(self):
        self.photo_images = [Image.open(image) for image in self.images]
        self.tk_images = [ImageTk.PhotoImage(image) for image in self.photo_images]
        
        for button, tk_image in zip(self.buttons, self.tk_images):
            button.config(image=tk_image)
            button.image = tk_image
    
    def on_button_click(self, button):
        button_index = self.buttons.index(button)
        image_index = self.images.index(self.images[button_index])
        
        if self.first_button is None:
            self.first_button = button
            button.config(state=tk.DISABLED)
        elif self.first_button != button:
            self.first_button.config(state=tk.NORMAL)
            if image_index == self.images.index(self.images[self.buttons.index(self.first_button)]):
                button.config(state=tk.DISABLED)
                self.first_button = None
                if all(b["state"] == tk.DISABLED for b in self.buttons):
                    messagebox.showinfo("Congratulations", "You've matched all pairs!")
            else:
                self.first_button = None

root = tk.Tk()
game = MatchingGame(root)
root.mainloop()
