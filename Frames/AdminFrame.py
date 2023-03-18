import tkinter as tk
from constants import *


class AdminFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL) 

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        image = tk.PhotoImage(file=PRI_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.photo = image
        imageLbl.place(in_=leftFrame, anchor=tk.CENTER, relx=0.5, rely=0.5)
        leftFrame.pack(side=tk.LEFT, ipadx=10, ipady=10)
    
        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
    
        headFrame = tk.Frame(rightFrame, background=P_COL)
        self.test = True
        
        userBtn = tk.Button(headFrame, text="User Management", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=25, command=controller.showUserDetails)
        userBtn.pack(padx=15, pady=15, anchor=tk.W)
        userBtn.bind('<Enter>', controller.hoverBtn)
        userBtn.bind('<Leave>', controller.unhoverBtn)
    
        questBtn = tk.Button(headFrame, text="Quiz Question Management", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=25, command=lambda: controller.showQuizDetails())
        questBtn.pack(padx=15, pady=15, anchor=tk.W)
        questBtn.bind('<Enter>', controller.hoverBtn)
        questBtn.bind('<Leave>', controller.unhoverBtn)
    
        logoutBtn = tk.Button(headFrame, text="Logout Quiz App", font=(FONT_FAM, FONT_SIZE), padx=10, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=25, command=lambda : controller.showFrame("auth")) 
        logoutBtn.pack(padx=15, pady=15, anchor=tk.W)
        logoutBtn.bind('<Enter>', controller.hoverBtn)
        logoutBtn.bind('<Leave>', controller.unhoverBtn)
        headFrame.place(in_=rightFrame, anchor=tk.CENTER, relx=0.5, rely=0.5)

        rightFrame.pack(side=tk.RIGHT, ipadx=10, ipady=10)
