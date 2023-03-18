import tkinter as tk
from tkinter import filedialog
from constants import *


class QuizManageFrame(tk.Frame):
    Preview = None
    data = None
    quests = None


    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)

        leftFrame = tk.Frame(self, width=WIN_W // 2.5, height=WIN_H, background=P_COL)
        heading = tk.Label(self, background=P_COL, foreground=TXT_COL, text="| QUIZ QUESTIONS |", font=(FONT_FAM, FONT_SIZE, "bold"), justify=tk.CENTER)
        heading.place(in_=leftFrame, relx=0.5, rely=0.06, anchor=tk.CENTER)

        self.listView = tk.Listbox(leftFrame, bg=P_COL, fg=TXT_COL, font=(FONT_FAM, 10), activestyle=tk.NONE, relief=tk.FLAT, highlightthickness=1, width=45, height=15)
        self.listView.place(in_=leftFrame, relx=0.5, rely=0.4, anchor=tk.CENTER)
        # self.setListData(controller)

        self.previewBtn = tk.Button(leftFrame, text="Start Preview", font=(FONT_FAM, VSM_FONT_SIZE), command=lambda: self.previewText(), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        self.previewBtn.place(in_=leftFrame, relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.previewBtn.bind('<Enter>', controller.hoverBtn)
        self.previewBtn.bind('<Leave>', controller.unhoverBtn)

        self.delBtn = tk.Button(leftFrame, text="Delete Question", font=(FONT_FAM, VSM_FONT_SIZE), command=lambda: self.delQuest(controller), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        self.delBtn.place(in_=leftFrame, relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.delBtn.bind('<Enter>', controller.hoverBtn)
        self.delBtn.bind('<Leave>', controller.unhoverBtn)
        leftFrame.pack(side=tk.LEFT, ipadx=10, ipady=10)


        rightFrame = tk.Frame(self, width=WIN_W // 1.5, height=WIN_H, background=P_COL)
        inputFrame = tk.Frame(rightFrame, background=P_COL)

        questLbl = tk.Label(inputFrame, text="Enter question body:", font=(FONT_FAM, VSM_FONT_SIZE), anchor=tk.W, background=P_COL, foreground=TXT_COL)
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
        self.saveBtn = tk.Button(submitFrame, text="Save Question", font=(FONT_FAM, VSM_FONT_SIZE), command=lambda: controller.saveQuest(self.getData()), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        self.saveBtn.pack(side=tk.LEFT, padx=5, pady=5)
        self.saveBtn.bind('<Enter>', controller.hoverBtn)
        self.saveBtn.bind('<Leave>', controller.unhoverBtn)

        backBtn = tk.Button(submitFrame, text="Go Back", font=(FONT_FAM, VSM_FONT_SIZE), width=22, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, command=lambda: controller.showFrame("admin"))
        backBtn.pack(side=tk.RIGHT, padx=5, pady=5)
        backBtn.bind('<Enter>', controller.hoverBtn)
        backBtn.bind('<Leave>', controller.unhoverBtn)
        submitFrame.pack(pady=(30, 0))

        self.multiSaveBtn = tk.Button(rightFrame, text="Save Multiple Questions", font=(FONT_FAM, VSM_FONT_SIZE), width=46, pady=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, command=lambda: self.saveMultiple(controller))
        self.multiSaveBtn.pack(padx=5, pady=5)
        self.multiSaveBtn.bind('<Enter>', controller.hoverBtn)
        self.multiSaveBtn.bind('<Leave>', controller.unhoverBtn)

        rightFrame.pack(side=tk.RIGHT, ipadx=10, ipady=10)

        note = tk.Label(self, text="Note: Any changes in the questions will clear the previous results of users!", font=(FONT_FAM, 9), bg=P_COL, fg=TXT_COL)
        note.place(in_=self, relx=0.01, rely=0.95)


    @classmethod
    def initData(cls, self, data):
        cls.Preview = False
        self.switchState()
        self.clearData()
        cls.data = data
        cls.quests = []

        for _, entry in data:
            cls.quests.append(entry[0])
        cls.quests = tuple(enumerate(cls.quests))
       
        self.setData()

    
    @staticmethod
    def formatText(text, limit):
        if len(text) > limit:
            return text[:limit + 1] + "..."
        return text


    def setData(self):
        self.update_idletasks()
        self.listView.delete(0, tk.END)
        for i, quest in QuizManageFrame.quests:
            self.listView.insert(i, " " + str(i + 1) + ". " + self.formatText(quest, 46))


    def clearData(self):
        self.update_idletasks()
        self.quest.delete(1.0, tk.END)
        self.opt1.delete(0, tk.END)
        self.opt2.delete(0, tk.END)
        self.opt3.delete(0, tk.END)
        self.opt4.delete(0, tk.END)
        self.ans.delete(0, tk.END)


    def getData(self):
        return self.quest.get(1.0, tk.END)[:-1], self.opt1.get(), self.opt2.get(), self.opt3.get(), self.opt4.get(), self.ans.get()


    def switchState(self, indexS=None):
        if QuizManageFrame.Preview and indexS is not None:
            self.quest.insert(1.0, QuizManageFrame.data[indexS][1][0])
            self.opt1.insert(0, QuizManageFrame.data[indexS][1][1])
            self.opt2.insert(0, QuizManageFrame.data[indexS][1][2])
            self.opt3.insert(0, QuizManageFrame.data[indexS][1][3])
            self.opt4.insert(0, QuizManageFrame.data[indexS][1][4])
            self.ans.insert(0, QuizManageFrame.data[indexS][1][5])
            self.previewBtn.config(text="Stop Preview")

            for widget in (self.quest, self.opt1, self.opt2, self.opt3, self.opt4, self.delBtn, self.ans, self.saveBtn, self.multiSaveBtn):
                widget.configure(state=tk.DISABLED)
        
        elif not QuizManageFrame.Preview:
            self.previewBtn.config(text="Start Preview")
            for widget in (self.quest, self.opt1, self.opt2, self.opt3, self.opt4, self.ans, self.delBtn, self.saveBtn, self.multiSaveBtn):
                widget.configure(state=tk.NORMAL)
            self.clearData()


    def previewText(self):
        selected = self.listView.curselection()
        selected = selected[0] if len(selected) != 0 else None

        if selected is not None and not QuizManageFrame.Preview:
            QuizManageFrame.Preview = True
            self.switchState(selected)
        elif QuizManageFrame.Preview:
            QuizManageFrame.Preview = False
            self.switchState()
        else:
            print("Please first select a question to preview it.")
        

    def delQuest(self, controller:tk.Tk):
        itms = self.listView.get(0, tk.END)
        selected = self.listView.curselection()
        selected = selected[0] if len(selected) != 0 else None

        if selected is not None:
            qName = QuizManageFrame.quests[selected][1]
            info = controller.database.delQuestByName(QUIZ_TABLE, qName)
            print(qName, info)
            if info[0] == "Success":
                print("The question haas been deleted successfully!")
            else:
                print("Something went wrong! Please restart the program.")
            controller.showQuizDetails()


    def saveMultiple(self, controller: tk.Tk):
        file = filedialog.askopenfilename(title='Open a file', initialdir='', filetypes=(("Only text files", "*.txt"),))
        text = None
        with open(file, "r") as f:
            text = f.readline()

        values = eval(text)
        controller.saveQuestMultiple(values)