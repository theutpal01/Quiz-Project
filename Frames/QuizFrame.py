import tkinter as tk
from constants import *


class QuizFrame(tk.Frame):
    data = None
    index = 0
    maxLen = None
    uAnswers = None


    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.configure(background=P_COL)
        self.answer = tk.StringVar(self, "     ")

        leftFrame = tk.Frame(self, background=P_COL)
        prevBtn = tk.Button(leftFrame, text="<", font=(FONT_FAM, FONT_SIZE), padx=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        prevBtn.pack(fill=tk.Y, expand=True)
        prevBtn.bind('<ButtonRelease-1>', self.updateIndex)
        prevBtn.bind('<Enter>', controller.hoverBtn)
        prevBtn.bind('<Leave>', controller.unhoverBtn)
        leftFrame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        

        middleFrame = tk.Frame(self, padx=20, pady=5, bg="white", background=P_COL)
        self.questionLbl = tk.Label(middleFrame, background=P_COL, foreground=TXT_COL, text="Question 1", font=(FONT_FAM, FONT_SIZE), wraplength=600, justify=tk.LEFT)
        self.questionLbl.pack(anchor=tk.W, pady=30)
        
        options = tk.Frame(middleFrame, background=P_COL, padx=10, pady=10)
        self.option1 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="", value="", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0, command=self.updateAnswer)
        self.option1.pack(anchor=tk.W, pady=5)
        
        self.option2 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="", value="", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0, command=self.updateAnswer)
        self.option2.pack(anchor=tk.W, pady=5)
        
        self.option3 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="", value="", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0, command=self.updateAnswer)
        self.option3.pack(anchor=tk.W, pady=5)
        
        self.option4 = tk.Radiobutton(options, background=P_COL, foreground=TXT_COL, selectcolor=S_COL, text="", value="", variable=self.answer, font=(FONT_FAM, FONT_SIZE), relief=tk.FLAT, border=0, command=self.updateAnswer)
        self.option4.pack(anchor=tk.W, pady=5)
        options.pack(padx=30, pady=20, anchor=tk.W)

        self.submitBtn = tk.Button(middleFrame, text="Submit Your Test", font=(FONT_FAM, FONT_SIZE), padx=15, pady=8, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0, command=lambda: self.submitQuiz(controller))
        self.submitBtn.pack(side=tk.BOTTOM, anchor=tk.CENTER, pady=20)
        self.submitBtn.bind('<Enter>', controller.hoverBtn)
        self.submitBtn.bind('<Leave>', controller.unhoverBtn)
        middleFrame.pack(side=tk.LEFT, anchor=tk.CENTER, fill=tk.BOTH, expand=True)
          
        rightFrame = tk.Frame(self, background=P_COL)
        nextBtn = tk.Button(rightFrame, text=">", font=(FONT_FAM, FONT_SIZE), padx=5, background=S_COL, foreground=TXT_COL, relief=tk.FLAT, bd=0)
        nextBtn.pack(fill=tk.Y, expand=True)
        nextBtn.bind('<ButtonRelease-1>', self.updateIndex)
        nextBtn.bind('<Enter>', controller.hoverBtn)
        nextBtn.bind('<Leave>', controller.unhoverBtn)
        rightFrame.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y)


    @classmethod
    def initData(cls, self, data):
        cls.index = 0
        cls.data = data
        cls.uAnswers = {}
        cls.maxLen = len(data) - 1
        self.setData(cls.data[cls.index][1])


    def updateIndex(self, event):
        if event.widget["text"] == "<" and QuizFrame.index > 0:
            QuizFrame.index -= 1
        elif event.widget["text"] == ">" and QuizFrame.index < QuizFrame.maxLen:
            QuizFrame.index += 1
        self.answer.set("    ")
        self.setData(QuizFrame.data[QuizFrame.index][1])


    def updateAnswer(self):
        if self.answer.get not in QuizFrame.uAnswers.values():
            QuizFrame.uAnswers.update({QuizFrame.data[QuizFrame.index][1][0]: self.answer.get()})


    def setData(self, data):
        self.update_idletasks()

        if data[0] in QuizFrame.uAnswers.keys():
            self.answer.set(QuizFrame.uAnswers.get(data[0]))

        self.questionLbl["text"] = str(QuizFrame.index + 1) + ". " + str(data[0])
        self.option1["text"] = data[1]
        self.option2["text"] = data[2]
        self.option3["text"] = data[3]
        self.option4["text"] = data[4]
        self.option1["value"] = data[1]
        self.option2["value"] = data[2]
        self.option3["value"] = data[3]
        self.option4["value"] = data[4]


    @staticmethod
    def getGrade(percent:float):
        grade = None
        if 97 <= percent <= 100:
            grade = "A+"
        elif 93 <= percent < 97:
            grade = "A"
        elif 90 <= percent < 93:
            grade = "A-"
        elif 87 <= percent < 90:
            grade = "B+"
        elif 83 <= percent < 87:
            grade = "B"
        elif 80 <= percent < 83:
            grade = "B-"
        elif 77 <= percent < 80:
            grade = "C+"
        elif 73 <= percent < 77:
            grade = "C"
        elif 70 <= percent < 73:
            grade = "C-"
        elif 67 <= percent < 70:
            grade = "D+"
        elif 65 <= percent < 67:
            grade = "D"
        elif percent < 65:
            grade = "F"
        return grade
    
    
    def submitQuiz(self, controller):


        maxScroe = len(QuizFrame.data)
        userScore = 0

        for quest in QuizFrame.data:
            if QuizFrame.uAnswers.get(quest[1][0]) == quest[1][5]:
                userScore += 1

        score = (str(userScore) + "/" + str(maxScroe))
        percentage = round((userScore / maxScroe) * 100, 2)
        grade = self.getGrade(percentage)
        percentage = str(percentage) + "%"

        if len(QuizFrame.uAnswers) < len(QuizFrame.data):
            print("All the questions are not answered! Do you wish to continue?")
            controller.quizComplete(QuizFrame.uAnswers, score, percentage, grade)
        else:
            print("All the questions are answered! Quiz has been submitted.")
            controller.quizComplete(QuizFrame.uAnswers, score, percentage, grade)




                
                