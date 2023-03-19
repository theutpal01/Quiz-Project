from constants import *
import tkinter as tk
import tkinter.messagebox as msg
import json
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
        self.database = Database()
        info = self.database.connect(HOST, USER, PWD, DB)

        if info[0] == "Success":
            info = self.database.initTables(AUTH_TABLE, RESULT_TABLE, QUIZ_TABLE)
            print(info[0] + ":", info[1])
        else:
            print(info[0] + ":", info[1])


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
        if msg.askyesno("Close App", "Do you really want to quit the application?"):
            self.database.disconnect()
            self.destroy()


    # ================= AUTH FUNCTIONS ======================= #
    def register(self):
        print("SIGN UP")
        name, pwd = self.frames.get("auth").name.get(), self.frames.get("auth").pwd.get()

        if len(name) !=0 and len(pwd) !=0:
            
            if " " in name and name.isalnum():
                print("Username cannot contain space and should be only alpha numeric!")

            
            elif len(pwd) < 8 or len(pwd) > 20:
                print("Password should be of 8 to 20 letters.")

            else:
                
                if name == "admin":
                    print("SIGNED UP")
                    info = self.database.insertIntoAuthTable(AUTH_TABLE, (name, pwd), True)
                    print(info)
                else:
                    info = self.database.insertIntoAuthTable(AUTH_TABLE, (name, pwd))
                    print(info)

                if info[0] == "Error":
                    if info[1][0] == 1062:
                        print("Username already taken! Please use a different username.")
                        self.frames.get("auth").pwd.set("")
                    else:
                        print("Something went wrong! Please try again.")
                else:
                    self.frames.get("auth").name.set("")
                    self.frames.get("auth").pwd.set("")
                    print("Registered successfully! Login to continue.")


    def login(self):
        name, pwd = self.frames.get("auth").name.get(), self.frames.get("auth").pwd.get()

        if len(name) !=0 and len(pwd) !=0:
            info = self.database.getFromAuthTable(AUTH_TABLE, name, pwd)

            if info[0] == "Success":
                
                if info[1][1] == "admin":
                    print("Welcome back Admin! You will be redirected to Admin Pannel.")
                    self.showFrame("admin")

                elif info[1][1] == "user":
                    print("You have successfully logged in! You will be redirected to Main Menu")
                    print(info[1][2], type(info[1][2]))
                    MenuFrame.initData(info[1][2])
                    self.showFrame("menu")
                
                self.frames.get("auth").name.set("")
                self.frames.get("auth").pwd.set("")
                App.name = name
            
            elif info[0] == "Warn":
                print(info[1])
                self.frames.get("auth").pwd.set("")

            else:
                print("Something went wrong! Please try again.")


    def logout(self):
        App.name = None
        self.showFrame("auth")


    # ================= ADMIN FUNCTIONS ======================= #
    def showUserDetails(self):
        info = self.database.fetchUsers(RESULT_TABLE)
        
        if info[0] == "Error":
            print("Something went wrong! Please restart the program.")

        elif info[0] == "Warn":
            print(info[1])

        else:
            info = info[1]
            info = tuple(enumerate(info))
            UserManageFrame.initData(self.frames.get("uManage"), info)
            self.showFrame("uManage")


    def showQuizDetails(self):
        info = self.database.fetchQuests(QUIZ_TABLE)

        if info[0] == "Error":
            print("Something went wrong! Please restart the program.")

        else:
            info = info[1]
            info = tuple(enumerate(info)) if len(info) != 0 else ()
            QuizManageFrame.initData(self.frames.get("qManage"), info)
            self.showFrame("qManage")


    def saveQuest(self, data):
        canSave = True
        for i in data:
            if len(i) == 0 or i.isspace():
                canSave = False
        
        if canSave:
            info = self.database.saveQuests(QUIZ_TABLE, data)
            print(info)
            self.showQuizDetails()

    
    def saveQuestMultiple(self, values):
        canSave = True
        for value in values:
            for i in value:
                if len(i) == 0 or i.isspace():
                    canSave = False

        if canSave:
            info = self.database.saveQuests(QUIZ_TABLE, values, True)
            if info[0] == "Success":
                print("Successfully added all the questions.")
                self.showQuizDetails()
            else:
                print("Something went wrong! Please restart the program.")


    # ================= USER FUNCTIONS ======================= #
    def playQuiz(self, attempted:int):
        print(attempted)
        if attempted == 0:
            info = self.database.fetchQuests(QUIZ_TABLE)

            if info[0] == "Error":
                print("Something went wrong! Please restart the program.")

            else:
                info = info[1]
                info = tuple(enumerate(info)) if len(info) != 0 else ()
                if len(info) != 0:
                    QuizFrame.initData(self.frames.get("quiz"), info)
                    self.showFrame("quiz")
                else:
                    print("No Quiz for the time being.")
        else:
            print("You have already given the quiz.")

    
    def quizComplete(self, answers:dict, score:str, percent:str, grade:str):
        answers = json.dumps(answers)
        info = self.database.insertIntoResultTable(RESULT_TABLE, (App.name, answers, grade, score, percent))
        print(info)
        if info[0] == "Success":
            info = self.database.updateAttempt(AUTH_TABLE, 1, App.name)

            if info[0] == "Success":
                MenuFrame.initData(1)
                self.showFrame("menu")
                print(info[1])
        
        else:
            print("Something went wrong! Please restart the program")


    def showResult(self):
        info = self.database.fetchUsers(RESULT_TABLE, App.name)
        
        if info[0] == "Error":
            print("Something went wrong! Please restart the program.")

        elif info[0] == "Warn":
            print(info[1])

        else:
            info = info[1][0]
            ResultFrame.initData(self.frames.get("result"), info)
            self.showFrame("result")


def main():
    app = App()
    app.mainloop()
    
    
if __name__ == '__main__':
    main()
