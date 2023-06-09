import tkinter as tk
from constants import *


class UserManageFrame(tk.Frame):
    data = None
    index = 0
    maxLen = None

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)
        self.COMPARING = False
        self.userVar = tk.StringVar(self, None)
        self.gradeVar = tk.StringVar(self, None)
        self.scoreVar = tk.StringVar(self, None)
        self.percentVar = tk.StringVar(self, None)

        heading = tk.Label(self, background=P_COL, foreground=TXT_COL, text="| USER INFORMATION |", font=(FONT_FAM, FONT_SIZE, "bold"), justify=tk.CENTER)
        heading.place(in_=self, relx=0.5, rely=0.06, anchor=tk.CENTER)

        leftMFrame = tk.Frame(self, background=P_COL)
        prevBtn = tk.Button(leftMFrame, text="<", font=(FONT_FAM, FONT_SIZE), padx=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        prevBtn.pack(fill=tk.Y, expand=True)
        prevBtn.bind('<ButtonRelease-1>', lambda event: self.updateIndex(event))
        prevBtn.bind('<Enter>', controller.hoverBtn)
        prevBtn.bind('<Leave>', controller.unhoverBtn)
        leftMFrame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)

        rightMFrame = tk.Frame(self, background=P_COL)
        nextBtn = tk.Button(rightMFrame, text=">", font=(FONT_FAM, FONT_SIZE), padx=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        nextBtn.pack(fill=tk.Y, expand=True)
        nextBtn.bind('<ButtonRelease-1>', lambda event: self.updateIndex(event))
        nextBtn.bind('<Enter>', controller.hoverBtn)
        nextBtn.bind('<Leave>', controller.unhoverBtn)
        rightMFrame.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)
        
        leftFrame = tk.Frame(self, width=(WIN_W // 2 - 50), height=WIN_H - 100, background=P_COL)
        image = tk.PhotoImage(file=GRADE_IMG)
        imageLbl = tk.Label(leftFrame, image=image, width=(WIN_W // 2), background=P_COL)
        imageLbl.photo = image
        imageLbl.place(in_=leftFrame, anchor=tk.CENTER, relx=0.5, rely=0.4)

        self.grade = tk.Label(leftFrame, textvariable=self.gradeVar, font=(FONT_FAM, GRADE_FONT), background=BLACK, foreground=TXT_COL)
        self.grade.place(in_=leftFrame, relx=0.5, rely=0.36, anchor=tk.CENTER)

        self.delBtn = tk.Button(leftFrame, text="Delete User", font=(FONT_FAM, SM_FONT_SIZE), padx=15, pady=8, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, width=15, command=lambda: controller.delUserRes(RESULT_TABLE, self.userVar.get(), 0))
        self.delBtn.place(in_=leftFrame, relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.delBtn.bind('<Enter>', controller.hoverBtn)
        self.delBtn.bind('<Leave>', controller.unhoverBtn)
        leftFrame.pack(side=tk.LEFT, anchor=tk.S, ipadx=10, ipady=10)

    
        rightFrame = tk.Frame(self, width=(WIN_W // 2 - 50), height=WIN_H - 100, bg=P_COL)
        inputFrame = tk.Frame(rightFrame, padx=5, background=P_COL)
        user = tk.Label(inputFrame, text="Username:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        user.pack(pady=2, fill=tk.X)
        self.user = tk.Entry(inputFrame, font=(FONT_FAM, FONT_SIZE), textvariable=self.userVar, width=25, state=tk.DISABLED, disabledforeground=P_COL)
        self.user.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)

        score = tk.Label(inputFrame, text="User Score:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        score.pack(pady=2, fill=tk.X)
        self.score = tk.Entry(inputFrame, font=(FONT_FAM, SM_FONT_SIZE), textvariable=self.scoreVar, width=25, state=tk.DISABLED, disabledforeground=P_COL)
        self.score.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)

        percent = tk.Label(inputFrame, text="User Percentage:", font=(FONT_FAM, SM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        percent.pack(pady=2, fill=tk.X)
        self.percent = tk.Entry(inputFrame, font=(FONT_FAM, SM_FONT_SIZE), textvariable=self.percentVar, width=25, state=tk.DISABLED, disabledforeground=P_COL)
        self.percent.pack(pady=2, fill=tk.X)
    
        dummyLbl = tk.Label(inputFrame, background=P_COL)
        dummyLbl.pack(pady=5, fill=tk.X)
        inputFrame.place(in_=rightFrame , anchor=tk.CENTER, relx=0.5, rely=0.34)
    
        submitFrame = tk.Frame(rightFrame, padx=10, background=P_COL)
        compareBtn = tk.Button(submitFrame, text="Compare Answers", font=(FONT_FAM, SM_FONT_SIZE), width=24, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        compareBtn.pack(padx=5, pady=5)
        compareBtn.bind('<Enter>', controller.hoverBtn)
        compareBtn.bind('<Leave>', controller.unhoverBtn)

        backBtn = tk.Button(submitFrame, text="Go Back", font=(FONT_FAM, SM_FONT_SIZE), width=24, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, command=lambda: controller.showFrame("admin"))
        backBtn.pack(padx=5, pady=5)
        backBtn.bind('<Enter>', controller.hoverBtn)
        backBtn.bind('<Leave>', controller.unhoverBtn)
        submitFrame.place(in_=rightFrame, anchor=tk.CENTER, relx=0.5, rely=0.8)  
        rightFrame.pack(side=tk.RIGHT, anchor=tk.S, ipadx=10, ipady=10)
        compareBtn.config(command=lambda: self.compare(controller, (prevBtn, nextBtn, self.delBtn, compareBtn, backBtn)))


    @classmethod
    def initData(cls, self, data):
        cls.index = 0
        cls.maxLen = len(data) - 1
        cls.data = data
        self.setData()


    def updateIndex(self, event):
        if event.widget['state'] == "active":
            if event.widget["text"] == "<" and UserManageFrame.index > 0:
                UserManageFrame.index -= 1
            elif event.widget["text"] == ">" and UserManageFrame.index < UserManageFrame.maxLen:
                UserManageFrame.index += 1
            self.setData()


    def setData(self):
        for id, entry in UserManageFrame.data:
            if id == UserManageFrame.index:
                self.userVar.set(entry[0])
                self.gradeVar.set(entry[2])
                self.scoreVar.set(entry[3])
                self.percentVar.set(entry[4])

        self.update_idletasks()


    def compare(self, controller, btns):
        if not self.COMPARING:
            self.COMPARING = True

            for btn in btns:
                btn.config(state=tk.DISABLED)

            controller.compareWin(self, controller, self.userVar.get(), btns)