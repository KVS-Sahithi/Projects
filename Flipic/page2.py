import tkinter
from tkinter import *
import pygame
pygame.mixer.init()

root=tkinter.Tk()
root.title("Memory Flip")
root.geometry("900x900")
def play_sound():
   pygame.mixer.music.load("2.mp3")
   pygame.mixer.music.play()
bg = PhotoImage(file ='pic.png')
def click():
    return
button1 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button2 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button3 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button4 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button5 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button6 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button7 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button8 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button9 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button10 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button11 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button12 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button13 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button14 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button15 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])
button16 = tkinter.Button(root,image = bg,command = lambda:[click(), play_sound()])


button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)
button4.grid(row=1,column=4)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=2,column=3)
button8.grid(row=2,column=4)
button9.grid(row=3,column=1)
button10.grid(row=3,column=2)
button11.grid(row=3,column=3)
button12.grid(row=3,column=4)
button13.grid(row=4,column=1)
button14.grid(row=4,column=2)
button15.grid(row=4,column=3)
button16.grid(row=4,column=4)



root.mainloop()