import tkinter as tk
from constants import *


class QuizManageFrame(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=WIN_W // 2.5, height=WIN_H, background=P_COL)
        heading = tk.Label(self, background=P_COL, foreground=TXT_COL, text="| QUIZ QUESTIONS |", font=(FONT_FAM, FONT_SIZE, "bold"), justify=tk.CENTER)
        heading.place(in_=leftFrame, relx=0.5, rely=0.06, anchor=tk.CENTER)

        self.listView = tk.Listbox(leftFrame, bg=P_COL, fg=TXT_COL, font=(FONT_FAM, 10), activestyle=tk.NONE, relief=tk.FLAT, highlightthickness=1, width=45, height=15)
        self.listView.place(in_=leftFrame, relx=0.5, rely=0.4, anchor=tk.CENTER)
        # self.setListData(controller)

        self.previewBtn = tk.Button(leftFrame, text="Start Preview", font=(FONT_FAM, VSM_FONT_SIZE), command=lambda: self.preview(controller), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        self.previewBtn.place(in_=leftFrame, relx=0.5, rely=0.75, anchor=tk.CENTER)

        self.delBtn = tk.Button(leftFrame, text="Delete Question", font=(FONT_FAM, VSM_FONT_SIZE), command=lambda: self.delete(controller), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        self.delBtn.place(in_=leftFrame, relx=0.5, rely=0.85, anchor=tk.CENTER)
        leftFrame.pack(side=tk.LEFT, ipadx=10, ipady=10)


        rightFrame = tk.Frame(self, width=WIN_W // 1.5, height=WIN_H, background=P_COL)
        inputFrame = tk.Frame(rightFrame, background=P_COL)
        

        qnoLbl = tk.Label(inputFrame, text=f"Enter a question number:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        qnoLbl.pack(pady=(10, 2), fill=tk.X)
        self.questNo = tk.Entry(inputFrame, font=(FONT_FAM, VSM_FONT_SIZE), width=46, disabledforeground=P_COL)
        self.questNo.pack(pady=2, fill=tk.X)

        questLbl = tk.Label(inputFrame, text="Enter a question:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        questLbl.pack(pady=2, fill=tk.X)
        self.quest = tk.Text(inputFrame, font=(FONT_FAM, VSM_FONT_SIZE), width=46, height=5)
        self.quest.pack(pady=(2, 10), fill=tk.X)
                
        setFrame1 = tk.Frame(inputFrame, background=P_COL)
        opt1Frame = tk.Frame(setFrame1, background=P_COL)
        opt1Lbl = tk.Label(opt1Frame, text=f"Enter option 1:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, justify=tk.LEFT, background=P_COL, foreground=TXT_COL)
        self.opt1 = tk.Entry(opt1Frame, font=(FONT_FAM, VSM_FONT_SIZE), width=22, disabledforeground=P_COL)
        opt1Lbl.pack(pady=2, fill=tk.X)
        self.opt1.pack(pady=2)
        opt1Frame.pack(side=tk.LEFT, anchor=tk.E)

        opt2Frame = tk.Frame(setFrame1, background=P_COL)
        opt2Lbl = tk.Label(opt2Frame, text=f"Enter option 2:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, justify=tk.LEFT, background=P_COL, foreground=TXT_COL)
        self.opt2 = tk.Entry(opt2Frame, font=(FONT_FAM, VSM_FONT_SIZE), width=22, disabledforeground=P_COL)
        opt2Lbl.pack(pady=2, fill=tk.X)
        self.opt2.pack(pady=2)
        opt2Frame.pack(side=tk.RIGHT)
        setFrame1.pack(fill=tk.X, anchor=tk.W)

        setFrame2 = tk.Frame(inputFrame, background=P_COL)
        opt3Frame = tk.Frame(setFrame2, background=P_COL)
        opt3Lbl = tk.Label(opt3Frame, text=f"Enter option 3:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, justify=tk.LEFT, background=P_COL, foreground=TXT_COL)
        self.opt3 = tk.Entry(opt3Frame, font=(FONT_FAM, VSM_FONT_SIZE), width=22, disabledforeground=P_COL)
        opt3Lbl.pack(pady=2, fill=tk.X)
        self.opt3.pack(pady=2)
        opt3Frame.pack(side=tk.LEFT, anchor=tk.E)

        opt4Frame = tk.Frame(setFrame2, background=P_COL)
        opt4Lbl = tk.Label(opt4Frame, text=f"Enter option 4:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, justify=tk.LEFT, background=P_COL, foreground=TXT_COL)
        self.opt4 = tk.Entry(opt4Frame, font=(FONT_FAM, VSM_FONT_SIZE), width=22, disabledforeground=P_COL)
        opt4Lbl.pack(pady=2, fill=tk.X)
        self.opt4.pack(pady=2)
        opt4Frame.pack(side=tk.RIGHT)
        setFrame2.pack(fill=tk.X, anchor=tk.W)

        ansLbl = tk.Label(inputFrame, text=f"Enter an answer:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
        ansLbl.pack(pady=(10, 2), fill=tk.X)
        self.ans = tk.Entry(inputFrame, font=(FONT_FAM, VSM_FONT_SIZE), width=46, disabledforeground=P_COL)
        self.ans.pack(pady=2, fill=tk.X)
        inputFrame.pack()

        submitFrame = tk.Frame(rightFrame, padx=20, background=P_COL)
        saveBtn = tk.Button(submitFrame, text="Save Question", font=(FONT_FAM, VSM_FONT_SIZE), command=lambda: self.save(controller), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        saveBtn.pack(side=tk.LEFT, padx=5, pady=5)
        saveBtn.bind('<Enter>', controller.hoverBtn)
        saveBtn.bind('<Leave>', controller.unhoverBtn)

        backBtn = tk.Button(submitFrame, text="Go Back", font=(FONT_FAM, VSM_FONT_SIZE), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        backBtn.pack(side=tk.RIGHT, padx=5, pady=5)
        backBtn.bind('<Enter>', controller.hoverBtn)
        backBtn.bind('<Leave>', controller.unhoverBtn)
        submitFrame.pack(pady=(10, 5)) 
        rightFrame.pack(side=tk.RIGHT, ipadx=10, ipady=10)

        note = tk.Label(self, text="Note: Any changes in the questions will clear the previous results of users!", font=(FONT_FAM, 9), bg=P_COL, fg=TXT_COL)
        note.place(in_=self, relx=0.01, rely=0.95)
