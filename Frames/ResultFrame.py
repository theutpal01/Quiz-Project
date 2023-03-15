import tkinter as tk
from constants import *


class ResultFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, background=P_COL)
        image = tk.PhotoImage(file=GRADE_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.photo = image
        imageLbl.pack()

        self.grade = tk.Label(leftFrame, text="", font=(FONT_FAM, GRADE_FONT), background=BLACK, foreground=TXT_COL)
        self.grade.place(in_=leftFrame, relx=0.5, rely=0.4, anchor=tk.CENTER)
        leftFrame.pack(side=tk.LEFT, ipadx=10, ipady=10)
    
        rightFrame = tk.Frame(self, width=(WIN_W // 2), height=WIN_H, bg=P_COL)
        inputFrame = tk.Frame(rightFrame, padx=5, background=P_COL)
        user = tk.Label(inputFrame, text="Username:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        user.pack(pady=2, fill=tk.X)
        self.user = tk.Entry(inputFrame, font=(FONT_FAM, FONT_SIZE), width=25, state=tk.DISABLED, disabledforeground=P_COL)
        self.user.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)

        score = tk.Label(inputFrame, text="Your Score:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        score.pack(pady=2, fill=tk.X)
        self.score = tk.Entry(inputFrame, font=(FONT_FAM, SM_FONT_SIZE), width=25, state=tk.DISABLED, disabledforeground=P_COL)
        self.score.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)

        percent = tk.Label(inputFrame, text="Your Percentage:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        percent.pack(pady=2, fill=tk.X)
        self.percent = tk.Entry(inputFrame, font=(FONT_FAM, SM_FONT_SIZE), width=25, state=tk.DISABLED, disabledforeground=P_COL)
        self.percent.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)
        inputFrame.place(in_=rightFrame , anchor=tk.CENTER, relx=0.5, rely=0.34)
    
        submitFrame = tk.Frame(rightFrame, padx=10, background=P_COL)
        compareBtn = tk.Button(submitFrame, text="Compare Answers", font=(FONT_FAM, SM_FONT_SIZE), width=24, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        compareBtn.pack(padx=5, pady=5)
        compareBtn.bind('<Enter>', controller.hoverBtn)
        compareBtn.bind('<Leave>', controller.unhoverBtn)

        backBtn = tk.Button(submitFrame, text="Go Back", font=(FONT_FAM, SM_FONT_SIZE), width=24, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        backBtn.pack(padx=5, pady=5)
        backBtn.bind('<Enter>', controller.hoverBtn)
        backBtn.bind('<Leave>', controller.unhoverBtn)
        submitFrame.place(in_=rightFrame, anchor=tk.CENTER, relx=0.5, rely=0.8)  
        rightFrame.pack(side=tk.RIGHT, ipadx=10, ipady=10)