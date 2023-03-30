from constants import *
import tkinter as tk
import tkinter.ttk as ttk
import json
from Frames.DialogFrame import DialogFrame
from Frames.AuthFrame import AuthFrame
from Frames.MenuFrame import MenuFrame
from Frames.QuizFrame import QuizFrame
from Frames.ResultFrame import ResultFrame
from Frames.AdminFrame import AdminFrame
from Frames.UserManageFrame import UserManageFrame
from Frames.QuizManageFrame import QuizManageFrame

from database import Database


class App(tk.Tk):
    name = None

    def __init__(self):
        tk.Tk.__init__(self)

        scrWidth = self.winfo_screenwidth()
        scrHeight = self.winfo_screenheight()

        x = (scrWidth // 2) - (WIN_W // 2)
        y = (scrHeight // 2) - (WIN_H // 2)

        
        self.title(WIN_T)
        self.geometry(f"{WIN_W}x{WIN_H}+{x}+{y}")
        self.resizable(False, False)
        # self.iconbitmap("deps/quizImg.ico")

        self.configure(background=P_COL)
        self.bind("<Configure>", self.refresh)
        self.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.box = DialogFrame(self)

        self.initDB()

        container = tk.Frame(self)
        container.pack(fill="both", expand=True, padx=2, pady=2)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        self.initFrames(container)
        self.showFrame("auth")


    def initFrames(self, container):
        auth = AuthFrame(container, self)
        auth.grid(row=0, column=0, sticky="nsew")

        menu = MenuFrame(container, self)
        menu.grid(row=0, column=0, sticky="nsew")

        result = ResultFrame(container, self)
        result.grid(row=0, column=0, sticky="nsew")

        quiz = QuizFrame(container, self)
        quiz.grid(row=0, column=0, sticky="nsew")

        admin = AdminFrame(container, self)
        admin.grid(row=0, column=0, sticky="nsew")

        uManage = UserManageFrame(container, self)
        uManage.grid(row=0, column=0, sticky="nsew")

        qManage = QuizManageFrame(container, self)
        qManage.grid(row=0, column=0, sticky="nsew")

        self.frames.update({"auth": auth, "menu": menu, "quiz": quiz, "result": result, "admin": admin, "uManage": uManage, "qManage": qManage})


    def initDB(self):
        self.database = Database(HOST, USER, PWD, DB)
        info = self.database.connect()

        if info[0] == "Success":
            info = self.database.initTables(AUTH_TABLE, RESULT_TABLE, QUIZ_TABLE)
        else:
            self.box.showBox("Error", info[1], "e")

        self.database.disconnect()


    # SHOW THE FRAME ON THE MAIN APP
    def showFrame(self, toShowCont):
        frame = self.frames.get(toShowCont)
        frame.tkraise()


    # WHEN ANY BUTTON IS HOVERED
    def hoverBtn(self, event):
        event.widget["bg"] = T_COL


    # WHEN ANY BUTTON IS UNHOVERED
    def unhoverBtn(self, event):
        event.widget["bg"] = S_COL


    # METHOD TO REFRESH THE GUI
    def refresh(self, e=None):
        self.update_idletasks()


    # METHOD TO PROMPT QUIT DIALOG
    def on_quit(self):
        if self.box.showYesNoBox("Close App", "Do you really want to quit the application?"):
            if self.database.myDB.is_connected():
                self.database.disconnect()
            self.destroy()


    # ================= AUTH FUNCTIONS ======================= #
    def register(self):
        name, pwd = self.frames.get("auth").name.get(), self.frames.get("auth").pwd.get()

        if len(name) !=0 and len(pwd) !=0:
            
            if " " in name and name.isalnum():
                self.box.showBox("Warning", "Username cannot contain space and should be only alpha numeric!", "w")

            
            elif len(pwd) < 8 or len(pwd) > 20:
                self.box.showBox("Warning", "Password should be of 8 to 20 letters.", "w")

            else:
                info = self.database.connect()
                if info[0] == "Success":
                    if name == "admin":
                        info = self.database.insertIntoAuthTable(AUTH_TABLE, (name, pwd), True)
                    else:
                        info = self.database.insertIntoAuthTable(AUTH_TABLE, (name, pwd))

                    if info[0] == "Error":
                        if info[1][0] == 1062:
                            self.box.showBox("Warning", "Username already taken! Please use a different username.", "w")
                            self.frames.get("auth").pwd.set("")
                        else:
                            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
                    else:
                        self.frames.get("auth").name.set("")
                        self.frames.get("auth").pwd.set("")
                        self.box.showBox("Info", "Registered successfully! Login to continue.", "i")
                else:
                    self.box.showBox("Error", "Something went wrong! Please restart the aprogram.", "e")
                
                if self.database.myDB.is_connected():
                    self.database.disconnect()


    def login(self):
        name, pwd = self.frames.get("auth").name.get(), self.frames.get("auth").pwd.get()

        if len(name) !=0 and len(pwd) !=0:
            info = self.database.connect()
            
            if info[0] == "Success":
                info = self.database.getFromAuthTable(AUTH_TABLE, name, pwd)

                if info[0] == "Success":
                    
                    if info[1][1] == "admin":
                        self.box.showBox("Info", "Welcome back Admin! You will be redirected to Admin Pannel.", "i")
                        self.showFrame("admin")

                    elif info[1][1] == "user":
                        self.box.showBox("Info", "You have successfully logged in! You will be redirected to Main Menu", "i")
                        MenuFrame.initData(info[1][2])
                        self.showFrame("menu")
                    
                    self.frames.get("auth").name.set("")
                    self.frames.get("auth").pwd.set("")
                    App.name = name
                
                elif info[0] == "Warn":
                    self.box.showBox("Warning", info[1], "w")
                    self.frames.get("auth").pwd.set("")
            
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            if self.database.myDB.is_connected():
                    self.database.disconnect()


    def logout(self):
        App.name = None
        self.showFrame("auth")


    # ================= ADMIN FUNCTIONS ======================= #
    def showUserDetails(self):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.fetchUsers(RESULT_TABLE)
            
            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            elif info[0] == "Warn":
                self.box.showBox("Warning", info[1], "w")
                self.showFrame("admin")

            else:
                info = info[1]
                info = tuple(enumerate(info))
                UserManageFrame.initData(self.frames.get("uManage"), info)
                self.showFrame("uManage")
        
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
        if self.database.myDB.is_connected():
                    self.database.disconnect()


    def showQuizDetails(self):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.fetchQuests(QUIZ_TABLE)

            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            else:
                info = info[1]
                info = tuple(enumerate(info)) if len(info) != 0 else ()
                QuizManageFrame.initData(self.frames.get("qManage"), info)
                self.showFrame("qManage")
        
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
        if self.database.myDB.is_connected():
                    self.database.disconnect()


    def saveQuest(self, data):
        canSave = True
        availUsers = True
        doChange = True

        for i in data:
            if len(i) == 0 or i.isspace():
                canSave = False
        
        if canSave:
            info = self.database.connect()
            
            if info[0] == "Success":

                info = self.database.fetchUsers(RESULT_TABLE)
                availUsers = False if info[0] != "Success" else True

                if availUsers:
                    doChange = self.box.showOkBox("Alert", "Saving the question will clear the users data who have attempted the quiz till now!")
        
                if doChange:
                    info = self.database.saveQuests(QUIZ_TABLE, data)
                    if info[0] == "Success":
                        if self.database.clearTable(RESULT_TABLE)[0] == "Success":
                            info = self.database.updateAttemptAll(AUTH_TABLE, 0)
                            if info[0] == "Success":
                                self.box.showBox("Info", "Questions added successfully.", "i")
                                self.showQuizDetails()
        
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
            if self.database.myDB.is_connected():
                        self.database.disconnect()

    
    def saveQuestMultiple(self, values):
        canSave = True
        availUsers = True
        doChange = True

        for value in values:
            for i in value:
                if len(i) == 0 or i.isspace():
                    canSave = False

        if canSave:
            info = self.database.connect()
            
            if info[0] == "Success":
                availUsers = False if info[0] != "Success" else True

                if availUsers:
                    doChange = self.box.showOkBox("Alert", "Saving the questions will clear the users data who have attempted the quiz till now!")
        
                if doChange:
                    info = self.database.saveQuests(QUIZ_TABLE, values, True)
                    if info[0] == "Success":
                        if self.database.clearTable(RESULT_TABLE)[0] == "Success":
                            info = self.database.updateAttemptAll(AUTH_TABLE, 0)
                            if info[0] == "Success":
                                self.box.showBox("Info", "Successfully added all the questions.", "i")
                                self.showQuizDetails()
                    else:
                        self.box.showBox("Error", "Something went wrong! Please recheck the format of questions.", "e")
            
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        
            if self.database.myDB.is_connected():
                        self.database.disconnect()


    def delUserRes(self, tbName:str, name:str, value:int):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.delResultByName(tbName, name)
            if info[0] == "Success":
                info = self.database.updateAttempt(AUTH_TABLE, value, name)
                if info[0] == "Success":
                    self.box.showBox("Info", "Successfully deleted the user data!", "i")
                    self.showUserDetails()
                else:
                    self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

        if self.database.myDB.is_connected():
                        self.database.disconnect()



    # ================= USER FUNCTIONS ======================= #
    def playQuiz(self, attempted:int):
        if attempted == 0:
            info = self.database.connect()
            
            if info[0] == "Success":
                info = self.database.fetchQuests(QUIZ_TABLE)

                if info[0] == "Error":
                    self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

                else:
                    info = info[1]
                    info = tuple(enumerate(info)) if len(info) != 0 else ()
                    if len(info) != 0:
                        QuizFrame.initData(self.frames.get("quiz"), info)
                        self.frames.get("quiz").focus_set()
                        self.showFrame("quiz")
                    else:
                        self.box.showBox("Info", "No Quiz for the time being.", "i")
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            
            if self.database.myDB.is_connected():
                self.database.disconnect()
        
        else:
            self.box.showBox("Info", "You have already given the quiz.", "i")

    
    def quizComplete(self, answers:dict, score:str, percent:str, grade:str):
        answers = json.dumps(answers)
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.insertIntoResultTable(RESULT_TABLE, (App.name, answers, grade, score, percent))
            if info[0] == "Success":
                info = self.database.updateAttempt(AUTH_TABLE, 1, App.name)

                if info[0] == "Success":
                    MenuFrame.initData(1)
                    self.showFrame("menu")
                    self.box.showBox("Info", "To check the result click the GET YOUR RESULT button.", "i")
            
            else:
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            
        if self.database.myDB.is_connected():
            self.database.disconnect()


    def showResult(self):
        info = self.database.connect()
            
        if info[0] == "Success":
            info = self.database.fetchUsers(RESULT_TABLE, App.name)
            
            if info[0] == "Error":
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")

            elif info[0] == "Warn":
                self.box.showBox("Warning", info[1], "w")

            else:
                info = info[1][0]
                ResultFrame.initData(self.frames.get("result"), info)
                self.showFrame("result")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            
        if self.database.myDB.is_connected():
            self.database.disconnect()



    # ======================== ADMIN AND USER FUNCTIONS ========================= #
    @staticmethod
    def compareWin(self, controller, name, btns):

        def close():
            self.COMPARING = False

            for btn in btns:
                btn.config(state=tk.NORMAL)

            win.destroy()

        win = tk.Toplevel(self)
        win.protocol("WM_DELETE_WINDOW", close)
        win.resizable(False, False)
        win.title("Compare Answers")

        tableFrame = tk.Frame(win, background=P_COL)
        columns = ('Question', 'Your Answer', 'Correct Answer')
        info = controller.database.connect()
            
        if info[0] == "Success":
            info = controller.database.fetchQandA(QUIZ_TABLE, RESULT_TABLE, name)
        
            if info[0] == "Success":
                realAns, myAns = info[1][0], json.loads(info[1][1][0][0])

                ttk.Style().configure("Treeview", background=T_COL,foreground=TXT_COL)
                table = ttk.Treeview(win, columns=columns)
                
                table.column("#0", width=0, stretch=tk.NO)
                table.column(columns[0], anchor=tk.W, width=400, minwidth=300)
                table.column(columns[1], anchor=tk.W, width=200, minwidth=150)
                table.column(columns[2], anchor=tk.W, width=200, minwidth=150)

                table.heading("#0", text="", anchor=tk.W)
                table.heading(columns[0], text=columns[0], anchor=tk.W)
                table.heading(columns[1], text=columns[1], anchor=tk.W)
                table.heading(columns[2], text=columns[2], anchor=tk.W)

                for i in range(len(realAns)):
                    quest, ans = realAns[i]
                    table.insert("", index=tk.END, iid=str(i), values=(quest, "Not answered" if myAns.get(quest) is None else myAns.get(quest), ans))

                table.pack()
                tableFrame.pack(expand=True, fill=tk.BOTH, anchor=tk.CENTER)
            else:
                close()
                self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
        else:
            self.box.showBox("Error", "Something went wrong! Please restart the program.", "e")
            
        if self.database.myDB.is_connected():
            self.database.disconnect()


def main():
    app = App()
    app.mainloop()
    
    
if __name__ == '__main__':
    main()
