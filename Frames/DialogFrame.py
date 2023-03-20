import tkinter as tk
import tkinter.messagebox as msg
from constants import *


class DialogFrame(tk.Frame):
    attempted = None

    def __init__(self, controller: tk.Tk):
        self.controller = controller


    def showBox(self, title:str, body:str, type:str):
        if type == "i":
            msg.showinfo(title, body)
        elif type == "w":
            msg.showwarning(title, body)
        elif type == "e":
            msg.showerror(title, body)


    def showOkBox(self, title:str, body:str):
        return msg.askokcancel(title, body)
    

    def showOkBox(self, title:str, body:str):
        return msg.askokcancel(title, body)
    
    def showYesNoBox(self, title:str, body:str):
        return msg.askyesno(title, body)
        
        
