import tkinter as tk
from constants import *


class QuizFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)
        self.iterVar = 1
        self.answer = tk.StringVar(self, "None")

        leftFrame = tk.Frame(self, background=P_COL)
        prevBtn = tk.Button(leftFrame, text="<", font=(FONT_FAM, FONT_SIZE), padx=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        prevBtn.pack(fill=tk.Y, expand=True)
        # prevBtn.bind('<ButtonRelease-1>', lambda event: self.updateQuest(event, controller))
        prevBtn.bind('<Enter>', controller.hoverBtn)
        prevBtn.bind('<Leave>', controller.unhoverBtn)
        leftFrame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        

        middleFrame = tk.Frame(self, padx=20, pady=5, bg="white", background=P_COL)
        self.questionLbl = tk.Label(middleFrame, background=P_COL, foreground=TXT_COL, text="Question 1", font=(FONT_FAM, FONT_SIZE), wraplength=600, justify=tk.LEFT)
        self.questionLbl.pack(anchor=tk.W, pady=30)
        
        options = tk.Frame(middleFrame, background=P_COL, padx=10, pady=10)
        self.option1 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="Option A", value="A", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0)
        self.option1.pack(anchor=tk.W, pady=5)
        
        self.option2 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="Option B", value="B", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0)
        self.option2.pack(anchor=tk.W, pady=5)
        
        self.option3 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="Option C", value="C", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0)
        self.option3.pack(anchor=tk.W, pady=5)
        
        self.option4 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="Option D", value="D", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0)
        self.option4.pack(anchor=tk.W, pady=5)
        options.pack(padx=30, pady=20, anchor=tk.W)

        self.submitBtn = tk.Button(middleFrame, text="Submit Your Test", font=(FONT_FAM, FONT_SIZE), padx=15, pady=8, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        self.submitBtn.pack(side=tk.BOTTOM, anchor=tk.CENTER, pady=20)
        self.submitBtn.bind('<Enter>', controller.hoverBtn)
        self.submitBtn.bind('<Leave>', controller.unhoverBtn)
        middleFrame.pack(side=tk.LEFT, anchor=tk.CENTER, fill=tk.BOTH, expand=True)
          
        rightFrame = tk.Frame(self, background=P_COL)
        nextBtn = tk.Button(rightFrame, text=">", font=(FONT_FAM, FONT_SIZE), padx=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        nextBtn.pack(fill=tk.Y, expand=True)
        # nextBtn.bind('<ButtonRelease-1>', lambda event: self.updateQuest(event, controller))
        nextBtn.bind('<Enter>', controller.hoverBtn)
        nextBtn.bind('<Leave>', controller.unhoverBtn)
        rightFrame.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)

        