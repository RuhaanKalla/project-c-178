# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:20:15 2022

@author: Dell
"""

from tkinter import*
import random
root = Tk()
root.geometry("500x500")
root.title("Encapsulation")
root.config(bg = "white")

label = Label(root , font = "arial 25" , bg = "white" , fg = "black")
label.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

class game:
    def __init__(self):
        self._score = 0
        
    def updateGame(self):
        self.text = ["GREEN" , "BLUE" , "RED" , "YELLOW" , "ORANGE" , "PURPLE" , "CYAN" , "AQUA" , "GREY"]
        self.random_no_for_text = random.randint(0 , 8)
        self.color = ["green" , "blue" , "red" , "yellow" ,"orange" , "purple" , "cyan" , "aqua" , "grey"]
        self.random_no_for_color = random.randint(0 , 8)
        label["text"] = self.text[self.random_no_for_text]
        label["fg"] = self.color[self.random_no_for_color]
        
obj = game()

btn = Button(root , text = "Start" , command = obj.updateGame , bg = "SpringGreen4" , fg = "white" , relief = FLAT , padx = 5 , pady = 5 , font = "arial 15") 
btn.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)
root.mainloop()       


