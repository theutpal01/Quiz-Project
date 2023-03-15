import tkinter as tk
from constants import *


class MenuFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)        

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.photo = image
        imageLbl.pack()
        leftFrame.pack(side=tk.LEFT, ipadx=5, ipady=5)
    
        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        headFrame = tk.Frame(rightFrame, background=P_COL)
        # demoBtn = tk.Button(headFrame, text="Give Demo Test", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=20)
        # demoBtn.pack(padx=15, pady=15, anchor=tk.W)
        # demoBtn.bind('<Enter>', controller.hoverBtn)
        # demoBtn.bind('<Leave>', controller.unhoverBtn)
    
        testBtn = tk.Button(headFrame, text="Attempt The Test", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=20)
        testBtn.pack(padx=15, pady=15, anchor=tk.W)
        testBtn.bind('<Enter>', controller.hoverBtn)
        testBtn.bind('<Leave>', controller.unhoverBtn)
    
        resBtn = tk.Button(headFrame, text="Get Your Result", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=20)
        resBtn.pack(padx=15, pady=15, anchor=tk.W)
        resBtn.bind('<Enter>', controller.hoverBtn)
        resBtn.bind('<Leave>', controller.unhoverBtn)
    
        logoutBtn = tk.Button(headFrame, text="Logout Quiz App", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=20) 
        logoutBtn.pack(padx=15, pady=15, anchor=tk.W)
        logoutBtn.bind('<Enter>', controller.hoverBtn)
        logoutBtn.bind('<Leave>', controller.unhoverBtn)
        headFrame.pack()
        rightFrame.pack(side=tk.RIGHT, ipadx=10, ipady=10)
