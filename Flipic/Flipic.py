import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import pygame
pygame.mixer.init()
root = tk.Tk()
root.title("FLIPIC")
root.geometry('1500x1500')
bg = PhotoImage(file ='backg.png')
playkey= PhotoImage(file = 'playbutton.png')
bg2 = bg.zoom(2,2)
def play_click():
   pygame.mixer.music.load("2.mp3")
   pygame.mixer.music.play()
def play_but():
   pygame.mixer.music.load("22.mp3")
   pygame.mixer.music.play()
def play_succes():
   pygame.mixer.music.load("succes.mp3")
   pygame.mixer.music.play()   
def play_screen():
   pygame.mixer.music.load("3.mp3")
   pygame.mixer.music.play()
def secondslide():
    root.withdraw()
    root2 = Toplevel(root)
    root2.geometry('800x800')
    root2.config(bg = 'black')
    front = PhotoImage(file = 'front.png')
    img1  = PhotoImage(file = 'thor.png')
    img2  = PhotoImage(file = 'vision.png')
    img3  = PhotoImage(file = 'witch.png')
    img4  = PhotoImage(file = 'spiderman.png')
    img5  = PhotoImage(file = 'ironman.png')
    img6  = PhotoImage(file = 'captain america.png')
    img7  = PhotoImage(file = 'black panther.png')
    img8  = PhotoImage(file = 'groot.png')
    img9  = PhotoImage(file = 'groot.png')
    img10 = PhotoImage(file = 'black panther.png')
    img11 = PhotoImage(file = 'captain america.png')
    img12 = PhotoImage(file = 'ironman.png')
    img13 = PhotoImage(file = 'spiderman.png')
    img14 = PhotoImage(file = 'witch.png')
    img15 = PhotoImage(file = 'vision.png')
    img16 = PhotoImage(file = 'thor.png')

    def change_image1():
        current_image = button1.cget("image")
        if current_image == str(front):
            button1.config(image = img1)
        else:
            button1.config(image = front)
    def change_image2():
        current_image =button2.cget("image")
        if current_image == str(front):
            button2.config(image = img2)
        else:
            button2.config(image = front)   
    def change_image3():
        current_image = button3.cget("image")
        if current_image == str(front):
            button3.config(image = img3)
        else:
            button3.config(image = front)
    def change_image4():
        current_image = button4.cget("image")
        if current_image == str(front):
            button4.config(image = img4)
        else:
            button4.config(image = front)
    def change_image5():
        current_image = button5.cget("image")
        if current_image == str(front):
            button5.config(image = img5)
        else:
            button5.config(image = front)
    def change_image6():
        current_image = button6.cget("image")
        if current_image == str(front):
            button6.config(image = img6)
        else:
            button6.config(image = front)
    def change_image7():
        current_image = button7.cget("image")
        if current_image == str(front):
            button7.config(image = img7)
        else:
            button7.config(image = front)
    def change_image8():
        current_image = button8.cget("image")
        if current_image == str(front):
            button8.config(image = img8)
        else:
            button8.config(image = front)
    def change_image9():
        current_image = button9.cget("image")
        if current_image == str(front):
            button9.config(image = img9)
        else:
            button9.config(image = front)
    def change_image10():
        current_image = button10.cget("image")
        if current_image == str(front):
            button10.config(image = img10)
        else:
            button10.config(image = front)
    def change_image11():
        current_image = button11.cget("image")
        if current_image == str(front):
            button11.config(image = img11)
        else:
            button11.config(image = front)
    def change_image12():
        current_image = button12.cget("image")
        if current_image == str(front):
            button12.config(image = img12)
        else:
            button12.config(image = front)
    def change_image13():
        current_image = button13.cget("image")
        if current_image == str(front):
            button13.config(image = img13)
        else:
            button13.config(image = front)
    def change_image14():
        current_image = button14.cget("image")
        if current_image == str(front):
            button14.config(image = img14)
        else:
            button14.config(image = front)
    def change_image15():
        current_image = button15.cget("image")
        if current_image == str(front):
            button15.config(image = img15)
        else:
            button15.config(image = front)
    def change_image16():
        current_image = button16.cget("image")
        if current_image == str(front):
            button16.config(image = img16)
        else:
            button16.config(image = front)
         
    button1  = Button(root2, image = front,bg = 'black',command = change_image1)
    button2  = Button(root2, image = front,bg ='black',command  = change_image2)
    button3  = Button(root2, image = front,bg = 'black',command = change_image3)
    button4  = Button(root2, image = front,bg = 'black',command = change_image4)
    button5  = Button(root2, image = front,bg = 'black',command = change_image5)
    button6  = Button(root2, image = front,bg = 'black',command = change_image6)
    button7  = Button(root2, image = front,bg = 'black',command = change_image7)
    button8  = Button(root2, image = front,bg = 'black',command = change_image8)
    button9  = Button(root2, image = front,bg = 'black',command = change_image9)
    button10 = Button(root2, image = front,bg = 'black',command = change_image10)
    button11 = Button(root2, image = front,bg = 'black',command = change_image11)
    button12 = Button(root2, image = front,bg = 'black',command = change_image12)
    button13 = Button(root2, image = front,bg = 'black',command = change_image13)
    button14 = Button(root2, image = front,bg = 'black',command = change_image14)
    button15 = Button(root2, image = front,bg = 'black',command = change_image15)
    button16 = Button(root2, image = front,bg = 'black',command = change_image16)
    def s3():
        messagebox.showinfo("Congratulations", "You've matched all pairs!")
    bttn = Button(root2, text = 'FINISH',bg = 'black',fg = 'white',font = ('arail',30),command = lambda : [play_succes(),s3()])
    button1.grid(row = 2, column = 1)
    button2.grid(row = 2, column = 2)
    button3.grid(row = 2, column = 3)
    button4.grid(row = 2, column = 4)
    button5.grid(row = 3, column = 1)
    button6.grid(row = 3, column = 2)
    button7.grid(row = 3, column = 3)
    button8.grid(row = 3, column = 4)
    button9.grid(row = 4, column = 1)
    button10.grid(row = 4, column = 2)
    button11.grid(row = 4, column = 3)
    button12.grid(row = 4, column = 4)
    button13.grid(row = 5, column = 1)
    button14.grid(row = 5, column = 2)
    button15.grid(row = 5, column = 3)
    button16.grid(row = 5, column = 4)
    bttn.place(x = 900,y = 100)
    root2.mainloop()
def temp_text(e):
   textbox.delete(0,"end")

def click2():
   my_label = Label(root,text = 'Welcome'+ ' ' + textbox.get(),font = ('gabriola',20),bg = 'black',fg = '#40E0D0').place(x = 690,y=520)

my_label = Label(root, image = bg2).place(x = 0,y= 0)

textbox = Entry(root, bg="magenta",font = ('gabriola',18) ,width = 50, borderwidth=3)
textbox.insert(0, 'Enter you name')

button = Button(root,image = playkey,command = lambda:[play_but(),secondslide()],borderwidth= 10 ,bg = 'magenta' )
bon = Button(root,text = 'OK',bg = 'magenta',font = ('arial', 18),command = click2).place(x =1010,y = 455)
textbox.place(x = 560,y = 450)
textbox.bind("<FocusIn>", temp_text)
button.place(x = 700,y = 600)
play_screen()
root.mainloop()



